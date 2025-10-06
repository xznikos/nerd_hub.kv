from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

KV = f'''
<AccountScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(16)
        canvas.before:
            Color:
                rgba: 0.07, 0.57, 0.38, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_y: None
            height: dp(56)
            Button:
                text: "⬅ Voltar"
                size_hint_x: None
                width: dp(100)
                background_normal: ''
                background_color: 1,1,1,1
                color: 0,0,0,1
                on_release:
                    app.root.current = "main"
            Label:
                text: "Minha Conta"
                color: 1,1,1,1
                font_size: '18sp'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: "Nome: Nikolas Kaio"
                color: 1,1,1,1
                font_size: '16sp'
            Label:
                text: "E-mail: exemplo@email.com"
                color: 1,1,1,1
                font_size: '16sp'
            Label:
                text: "Pedidos: 3"
                color: 1,1,1,1
                font_size: '16sp'
'''

Builder.load_string(KV)

class AccountScreen(Screen):
    pass
