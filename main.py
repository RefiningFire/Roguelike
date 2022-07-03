from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivy.core.window import Window
Window.fullscreen = 'auto'


class MainScreen(Screen):
    pass

class Roguelike(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(MainScreen(name='main'))

        return sm


if __name__ == '__main__':
    app = Roguelike()
    app.run()
