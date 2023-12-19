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
    
    # выбор языка приложения
    class Language_selection:
        def __init__(self) -> None:
            self.error_language = ft.Text(color='red')
            self.language_selects = ft.Dropdown(
                width = 280,
                label = 'Выберите язык приложения',
                options = [ft.dropdown.Option("Russian"),
                           ft.dropdown.Option("English"),
                           ft.dropdown.Option("Greek"),
                           ft.dropdown.Option("Kyrgyz"),
                           ]
            )

        def language_select(self, event):
            if self.language_selects.value == None:
                self.error_language.color = 'red'
                self.error_language.value = "Нельзя выбрать пустое значение" 
                self.error_language.update()
                time.sleep(5)
                self.error_language.value = ''
                self.error_language.update()
            else:
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                data['system_language'] = self.language_selects.value
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                # page.update()
                self.error_language.color = 'green'
                self.error_language.value = 'Успешно обновлено'
                self.error_language.update()
                time.sleep(5)
                self.error_language.value = ''
                self.error_language.update()

        def language_submit(self):
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=self.language_select)
    
    # Удаление данных api 
    class Delete_birja():
        with open('config\settings_secret.json', 'r') as file:
            data = json.load(file)
            keys = data["keys_api"].keys()
        options  = []
        for key in keys:
            option = ft.dropdown.Option(key)  # Создаем объект Option для текущего ключа
            options.append(option)

        def __init__(self, table: ft.DataTable) -> None:
            self.table = table
            self.error_delete_ex = ft.Text(color='red')
            self.dropdown = ft.Dropdown(
                width=250,
                label='Выберите биржу',
                options=self.options)
        
        def delete_exc(self, event):
            if self.dropdown.value == None:
                self.error_delete_ex.color = 'red'
                self.error_delete_ex.value = "Нельзя очистить пустое значение" 
                self.error_delete_ex.update()
                time.sleep(5)
                self.error_delete_ex.value = ''
                self.error_delete_ex.update()

            else:
                self.data["keys_api"][self.dropdown.value]['api_key'] = None
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(self.data, file, indent=4)
                self.data["keys_api"][self.dropdown.value]['secret_key'] = None
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(self.data, file, indent=4)

                options_api_key_values = []  # Здесь будем хранить значения api_key
                options_secret_key_values = []  # Здесь будем хранить значения secret_key

                # Список выпадающей биржи
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                    keys_api = data["keys_api"]

                for key, value in keys_api.items():
                    if "api_key" in value:
                        api_keys = ft.DataCell(ft.Text(value["api_key"], no_wrap=False, width=70, selectable=True))
                        options_api_key_values.append(api_keys)
                    if "secret_key" in value:
                        secret_key = ft.DataCell(ft.Text(value["secret_key"], no_wrap=False, width=70, selectable=True))
                        options_secret_key_values.append(secret_key)

                text_apikey = ft.DataRow(cells=options_api_key_values) 
                text_secretkey = ft.DataRow(cells=options_secret_key_values) 
                self.table.rows=[text_apikey, text_secretkey]

                self.table.update()
                
                self.error_delete_ex.color = 'green'
                self.error_delete_ex.value = 'Успешно очищено'
                self.error_delete_ex.update()
                time.sleep(5)
                self.error_delete_ex.value = ''
                self.error_delete_ex.update()

        # Кнопка для выпадающей биржи
        def submit_delete(self):
            return ft.ElevatedButton(text="Очистить", icon=ft.icons.CLEAR, on_click=self.delete_exc)
        
    class DataTableAddKey:
        def __init__(self) -> None:
            self.table = ft.DataTable()
            # Список выпадающей биржи
            with open('config\settings_secret.json', 'r') as file:
                data = json.load(file)
                keys = data["keys_api"].keys()
                keys_api = data["keys_api"]
            options_colomns = []
            for key in keys:
                options_colomn = ft.DataColumn(
                                        label=ft.Text(key),
                                        visible=True,                                
                                    )
                options_colomns.append(options_colomn)\
                
            self.table.columns = [title for title in options_colomns]
            options_api_key_values = []  # Здесь будем хранить значения api_key
            options_secret_key_values = []  # Здесь будем хранить значения secret_key
            for key, value in keys_api.items():
                if "api_key" in value:
                    api_keys = ft.DataCell(ft.Text(value["api_key"], no_wrap=False, width=70, selectable=True))
                    options_api_key_values.append(api_keys)

                if "secret_key" in value:
                    secret_key = ft.DataCell(ft.Text(value["secret_key"], no_wrap=False, width=70, selectable=True))
                    options_secret_key_values.append(secret_key)

            text_apikey = ft.DataRow(cells=options_api_key_values) 
            text_secretkey = ft.DataRow(cells=options_secret_key_values) 
            self.table.rows=[text_apikey, text_secretkey]

    class FormAddKey():
        with open('config\settings_secret.json', 'r') as file:
            data = json.load(file)
            keys = data["keys_api"].keys()
        options  = []
        for key in keys:
            option = ft.dropdown.Option(key)  # Создаем объект Option для текущего ключа
            options.append(option)

        def __init__(self, table: ft.DataTable) -> None:
            self.table = table
            self.text_apikey = ft.TextField(label='Введите Api Key', password=True, can_reveal_password=True)
            self.text_secretkey = ft.TextField(label='Введите Secret Key', password=True,can_reveal_password=True)
            self.error_apikey = ft.Text(color='red')
            self.add = ft.ElevatedButton(
                text="Добавить", 
                icon=ft.icons.SAVE, 
                on_click=self.save_data)
            
            self.dropdown = ft.Dropdown(
                width=250,
                label='Выберите биржу',
                options=self.options)

        def save_data(self, event):
            values: list = [self.dropdown.value,self.text_apikey.value.strip(), self.text_secretkey.value.strip()]
            # check all fields first ...
            if all(values):
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)

                data["keys_api"][self.dropdown.value]['api_key'] = self.text_apikey.value.strip()
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                data["keys_api"][self.dropdown.value]['secret_key'] = self.text_secretkey.value.strip()
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                
                options_api_key_values = []  # Здесь будем хранить значения api_key
                options_secret_key_values = []  # Здесь будем хранить значения secret_key

                # Список выпадающей биржи
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                    keys_api = data["keys_api"]

                for key, value in keys_api.items():
                    if "api_key" in value:
                        api_keys = ft.DataCell(ft.Text(value["api_key"], no_wrap=False, width=70, selectable=True))
                        options_api_key_values.append(api_keys)
                    if "secret_key" in value:
                        secret_key = ft.DataCell(ft.Text(value["secret_key"], no_wrap=False, width=70, selectable=True))
                        options_secret_key_values.append(secret_key)

                text_apikey = ft.DataRow(cells=options_api_key_values) 
                text_secretkey = ft.DataRow(cells=options_secret_key_values) 
                self.table.rows=[text_apikey, text_secretkey]

                self.table.update()

                self.error_apikey.color = 'green'
                self.error_apikey.value = 'Успешно добавлено'
                self.error_apikey.update()
                time.sleep(5)
                self.error_apikey.value = ''
                self.error_apikey.update()

            else:
                self.error_apikey.color = 'red'
                self.error_apikey.value = "Нельзя добавить пустое значение" 
                self.error_apikey.update()
                time.sleep(5)
                self.error_apikey.value = ''
                self.error_apikey.update()

    language_selection = Language_selection()
    datatable_add_key = DataTableAddKey()   
    form_add_key = FormAddKey(datatable_add_key.table)
    delete_birja = Delete_birja(datatable_add_key.table)

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
                    form_add_key.dropdown,
                    form_add_key.text_apikey,
                    form_add_key.text_secretkey,
                    form_add_key.error_apikey,
                    form_add_key.add,
                ]
            ),


            # Удаление API ключей из json файла
            ft.Row(
                [
                    delete_birja.dropdown,
                    delete_birja.error_delete_ex,
                    delete_birja.submit_delete()
                ]
            ),

            # таблица
            ft.Row(
                controls=[
                    datatable_add_key.table,
                ]
            ),

        ],
        scroll='HIDDEN',
    )
    
    
    return content