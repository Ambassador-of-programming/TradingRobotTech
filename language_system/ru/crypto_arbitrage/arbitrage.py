import flet as ft

def Crypto_Arbitrage(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Арбитраж", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ROUNDED, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.Text("Раздел арбитраж находится на стадии разработки. В новых обновлениях она появится")
                ]
            ),
        ]
    )
    return content