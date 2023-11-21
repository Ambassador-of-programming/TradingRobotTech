import flet as ft

def Notes(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Мои заметки", size=30), 
                ft.IconButton(icon=ft.icons.NOTES, icon_size=30),
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