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
    
    # Добавление API ключей в json файл
    class add_api_keys:
        dropdown = ft.Dropdown(
        width=250,
        label='Выберите биржу',
        options=options,  # Передаем список объектов Option
        )
        text_apikey = ft.TextField(label='Введите Api Key', password=True, can_reveal_password=True)
        text_secretkey = ft.TextField(label='Введите Secret Key', password=True, can_reveal_password=True)
        error_apikey = ft.Text(color='red')

        def button_clicked(e):
            if (add_api_keys.text_apikey.value == '' and add_api_keys.text_secretkey.value == '') or add_api_keys.dropdown.value == None:
                add_api_keys.error_apikey.color = 'red'
                add_api_keys.error_apikey.value = "Нельзя добавить пустое значение" 
                add_api_keys.error_apikey.update()
                time.sleep(5)
                add_api_keys.error_apikey.value = ''
                add_api_keys.error_apikey.update()

            elif len(add_api_keys.text_apikey.value) > 500 and len(add_api_keys.text_secretkey.value) > 500:
                add_api_keys.error_apikey.color = 'red'
                add_api_keys.error_apikey.value = "Нельзя добавлять больше 500 символов" 
                add_api_keys.error_apikey.update()
                time.sleep(5)
                add_api_keys.error_apikey.value = ''
                add_api_keys.error_apikey.update()

            else:
                data["keys_api"][add_api_keys.dropdown.value]['api_key'] = add_api_keys.text_apikey.value
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                page.update()
                data["keys_api"][add_api_keys.dropdown.value]['secret_key'] = add_api_keys.text_secretkey.value
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                page.update()

                add_api_keys.error_apikey.color = 'green'
                add_api_keys.error_apikey.value = 'Успешно добавлено'
                add_api_keys.error_apikey.update()
                time.sleep(5)
                add_api_keys.error_apikey.value = ''
                add_api_keys.error_apikey.update()

        def submit():
            return ft.ElevatedButton(text="Добавить", icon=ft.icons.SAVE, on_click=add_api_keys.button_clicked)

    # выбор языка приложения
    class language_selection:
        language_selects = ft.Dropdown(
                width = 280,
                label = 'Выберите язык приложения',
                options = [ft.dropdown.Option("Russian"),
                           ft.dropdown.Option("English"),
                           ft.dropdown.Option("Greek"),
                           ft.dropdown.Option("Kyrgyz"),

                           ]
            )
        
        error_language = ft.Text(color='red')

        def language_select(e):
                if language_selection.language_selects.value == None:
                    language_selection.error_language.color = 'red'
                    language_selection.error_language.value = "Нельзя выбрать пустое значение" 
                    language_selection.error_language.update()
                    time.sleep(5)
                    language_selection.error_language.value = ''
                    language_selection.error_language.update()

                else:
                    with open('config\settings_secret.json', 'r') as file:
                        data = json.load(file)
                    data['system_language'] = language_selection.language_selects.value
                    with open('config\settings_secret.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    # page.update()
                    language_selection.error_language.color = 'green'
                    language_selection.error_language.value = 'Успешно обновлено'
                    language_selection.error_language.update()
                    time.sleep(5)
                    language_selection.error_language.value = ''
                    language_selection.error_language.update()

        def language_submit():
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=language_selection.language_select)
    
    # Удаление данных api 
    class delete_birja(add_api_keys):
        error_delete_ex = ft.Text(color='red')
        
        def delete_exc(e):
            if delete_birja.dropdown.value == None:
                delete_birja.error_delete_ex.color = 'red'
                delete_birja.error_delete_ex.value = "Нельзя очистить пустое значение" 
                delete_birja.error_delete_ex.update()
                time.sleep(5)
                delete_birja.error_delete_ex.value = ''
                delete_birja.error_delete_ex.update()
            else:
                data["keys_api"][delete_birja.dropdown.value]['api_key'] = None
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                data["keys_api"][delete_birja.dropdown.value]['secret_key'] = None
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                # page.update()
                delete_birja.error_delete_ex.color = 'green'
                delete_birja.error_delete_ex.value = 'Успешно очищено'
                delete_birja.error_delete_ex.update()
                time.sleep(5)
                delete_birja.error_delete_ex.value = ''
                delete_birja.error_delete_ex.update()

        # Кнопка для выпадающей биржи
        def submit_delete():
            return ft.ElevatedButton(text="Очистить", icon=ft.icons.CLEAR, on_click=delete_birja.delete_exc)

    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Мои Настройки", size=30), 
                ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                    ft.TextButton("Светлый/темный режим", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                ],
            ),

            ft.Row(
                [
                    ft.TextButton("Выход", icon=ft.icons.CLOSE, on_click=exit_app, icon_color="red")
                ]
            ),

            ft.Row(
                [
                    ft.TextButton("Проверить обновления", icon=ft.icons.UPDATE, on_click=lambda _: page.go('/settings/update'), icon_color="green")
                ]
            ),

            ft.Row(
                [
                    ft.TextButton("Изменение размера экрана", icon=ft.icons.DISPLAY_SETTINGS_OUTLINED, on_click=resize_screen, icon_color="yellow")
                ]
            ),
            
            ft.Row(
                [
                    language_selection.language_selects,
                    language_selection.error_language,
                    language_selection.language_submit(),
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
                    add_api_keys.dropdown,
                    add_api_keys.text_apikey,
                    add_api_keys.text_secretkey,
                    add_api_keys.error_apikey,
                    add_api_keys.submit(),
                ]
            ),

            # Удаление API ключей из json файла
            ft.Row(
                [
                    delete_birja.dropdown,
                    # error_delete_exc,
                    # submit_delete,
                    delete_birja.error_delete_ex,
                    delete_birja.submit_delete()
                    
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