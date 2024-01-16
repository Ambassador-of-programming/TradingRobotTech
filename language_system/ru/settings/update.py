import flet as ft
import aiohttp

async def update_app(page):
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text(
                    "Центр обновлений TradingRobotTech", 
                    size=30,
                    ), 
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),


            ft.Row(
                [
                    ft.Text(
                        "Раздел обновление находится на стадии разработки. В новых обновлениях она появится",)
                ]
            ),
        ]
    )
    return content