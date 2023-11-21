import flet as ft

def Parsing_News(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Парсинг новостей", size=30), 
                ft.IconButton(icon=ft.icons.NEWSPAPER, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.Text("Раздел парсинг новостей находится на стадии разработки. В новых обновлениях она появится")
                ]
            ),
        ]
    )
    return content