from flet import padding

from flet import *

def main(page: Page):
    BG = '#041955'
    FMG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]#chamamos o nosso dicionario de rotas aqui
        )
    create_task_view = Container(
        content=Container(on_click=lambda _: page.go('/'),
            height=40,
            width=40,
            content=Text('x')
            )
    )  

    tasks = Column(
        height=400,
        scroll='auto',
        #controls=[
            #Container(height=50,width=300,bgcolor='red'),
            #Container(height=50,width=300,bgcolor='red'),
            #Container(height=50,width=300,bgcolor='red'),
            #Container(height=50,width=300,bgcolor='red'),
            #]
    )
    for i in range(10):
        tasks.controls.append(
            Container(
                height=50,
                width=300,
                bgcolor=BG,
                border_radius=25
                )
        )


    tasks = Column()
    
    categories_card = Row(  
        scroll='auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for index, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG, 
                height=110, 
                width=170,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=index*30),
                            content= Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )

            )
        )

    first_page_contents =  Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(
                                Icons.MENU)),
                        Row(
                            controls=[
                                Icon(Icons.SEARCH),
                                Icon(Icons.NOTIFICATIONS_OUTLINED)

                                ],
                            ),
                    ],
                ),
                Container(height=20),
                Text(
                    value='What\'s up, Mira!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon=Icons.ADD,
                            on_click=lambda _: page.go('/create_task')

                        )
                    ]
                )
            ],
        ),
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container( width = 400,
                height = 850,
                bgcolor = FG,
                border_radius = 35,
                padding=padding.only(top=50, left=50, right=20, bottom=5),
                content= Column(
                    controls=[
                        first_page_contents
                    ]
                )

            )
        ]
    )
    
    container= Container (   
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content= Stack(
            controls = [
                page_1,
                page_2,
            ],
        ),
    )    
    
    pages = {#fizemos um dicionario para definir rotas de uma pagina para a outra
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task':View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }

    

    page.add(container)
    
    page.on_route_change = route_change
    page.go(page.route)

app(target=main,  port=0)