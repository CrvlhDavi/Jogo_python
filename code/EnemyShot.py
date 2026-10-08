from code.entity1 import Entity1

from code.Const import ENEMY_SHOT_DAMAGE, ENTITY_SPEED

class EnemyShot(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.damage = ENEMY_SHOT_DAMAGE


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]