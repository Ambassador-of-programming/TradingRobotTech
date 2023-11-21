import flet as ft

def Trading_Strategy(page):

    text_apikey = ft.TextField(label='Введите Api Key', password=True, can_reveal_password=True)
    text_secretkey = ft.TextField(label='Введите Secret Key', password=True, can_reveal_password=True)
    error_apikey = ft.Text(color='red')
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Мои стратегии", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ALT, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
            ft.Row(
                [
                    text_apikey
                ],
            ),
            ft.Row(
                [
                    text_secretkey
                ]
            ),
            ft.Row(
                [
                    ft.Text("Github: https://github.com/CodingJQ")
                ]
            )
        ]
    )
    return content