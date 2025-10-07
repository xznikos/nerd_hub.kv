from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ProductCard(BoxLayout):
    title = StringProperty('')
    price = StringProperty('')

class HomeScreen(Screen):
    def on_enter(self):
        grid = self.ids.products_grid
        if len(grid.children) == 0:
            produtos = [
                {"title": "FORZA - Xbox Series X", "price": "R$ 179,00"},
                {"title": "LEGO Minecraft - Aventura", "price": "R$ 1.349,90"},
                {"title": "PlayStation 5 Pro", "price": "R$ 6.509,00"},
                {"title": "PlayStation Portal", "price": "R$ 1.349,90"},
                {"title": "Funko Pop! Star Wars", "price": "R$ 389,90"},
                {"title": "Camiseta Marvel Avengers", "price": "R$ 82,35"},
                {"title": "Pelúcia Chewbacca", "price": "R$ 141,50"},
                {"title": "LEGO Star Wars - 75257", "price": "R$ 201,00"},
            ]
            for p in produtos:
                grid.add_widget(ProductCard(title=p["title"], price=p["price"]))
