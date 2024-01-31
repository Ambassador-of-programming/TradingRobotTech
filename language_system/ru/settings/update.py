import flet as ft
import aiohttp
from current_version import current_version

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
                        f"У вас установлена версия приложения:",
                    ),
                    ft.Text(
                        current_version,
                        color='yellow'
                    ),
                ]
            ),
        ]
    )
    return content