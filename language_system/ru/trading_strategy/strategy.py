import flet as ft
import time

def Trading_Strategy(page):
    language_selects = ft.Dropdown(
            width = 280,
            label = 'Выберите стратегию',
            options = [ft.dropdown.Option("Скальпинг"),
                       ft.dropdown.Option("Интрадей"),
                       ft.dropdown.Option("Трендовая торговля"),
                       ft.dropdown.Option("Контртрендовая торговля"),
                       ft.dropdown.Option("Торговля по уровням поддержки и сопротивления"),
                       ft.dropdown.Option("Торговля с использованием индикаторов"),
                       ft.dropdown.Option("Арбитраж"),
                       ft.dropdown.Option("Новостной трейдинг"),
                       ft.dropdown.Option("Торговля на основе объемов"),
                       ft.dropdown.Option("Кастомный"),
                       ]
        )
    error_language = ft.Text(color='red')
    def language_select(e):
            if language_selects.value == None:
                error_language.color = 'red'
                error_language.value = "Нельзя выбрать пустое значение" 
                error_language.update()
                time.sleep(5)
                error_language.value = ''
                error_language.update()
            else:
                error_language.color = 'green'
                error_language.value = 'Успешно обновлено'
                error_language.update()
                time.sleep(5)
                error_language.value = ''
                error_language.update()
    language_submit = ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=language_select)


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
                    language_selects,
                    language_submit

                ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        
        ]
    )
    return content