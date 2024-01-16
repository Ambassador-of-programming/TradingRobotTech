import flet as ft

async def support(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Служба поддержки", size=30), 
                ft.IconButton(icon=ft.icons.SUPPORT_AGENT, icon_size=30),
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
                    ft.Text('Всё о брокерах')
                ],
            ),

            ft.Row(
                [
                    ft.Text('Всё о стратегиях для трейдинга')
                ],
            ),

            ft.Row(
                [
                    ft.Text("Связаться со службой поддержки")
                ]
            ),

            ft.Row(
                [
                    ft.Text("Идеи и Предложения")
                ]
            ),

            
        ]
    )
    return content