import sys
from map import *
from player import *
from raycasting import *
from object_renderer import *
from weapon import *
from sound import *
from pathfinding import *
from button import *
import button


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)  # Create a display window
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 600)
        self.count_lvl = 0
        self.titri_image = pg.image.load('resources/textures/titri.png').convert_alpha()
        self.start_img = pg.image.load('resources/textures/START.png').convert_alpha()
        self.exit_img = pg.image.load('resources/textures/EXIT.png').convert_alpha()
        self.menu1_image = pg.image.load('resources/textures/menu.png').convert_alpha()
        self.menu_trigger = True
        self.start_button = Button(100, 200, self.start_img, 0.8)
        self.exit_button = Button(400, 200, self.exit_img, 0.8)
        self.menu()

    def menu(self):
        pg.display.set_caption('Kill_Field')
        self.screen.blit(self.menu1_image, (0, 0))
        self.start_button = button.Button(50, 100, self.start_img, 0.8)
        self.exit_button = button.Button(50, 300, self.exit_img, 0.8)
        while self.menu_trigger:
            self.screen.blit(self.menu1_image, RES)
            if self.start_button.draw(self.screen):
                self.menu_trigger = False
            if self.exit_button.draw(self.screen):
                sys.exit()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            pg.display.update()
        self.new_game()

    def new_game(self):
        if self.count_lvl < 2:
            pg.mouse.set_visible(False)
            self.map = Map(self)
            self.player = Player(self)
            self.object_renderer = ObjectRenderer(self)
            self.raycasting = RayCasting(self)
            self.player.x, self.player.y = PLAYER_POS
            self.object_handler = ObjectHandler(self)
            self.weapon = Weapon(self)
            self.sound = Sound(self)
            self.pathfinding = PathFinding(self)
        else:
            self.screen.blit(self.titri_image, (0, 0))
            pg.display.flip()
            pg.time.delay(9000)
            sys.exit()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        if self.menu_trigger == False:
            while True:
                self.check_events()
                self.update()
                self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()