import flet as ft

def Statistic(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Моя статистика", size=30), 
                ft.IconButton(icon=ft.icons.ANALYTICS, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.Text("Раздел моя статистика находится на стадии разработки. В новых обновлениях она появится")
                ]
            ),

        ]
    )
    return content