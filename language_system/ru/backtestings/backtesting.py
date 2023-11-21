import flet as ft
import time

def Backtesting(page):

    language_selects = ft.Dropdown(
            width = 280,
            label = 'Выберите метод тестирования',
            options = [ft.dropdown.Option("Backtrader"),
                       ft.dropdown.Option("Zipline"),
                       ft.dropdown.Option("Трендовая торговля"),
                       ],
        )
    error_language = ft.Text(color='red')
    def language_select(e):
        pass
            # if language_selects.value == None:
            #     error_language.color = 'red'
            #     error_language.value = "Нельзя выбрать пустое значение" 
            #     error_language.update()
            #     time.sleep(5)
            #     error_language.value = ''
            #     error_language.update()
            # else:
            #     error_language.color = 'green'
            #     error_language.value = 'Успешно обновлено'
            #     error_language.update()
            #     time.sleep(5)
            #     error_language.value = ''
            #     error_language.update()
    language_submit = ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=language_select)
    
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
                    language_submit,
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
    )
    return content