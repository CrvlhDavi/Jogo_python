from code.enemy import Enemy
from code.entity1 import Entity1

#Apaga os inimigos após sairem da tela para economizar memoria
class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity1):#metodo privado que não é possivel invocar em outro lugar
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list:list[Entity1]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent) #se a vida do inimigo for menor ou igual a zero, ele é removido da lista
