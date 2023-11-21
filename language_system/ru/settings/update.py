import flet as ft

def Update_app(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Обновление", size=30), 
                ft.IconButton(icon=ft.icons.NEWSPAPER, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.Text("Обновление системы")
                ]
            ),
        ]
    )
    return content