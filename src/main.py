import flet as ft
from story import intro_rimsky
from view.shop_view import intro_shop



def main(page: ft.Page):
    page.title = "Äventyret"
    page.bgcolor = ft.Colors.AMBER_100
    page.padding = 30
 
    area = ft.Column(spacing=15)
 
    def show_start(e=None):
        area.controls = [
            ft.Text("Mitt äventyr", size=32,
                    weight=ft.FontWeight.BOLD),
            ft.Text("Ett äventyr där dina val spelar roll."),
            ft.Button("Starta", on_click=show_story),
        ]
        page.update()
 
    def show_story(e=None):
        area.controls = [
            ft.Text("Vid bron", size=26),
            ft.Text(intro_rimsky("ada")),
            ft.Button("Till startsidan", on_click=show_start),
            ft.Button("Till afären", on_click=show_shop),
        ]
        page.update()

    def show_shop(e=None):
        area.controls = [
            ft.Text("I affären", size=26),
            ft.Text(intro_shop()),
            ft.Button("Till startsidan", on_click=show_start),
        ]
        page.update()
 
    page.add(area)
    show_start()
ft.run(main)
