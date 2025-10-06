# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# Tamanho da janela (apenas para testes no desktop)
Window.size = (420, 900)

KV = '''
#:import dp kivy.metrics.dp

<Header@BoxLayout>:
    size_hint_y: None
    height: dp(56)
    padding: dp(8)
    spacing: dp(8)
    canvas.before:
        Color:
            rgba: 0.07, 0.57, 0.38, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "NERD HUB"
        color: 1, 1, 1, 1
        font_size: '18sp'
        size_hint_x: None
        width: dp(100)
        
    TextInput:
        hint_text: "O que você está procurando?"
        multiline: False
        background_normal: ''
        background_active: ''
        background_color: 1, 1, 1, 1
        foreground_color: 0, 0, 0, 1
        size_hint_x: 1
        padding: [dp(8), dp(8)]
        font_size: '14sp'
    Button:
        text: "🔍"
        background_normal: ''
        background_color: 1, 1, 1, 1
        size_hint_x: None
        width: dp(40)

<Banner@BoxLayout>:
    size_hint_y: None
    height: dp(150)
    padding: dp(10)
    spacing: dp(10)
    canvas.before:
        Color:
            rgba: 0.15, 0.6, 0.85, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),]
    Label:
        markup: True
        text: "[b]50% OFF\\nProdutos Selecionados[/b]"
        color: 1, 1, 1, 1
        font_size: '20sp'
        halign: 'center'
        valign: 'middle'
        text_size: self.size

<SubBanner@BoxLayout>:
    size_hint_y: None
    height: dp(70)
    spacing: dp(10)
    padding: dp(5)
    BoxLayout:
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            markup: True
            text: "[b]STAR\\nWARS[/b]"
            color: 1,1,1,1
            halign: 'center'
            valign: 'middle'
            text_size: self.size
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1, 0.85, 0.2, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Disney+"
            color: 0,0,0,1
            halign: 'center'
            valign: 'middle'
            text_size: self.size

<ProductCard>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(250)
    padding: dp(8)
    spacing: dp(5)
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8),]
    # Área da imagem (placeholder se não houver image_source)
    BoxLayout:
        size_hint_y: None
        height: dp(120)
        canvas.before:
            Color:
                rgba: (0.95, 0.95, 0.95, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        Image:
            id: thumb
            source: root.image_source
            allow_stretch: True
            keep_ratio: True
            opacity: 1 if root.image_source else 0
        Label:
            text: "IMG" if not root.image_source else ""
            color: 0, 0, 0, 0.5
            halign: 'center'
            valign: 'middle'
            text_size: self.size
    Label:
        text: root.title
        text_size: self.width, None
        halign: 'center'
        valign: 'middle'
        color: 0,0,0,1
        size_hint_y: None
        height: dp(40)
    Label:
        text: root.price
        size_hint_y: None
        height: dp(22)
        halign: 'center'
        valign: 'middle'
        color: 0,0,0,1
    Button:
        text: "Adicionar ao Carrinho"
        size_hint_y: None
        height: dp(34)
        background_normal: ''
        background_color: 0.07, 0.57, 0.38, 1
        color: 1, 1, 1, 1
        font_size: '12sp'

<MainScreen>:
    orientation: 'vertical'
    padding: dp(8)
    spacing: dp(8)
    Header:
    ScrollView:
        do_scroll_x: False
        GridLayout:
            cols: 1
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height
            Banner:
            SubBanner:
            BoxLayout:
                size_hint_y: None
                height: dp(36)
                canvas.before:
                    Color:
                        rgba: 0.92, 0.92, 0.92, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(6),]
                Label:
                    text: "PRODUTOS EM DESTAQUE"
                    color: 0, 0, 0, 1
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: "01 : 54 : 45"
                    color: 0, 0, 0, 1
                    size_hint_x: None
                    width: dp(100)
                    halign: 'right'
                    valign: 'middle'
            GridLayout:
                id: products_grid
                cols: 2
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height
                row_default_height: dp(250)
            BoxLayout:
                size_hint_y: None
                height: dp(60)
                spacing: dp(8)
                TextInput:
                    hint_text: "Digite seu e-mail"
                    multiline: False
                    background_normal: ''
                    background_active: ''
                    background_color: 1,1,1,1
                    foreground_color: 0,0,0,1
                    padding: [dp(8), dp(8)]
                Button:
                    text: "ENVIAR"
                    background_normal: ''
                    background_color: 0.07, 0.57, 0.38, 1
                    color: 1, 1, 1, 1
'''

# Carrega KV antes das classes
Builder.load_string(KV)


# Widget Python com propriedades - evita problemas de acesso a root.title no KV
class ProductCard(BoxLayout):
    image_source = StringProperty('')
    title = StringProperty('')
    price = StringProperty('')


class MainScreen(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        root = MainScreen()

        # Produtos (adicione "image_source" com caminho/URL se quiser imagens)
        products = [
            {"title": "FORZA - Xbox Series X", "price": "R$ 179,00", "image_source": ""},
            {"title": "LEGO Minecraft - Aventura", "price": "R$ 1.349,90", "image_source": ""},
            {"title": "PlayStation 5 Pro", "price": "R$ 6.509,00", "image_source": ""},
            {"title": "PlayStation Portal", "price": "R$ 1.349,90", "image_source": ""},
            {"title": "Funko Pop! Star Wars", "price": "R$ 389,90", "image_source": ""},
            {"title": "Camiseta Marvel Avengers", "price": "R$ 82,35", "image_source": ""},
            {"title": "Pelúcia Chewbacca", "price": "R$ 141,50", "image_source": ""},
            {"title": "LEGO Star Wars - 75257", "price": "R$ 201,00", "image_source": ""},
        ]

        grid = root.ids.products_grid
        for p in products:
            card = ProductCard()
            card.title = p.get("title", "")
            card.price = p.get("price", "")
            card.image_source = p.get("image_source", "")
            grid.add_widget(card)

        return root


if __name__ == "__main__":
    MainApp().run()
