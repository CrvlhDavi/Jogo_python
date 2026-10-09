from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity1 import Entity1
from code.player import Player

#Apaga os inimigos após sairem da tela para economizar memoria
class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity1):#metodo privado que não é possivel invocar em outro lugar
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <=0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent01: Entity1, ent02: Entity1):
        valid_interaction = (
            isinstance(ent01, Enemy) and isinstance(ent02, PlayerShot)
            or isinstance(ent01, PlayerShot) and isinstance(ent02, Enemy)
            or isinstance(ent01, Player) and isinstance(ent02, EnemyShot)
            or isinstance(ent01, EnemyShot) and isinstance(ent02, Player)
        )
        if (valid_interaction and ent01.health > 0 and ent02.health > 0
                and ent01.rect.colliderect(ent02.rect)):
            ent01.health -= ent02.damage
            ent02.health -= ent01.damage
            ent01.last_dmg = ent02.name
            ent02.last_dmg = ent01.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity1]):
        player_name = enemy.last_dmg.removesuffix('Shot')
        for ent in entity_list:
            if isinstance(ent, Player) and ent.name == player_name:
                ent.score += enemy.score
                break

    @staticmethod
    def verify_collision(entity_list: list[Entity1]):
        for entity in entity_list:
            EntityMediator.__verify_collision_window(entity)

        for i, entity01 in enumerate(entity_list):
            for entity02 in entity_list[i + 1:]:
                EntityMediator.__verify_collision_entity(entity01, entity02)


    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent) #se a vida do inimigo for menor ou igual a zero, ele é removido da lista
