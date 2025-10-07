from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from paginas.home import HomeScreen
from paginas.login import LoginScreen

# Tamanho da janela (opcional, para desktop)
Window.size = (420, 900)

class Gerenciador(ScreenManager):
    pass

class NerdHubApp(App):
    def build(self):
        # Carrega os arquivos KV
        Builder.load_file("telas/home.kv")
        Builder.load_file("telas/login.kv")

        sm = Gerenciador()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        return sm

if __name__ == "__main__":
    NerdHubApp().run()
