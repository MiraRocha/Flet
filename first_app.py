from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    container = Container(
        width=400,height=850,
        bgcolor=BG, 
        border_radius=35,
        #content=Stack(
          #  controls=[
        #page_1,
               # page_2
         #   ]
        #)
        )
    page.add(container)


app(target=main)