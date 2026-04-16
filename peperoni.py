import flet as ft
 
def main(page: ft.Page):
 
    def cambiar(e):
        pepperoni.visible = switchpeperoni.value
        olives.visible = switcholives.value
        bacon.visible = switchbacon.value
        page.update()
 
    base = ft.Image(src="pizzabase.png", width=300, height=300)
    pepperoni = ft.Image(src="peperoni2.png", visible=False)
    olives = ft.Image(src="olive2.png", visible=False, width=300, height= 250)
    bacon = ft.Image(src="bacon2.png", visible=False, width= 250)
 
    switchpeperoni = ft.Switch(label="Peperoni", on_change=cambiar)
    switcholives = ft.Switch(label="olives", on_change=cambiar)
    switchbacon = ft.Switch(label="bacon", on_change=cambiar)
 
    page.add(ft.Row([
            ft.Stack([base, pepperoni, olives, bacon]),
            ft.Column([switchpeperoni, switcholives, switchbacon])
        ]))
 
ft.run(main)