import flet as ft
from flet import Text
import time
import json

def SettingsView(page):

    def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else: 
            page.theme_mode = "dark"
            page.update()

    def resize_screen(e):
        if page.window_full_screen == False:
            page.window_full_screen = True
            page.update()
        else: 
            page.window_full_screen = False
            page.update()

    def exit_app(e):
        page.window_destroy()
    
    # Список выпадающей биржи
    with open('config\settings_secret.json', 'r') as file:
        data = json.load(file)
        keys = data["keys_api"].keys()
        keys_api = data["keys_api"]

    options  = []
    options_colomns = []
    options_api_key_values = []  # Здесь будем хранить значения api_key
    options_secret_key_values = []  # Здесь будем хранить значения secret_key

    for key, value in keys_api.items():
        if "api_key" in value:
            api_keys = ft.DataCell(ft.Text(value["api_key"], no_wrap=False, width=70, selectable=True))
            options_api_key_values.append(api_keys)
        if "secret_key" in value:
            secret_key = ft.DataCell(ft.Text(value["secret_key"], no_wrap=False, width=70, selectable=True))
            options_secret_key_values.append(secret_key)

    for key in keys:
        option = ft.dropdown.Option(key)  # Создаем объект Option для текущего ключа
        options.append(option)
        options_colomn = ft.DataColumn(
                                label=Text(key),
                                visible=True,                                
                            )
        options_colomns.append(options_colomn)
    

    dropdown =  ft.Dropdown(
        width=250,
        label='Выберите биржу',
        options=options,  # Передаем список объектов Option
        )
    
    text_apikey = ft.TextField(label='Введите Api Key', password=True, can_reveal_password=True)
    text_secretkey = ft.TextField(label='Введите Secret Key', password=True, can_reveal_password=True)
    error_apikey = ft.Text(color='red')

    def button_clicked(e):
        if (text_apikey.value == '' and text_secretkey.value == '') or dropdown.value == None:
            error_apikey.color = 'red'
            error_apikey.value = "Нельзя вводить пустое значение" 
            error_apikey.update()
            time.sleep(5)
            error_apikey.value = ''
            error_apikey.update()

        elif len(text_apikey.value) > 500 and len(text_secretkey.value) > 500:
            error_apikey.color = 'red'
            error_apikey.value = "Нельзя вводить больше 500 символов" 
            error_apikey.update()
            time.sleep(5)
            error_apikey.value = ''
            error_apikey.update()

        else:
            data["keys_api"][dropdown.value]['api_key'] = text_apikey.value
            with open('config\settings_secret.json', 'w') as file:
                json.dump(data, file, indent=4)
            page.update()
            data["keys_api"][dropdown.value]['secret_key'] = text_secretkey.value
            with open('config\settings_secret.json', 'w') as file:
                json.dump(data, file, indent=4)
            page.update()

            error_apikey.color = 'green'
            error_apikey.value = 'Успешно добавлено'
            error_apikey.update()
            time.sleep(5)
            error_apikey.value = ''
            error_apikey.update()

    # Кнопка для выпадающей биржи
    submit = ft.ElevatedButton(text="Добавить", icon=ft.icons.SAVE, on_click=button_clicked)

    language_selects = ft.Dropdown(
            width = 280,
            label = 'Выберите язык приложения',
            options = [ft.dropdown.Option("Russian"),
                       ft.dropdown.Option("English"),
                       ft.dropdown.Option("Greek")
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
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                data['system_language'] = language_selects.value
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                page.update()
                error_language.color = 'green'
                error_language.value = 'Успешно обновлено'
                error_language.update()
                time.sleep(5)
                error_language.value = ''
                error_language.update()

    language_submit = ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=language_select)

    error_delete_exc = ft.Text(color='red')
    def delete_exc(e):
        if dropdown.value == None:
            error_delete_exc.color = 'red'
            error_delete_exc.value = "Нельзя очистить пустое значение" 
            error_delete_exc.update()
            time.sleep(5)
            error_delete_exc.value = ''
            error_delete_exc.update()
        else:
            data["keys_api"][dropdown.value]['api_key'] = None
            with open('config\settings_secret.json', 'w') as file:
                json.dump(data, file, indent=4)
            data["keys_api"][dropdown.value]['secret_key'] = None
            with open('config\settings_secret.json', 'w') as file:
                json.dump(data, file, indent=4)
            page.update()
            error_delete_exc.color = 'green'
            error_delete_exc.value = 'Успешно очищено'
            error_delete_exc.update()
            time.sleep(5)
            error_delete_exc.value = ''
            error_delete_exc.update()

    # Кнопка для выпадающей биржи
    submit_delete = ft.ElevatedButton(text="Очистить", icon=ft.icons.CLEAR, on_click=delete_exc)

    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("My Settings", size=30), 
                ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                ],
            ),

            ft.Row(
                [
                    ft.TextButton("Exit Application", icon=ft.icons.CLOSE, on_click=exit_app, icon_color="red")
                ]
            ),

            ft.Row(
                [
                    ft.TextButton("Check for updates", icon=ft.icons.UPDATE, on_click=exit_app, icon_color="green")
                ]
            ),

            ft.Row(
                [
                    ft.TextButton("Resize the screen", icon=ft.icons.DISPLAY_SETTINGS_OUTLINED, on_click=resize_screen, icon_color="yellow")
                ]
            ),
            
            ft.Row(
                [
                    language_selects,
                    error_language,
                    language_submit
                ]
            ),

            ft.Row(
            [
                ft.Text("Мои API ключи", size=30), 
                ft.IconButton(icon=ft.icons.KEY, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            # Добавление API ключей в json файл
            ft.Row(
                [
                    dropdown,
                    text_apikey,
                    text_secretkey,
                    error_apikey,
                    submit,
                ]
            ),

            # Удаление API ключей из json файла
            ft.Row(
                [
                    dropdown,
                    error_delete_exc,
                    submit_delete,
                ]
            ),

            # таблица
            ft.Row(
                [
                    ft.DataTable(
                        columns=options_colomns
                        ,

                        rows=[
                                ft.DataRow(
                                    cells=options_api_key_values,
                                ),
                                ft.DataRow(
                                    cells=options_secret_key_values,
                                ),
                                
                        ],
                    )
                ]
            ),

        ],
        scroll='HIDDEN',
    )
    
    
    return content