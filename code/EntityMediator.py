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
    def verify_collision(entity_list:list[Entity1]):
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)

            if isinstance(ent, EnemyShot):
                for target in entity_list:
                    if isinstance(target, Player) and ent.rect.colliderect(target.rect):
                        target.health -= ent.damage
                        ent.health = 0
                        break

    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent) #se a vida do inimigo for menor ou igual a zero, ele é removido da lista
