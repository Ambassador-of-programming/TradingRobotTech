import flet as ft
import time
import asyncio

async def backtesting(page):
    language_selects = ft.Dropdown(
            width = 280,
            label = 'Выберите метод тестирования',
            options = [ft.dropdown.Option("Backtrader"),
                       ft.dropdown.Option("Zipline"),
                        ft.dropdown.Option("Трендовая торговля"),
                       ],
        )
    error_language = ft.Text(color='red')

    async def language_select(event):
        if language_selects.value == None:
            error_language.color = 'red'
            error_language.value = "Нельзя выбрать пустое значение" 
            await error_language.update_async()
            await asyncio.sleep(5)
            error_language.value = ''
            await error_language.update_async()
        else:
            error_language.color = 'green'
            error_language.value = 'Успешно обновлено'
            await error_language.update_async()
            await asyncio.sleep(5)
            error_language.value = ''
            await error_language.update_async()

    async def language_submit():
        return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=language_select)
    
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Мои бэктесты", size=30), 
                    ft.IconButton(icon=ft.icons.SETTINGS_CELL, icon_size=30),
                ], 
                    alignment=ft.MainAxisAlignment.CENTER
        ),

            ft.Row(
                [
                    language_selects,
                    error_language,
                    await language_submit(),
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        scale=None
    )
    return content