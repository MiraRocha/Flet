from flet import *
import flet as ft


def main(page: Page):
    
    page.add(container)
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    container = Container(
        width=400,height=850,
        bgcolor=BG, 
        border_radius=35,
        
        )
    


app(target=main)