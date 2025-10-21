from flet import *

def main(page: Page):
    BG = '#041955'
    FMG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    
    first_page_contents =  Container(
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            content=Icon(
                                Icons.MENU))
                    ]
                )
            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container( width = 400,
                height = 850,
                bgcolor = FG,
                border_radius = 35,
                padding=padding.only(top=50, left=50, right=20, bottom=5
                ),
                content= Column(
                    controls=[
                        first_page_contents
                    ]
                )

            )
        ]
    )
    container = Container (   
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content= Stack(
            controls = [
                page_1,
                page_2,
            ]
        )
    )
        
    
    
    page.add(container)

app(target=main)