from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

class ProductCard(BoxLayout):
    title = StringProperty('')
    price = StringProperty('')

class HomeScreen(Screen):
    def on_enter(self):
        # --- Carrossel de Subbanners com botões ---
        carousel = self.ids.subbanner_carousel
        if len(carousel.children) == 0:
            marcas = [
                {"nome": "PlayStation", "cor": (0.15, 0.5, 0.85, 1), "tela": "playstation"},
                {"nome": "Xbox", "cor": (0.0, 0.5, 0.0, 1), "tela": "xbox"},
                {"nome": "Marvel", "cor": (0.85, 0, 0, 1), "tela": "marvel"},
                {"nome": "Star Wars", "cor": (0.1, 0.1, 0.1, 1), "tela": "starwars"},
                {"nome": "Disney+", "cor": (1, 0.85, 0.2, 1), "tela": "disney"},
            ]
            for m in marcas:
                btn = Button(
                    text=f"[b]{m['nome']}[/b]",
                    markup=True,
                    color=(1, 1, 1, 1) if m['nome'] != "Disney+" else (0,0,0,1),
                    background_normal='',
                    background_color=m['cor'],
                    font_size='16sp'
                )
                btn.bind(on_release=lambda instance, tela=m['tela']: self.mudar_tela(tela))
                carousel.add_widget(btn)

        # --- Grid de produtos ---
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

    def mudar_tela(self, nome_tela):
        if self.manager.has_screen(nome_tela):
            self.manager.current = nome_tela
