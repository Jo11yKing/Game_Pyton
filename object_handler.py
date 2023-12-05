from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}


        if self.game.count_lvl == 0:
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(14.5, 13.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(5.5, 15.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(8.5, 20.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(2.5, 23.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(12.5, 25.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(5.5, 29.5)))
            add_sprite(AnimatedSprites(game, pos=(2.5, 5.5)))
            add_sprite(AnimatedSprites(game, pos=(14.5, 2.5)))
            add_sprite(AnimatedSprites(game, pos=(1.5, 22.5)))
            add_sprite(AnimatedSprites(game, pos=(14.5, 7.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(8.5, 4.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 9.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 12.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 19.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 27.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(3.5, 2.0)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(18.5, 2.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(30.5, 14.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png', scale=0.8, pos=(11.5, 6.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png', scale=0.8, pos=(4.5, 17.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png', scale=0.8,pos=(11.5, 27.5)))
            self.enemies = 15  # npc count
            self.npc_types = [ChaosRobotNPC, ChaosMarineNPC]
            self.weights = [10, 90]
            self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
            self.spawn_npc()
        else:
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(14.5, 1.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(8.5, 17.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(1.5, 18.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(6.5, 27.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'mecanicus_lamp/0.png', pos=(1.5, 30.5)))
            add_sprite(AnimatedSprites(game, pos=(4.5, 3.5)))
            add_sprite(AnimatedSprites(game, pos=(14.5, 13.5)))
            add_sprite(AnimatedSprites(game, pos=(1.5, 16.5)))
            add_sprite(AnimatedSprites(game, pos=(13.5, 26.5)))
            add_sprite(AnimatedSprites(game, pos=(1.5, 28.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(8.5, 1.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(5.5, 6.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 8.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(7.5, 10.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 16.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(1.5, 4.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(4.5, 12.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(8.5, 21.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'fontan/0.png', pos=(14.5, 30.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png', scale=0.8, pos=(3.5, 6.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png', scale=0.8, pos=(1.5, 21.5)))
            add_sprite(AnimatedSprites(game, path=self.anim_sprite_path + 'servitor/0.png',scale=0.8, pos=(11.5, 27.5)))
            self.enemies = 20 # npc count
            self.npc_types = [OrkNPC, OrkMekkaNPC]
            self.weights = [90, 10]
            self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
            self.spawn_npc()


    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.count_lvl += 1

            self.game.new_game()
        else:
            pass

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
