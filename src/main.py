import flet as ft
from story import intro_rimsky
from view.shop_view import intro_shop
from component.shop import gold
from view.shop_view import cahs_counter
from view.shop_view import shoping_response
from component.shop import rope
from component.shop import lampoil
from component.shop import  bomb

import component.create_person as p

person = p.createPerson()


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
            ft.Text(intro_rimsky(person)),
            ft.Button("Till startsidan", on_click=show_start),
            ft.Button("Till afären", on_click=show_shop),
        ]
        page.update()

    def show_shop(e=None):
        area.controls = [
            ft.Text("I affären", size=26),
            ft.Button("Till startsidan", on_click=show_start),
            ft.Text(intro_shop()),
            ft.Button("skaffa guld", on_click=gold),
            ft.Text(cahs_counter(gold)),
            ft.Text(shoping_response("Link")),
            ft.Button("skaffa lampolja", on_click=lampoil),
            ft.Button("skaffa rep", on_click=rope),
            ft.Button("skaffa bomber", on_click=bomb),
        ]
        page.update()
 
    page.add(area)
    show_start()
ft.run(main)
