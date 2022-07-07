from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.graphics import Color, Rectangle

from kivy.atlas import Atlas
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image

from kivy.core.window import Window
Window.fullscreen = 'auto'

import random

atlas = Atlas('graphics/DawnLike/Objects/floor.atlas')
floor_atlas = 'atlas://graphics/DawnLike/Objects/Floor/'

atlas = Atlas('graphics/DawnLike/Objects/wall.atlas')
wall_atlas = 'atlas://graphics/DawnLike/Objects/Wall/'

atlas = Atlas('graphics/DawnLike/Objects/fence.atlas')
fence_atlas = 'atlas://graphics/DawnLike/Objects/Fence/'

atlas = Atlas('graphics/DawnLike/Objects/tile.atlas')
tile_atlas = 'atlas://graphics/DawnLike/Objects/Tile/'

atlas = Atlas('graphics/DawnLike/Objects/decor0.atlas')
decor0_atlas = 'atlas://graphics/DawnLike/Objects/Decor0/'
atlas = Atlas('graphics/DawnLike/Objects/decor1.atlas')
decor1_atlas = 'atlas://graphics/DawnLike/Objects/Decor1/'

atlas = Atlas('graphics/DawnLike/Objects/door0.atlas')
door0_atlas = 'atlas://graphics/DawnLike/Objects/Door0/'
atlas = Atlas('graphics/DawnLike/Objects/door1.atlas')
door1_atlas = 'atlas://graphics/DawnLike/Objects/Door1/'

atlas = Atlas('graphics/DawnLike/Objects/effect0.atlas')
effect0_atlas = 'atlas://graphics/DawnLike/Objects/Effect0/'
atlas = Atlas('graphics/DawnLike/Objects/effect1.atlas')
effect1_atlas = 'atlas://graphics/DawnLike/Objects/Effect1/'

atlas = Atlas('graphics/DawnLike/Characters/player0.atlas')
char_0_atlas = 'atlas://graphics/DawnLike/Characters/Player0/'





class MainScreen(Screen):
    def draw_map(self,width_in_squares,height_in_squares):
        self.map = RelativeLayout(
                    pos=(0,0),
                    size_hint=(None,None),
                    size=(app.scale*width_in_squares,app.scale*height_in_squares))

        with self.map.canvas.before:
            Color(.4,.4,0,.5)
            self.map.rect = Rectangle(
                            size=self.map.size)


        self.draw_room(3,3)

        app.sm.get_screen('main').add_widget(self.map)

        self.__char_image = Image(
            source=f'{char_0_atlas}generic',
            keep_ratio=False,
            allow_stretch=True,
            size_hint=(None,None),
            size=(app.scale,app.scale),
            pos=(self.width/2-(app.scale/2),self.height/2))


        app.sm.get_screen('main').add_widget(self.__char_image)

    def move_map(self,x,y):
        self.map.pos=(self.map.x + x,self.map.y + y)


    def draw_room(self,width_in_squares,height_in_squares):
        for x in range(width_in_squares):
            for y in range(height_in_squares):
                self.__cur_square_image = Image(
                    source=f'{effect1_atlas}row_18_col_04',
                    keep_ratio=False,
                    allow_stretch=True,
                    size_hint=(None,None),
                    size=(app.scale,app.scale),
                    pos=(app.scale*x,app.scale*y))

                self.map.add_widget(self.__cur_square_image)

class Roguelike(App):
    def build(self):
        app.sm = ScreenManager(transition=SlideTransition())

        app.sm.add_widget(MainScreen(name='main'))

        # This represents the size of a square in pixels. Art is 16x16, scaling up will zoom in.
        app.scale = 64

        return app.sm

def d(sides,times=1):
    __result = 0
    for roll in range(times):
        __result += random.randint(1,sides)
    return __result


if __name__ == '__main__':
    app = Roguelike()

    app.run()
