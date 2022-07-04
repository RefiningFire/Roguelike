from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.graphics import Color, Rectangle

from kivy.atlas import Atlas
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image

from kivy.core.window import Window
Window.fullscreen = 'auto'

atlas = Atlas('graphics/DawnLike/Objects/floor.atlas')
print(atlas.textures.keys())
print()
print(atlas['dark-cobblestone-sw'])




class MainScreen(Screen):
    def draw_map(self):
        self.layout = RelativeLayout(
                    pos=(500,500),
                    size_hint=(None,None),
                    size=(300,300))

        with self.layout.canvas.before:
            Color(.4,.4,0,.5)
            self.layout.rect = Rectangle(
                            size=self.layout.size)


        self.image = Image(
            source='atlas://graphics/DawnLike/Objects/Floor/dark-cobblestone-sw',
            pos=(-142,-142))

        self.layout.add_widget(self.image)

        app.sm.get_screen('main').add_widget(self.layout)

class Roguelike(App):
    def build(self):
        app.sm = ScreenManager(transition=SlideTransition())

        app.sm.add_widget(MainScreen(name='main'))

        return app.sm


if __name__ == '__main__':
    app = Roguelike()
    app.run()
