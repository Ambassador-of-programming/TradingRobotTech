import flet as ft

def Support(page):

    text_apikey = ft.TextField(label='Введите Api Key', password=True, can_reveal_password=True)
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Служба поддержки", size=30), 
                ft.IconButton(icon=ft.icons.ANALYTICS, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
            ft.Row(
                [
                    ft.Text('Всё о криптобиржках')
                ],
            ),

            ft.Row(
                [
                    ft.Text("Связаться со службой поддержки")
                ]
            ),

            
        ]
    )
    return content