import flet as ft
import asyncio
import aiofiles
import json

async def settings_view(page: ft.Page):
    async def toggle_dark_mode(event):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            await page.update_async()
        else: 
            page.theme_mode = "dark"
            await page.update_async()

    async def resize_screen(event):
        if page.window_full_screen == False:
            page.window_full_screen = True
            await page.update_async()
        else: 
            page.window_full_screen = False
            await page.update_async()

    async def exit_app(event):
        async def dialog_dismissed(event):
            await page.close_dialog_async()

        async def exit_app(event):
            await page.window_destroy_async()

        cupertino_alert_dialog = ft.CupertinoAlertDialog(
        content=ft.Text("Вы хотите закрыть приложение?"),
        actions=[
            ft.CupertinoDialogAction(
                text = 'Да',
                is_destructive_action=True,
                on_click=exit_app,
                ),

            ft.CupertinoDialogAction(
                text = "Отмена",
                on_click=dialog_dismissed,
                ),
            ],
        )
        page.dialog = cupertino_alert_dialog
        cupertino_alert_dialog.open = True
        await page.update_async()

    async def check_update(event):
        return await page.go_async('/settings/update')
    
    class EditResizeScale:
        def __init__(self) -> None:
            self.scale_textfield = ft.TextField(label="Изменить маштаб", hint_text="Только целое или дробное число (1 или 0.1)")
            self.scale_error = None

        async def resize_scale(self):
            async with aiofiles.open('config/user_settings.json', mode='r') as file:
                data = json.loads(await file.read())
            return data['scale']
    
        async def __scale_update(self, event):
            async def convert_to_float_or_str(value):
                try:
                    result = float(value)
                    return result
                except ValueError:
                    return value
            
            if self.scale_textfield.value is not None and \
                isinstance(await convert_to_float_or_str(self.scale_textfield.value), (int, float)):

                async with aiofiles.open('config/user_settings.json', mode='r') as file:
                    data = json.loads(await file.read())
                data['scale'] = await convert_to_float_or_str(self.scale_textfield.value.strip().replace(" ", ""))
                async with aiofiles.open('config/user_settings.json', mode='w') as file:
                    await file.write(json.dumps(data, indent=4))
                    
                content.scale = await self.resize_scale()
                await page.update_async()
            else:
                print("у вас не int или float")

        async def scale_button(self):
            button = ft.IconButton(
                icon=ft.icons.UPDATE,
                icon_size=20,
                tooltip="Изменить маштаб",
                on_click=self.__scale_update,
            )

            return button
            
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

        async def language_select(self, event):
            if self.language_selects.value == None:
                self.error_language.color = 'red'
                self.error_language.value = "Нельзя выбрать пустое значение" 
                await self.error_language.update_async()
                await asyncio.sleep(5)
                self.error_language.value = ''
                await self.error_language.update_async()
            else:
                async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                    data = json.loads(await file.read())
                data['system_language'] = self.language_selects.value
                async with aiofiles.open('config/settings_secret.json', mode='w') as file:
                    await file.write(json.dumps(data, indent=4))
                # page.update()
                self.error_language.color = 'green'
                self.error_language.value = 'Успешно обновлено'
                await self.error_language.update_async()
                await asyncio.sleep(5)
                self.error_language.value = ''
                await self.error_language.update_async()

        async def language_submit(self):
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=self.language_select)
    
    
    async with aiofiles.open('config/settings_secret.json', mode='r') as file:
        data = json.loads(await file.read())
        keys = data["keys_api"].keys()
        options  = []
        for key in keys:
            option = ft.dropdown.Option(key)  # Создаем объект Option для текущего ключа
            options.append(option)
            
    # def __init__(self, table: ft.DataTable) -> None:
    delete_table = ft.DataTable
    error_delete_ex = ft.Text(color='red')
    delete_dropdown = ft.Dropdown(
            width=250,
            label='Выберите биржу для удаления',
            options=options)
    
    async def delete_exc(event):
        if delete_dropdown.value == None:
            error_delete_ex.color = 'red'
            error_delete_ex.value = "Нельзя очистить пустое значение" 
            await error_delete_ex.update_async()
            await asyncio.sleep(5)
            error_delete_ex.value = ''
            await error_delete_ex.update_async()
        else:
            async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                data = json.loads(await file.read())
            data["keys_api"][delete_dropdown.value]['api_key'] = None
            async with aiofiles.open('config/settings_secret.json', mode='w') as file:
                await file.write(json.dumps(data, indent=4))
            data["keys_api"][delete_dropdown.value]['secret_key'] = None
            async with aiofiles.open('config/settings_secret.json', mode='w') as file:
                await file.write(json.dumps(data, indent=4))

            options_api_key_values = []  # Здесь будем хранить значения api_key
            options_secret_key_values = []  # Здесь будем хранить значения secret_key
            # Список выпадающей биржи
            async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                data = json.loads(await file.read())
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
            delete_table.rows = [text_apikey, text_secretkey]
            await delete_table.update_async()
            
            error_delete_ex.color = 'green'
            error_delete_ex.value = 'Успешно очищено'
            await error_delete_ex.update_async()
            await asyncio.sleep(5)
            error_delete_ex.value = ''
            await error_delete_ex.update_async()

    # Кнопка для выпадающей биржи
    async def submit_delete():
        return ft.ElevatedButton(text="Очистить", icon=ft.icons.CLEAR, on_click=delete_exc)
        
    async with aiofiles.open('config/settings_secret.json', mode='r') as file:
        data = json.loads(await file.read())
        keys = data["keys_api"].keys()
        keys_api = data["keys_api"]
    options_colomns = []
    for key in keys:
        options_colomn = ft.DataColumn(
                                label=ft.Text(key),
                                visible=True,                                
                            )
        options_colomns.append(options_colomn)
    
    async with aiofiles.open('config/settings_secret.json', mode='r') as file:
        data = json.loads(await file.read())
        keys = data["keys_api"].keys()
        keys_api = data["keys_api"]        
    
    table = ft.DataTable()
    table.columns = [title for title in options_colomns]
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
    table.rows=[text_apikey, text_secretkey]
    
    class FormAddKey():
        
        async def options_data():
            async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                data = json.loads(await file.read())
                keys = data["keys_api"].keys()
            options  = []
            for key in keys:
                option = ft.dropdown.Option(key)  # Создаем объект Option для текущего ключа
                options.append(option)
            return options

        def __init__(self, table: ft.DataTable, options) -> None:
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
                options=options)

        async def save_data(self, event):
            values: list = [self.dropdown.value, self.text_apikey.value.strip(), self.text_secretkey.value.strip()]
            # check all fields first ...
            if all(values):
                async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                    data = json.loads(await file.read())

                data["keys_api"][self.dropdown.value]['api_key'] = self.text_apikey.value.strip()
                async with aiofiles.open('config/settings_secret.json', mode='w') as file:
                    await file.write(json.dumps(data, indent=4))
                data["keys_api"][self.dropdown.value]['secret_key'] = self.text_secretkey.value.strip()
                async with aiofiles.open('config/settings_secret.json', mode='w') as file:
                    await file.write(json.dumps(data, indent=4))
                
                options_api_key_values = []  # Здесь будем хранить значения api_key
                options_secret_key_values = []  # Здесь будем хранить значения secret_key

                # Список выпадающей биржи
                async with aiofiles.open('config/settings_secret.json', mode='r') as file:
                    data = json.loads(await file.read())
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

                await self.table.update_async()

                self.error_apikey.color = 'green'
                self.error_apikey.value = 'Успешно добавлено'
                await self.error_apikey.update_async()
                await asyncio.sleep(5)
                self.error_apikey.value = ''
                await self.error_apikey.update_async()

            else:
                self.error_apikey.color = 'red'
                self.error_apikey.value = "Нельзя добавить пустое значение" 
                await self.error_apikey.update_async()
                await asyncio.sleep(5)
                self.error_apikey.value = ''
                await self.error_apikey.update_async()
    
    editresizescale = EditResizeScale()
    language_selection = Language_selection()
    datatable_add_key = table  
    form_add_key = FormAddKey(datatable_add_key, options=await FormAddKey.options_data())
    delete_table = datatable_add_key

    content = ft.Column(
        [
            ft.Row(
            [
                # page.appbar = await appbar(page)
            ], 
            ),

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
                    ft.TextButton("Проверить наличие обновлений", icon=ft.icons.UPDATE, on_click=check_update, icon_color="green")
                ]
            ),

            ft.Row(
                [
                    ft.TextButton("Изменение размера экрана", icon=ft.icons.DISPLAY_SETTINGS_OUTLINED, on_click=resize_screen, icon_color="yellow")
                ]
            ),

            # Изменить маштаб приложения 
            ft.Row(
                [
                    editresizescale.scale_textfield,
                    await editresizescale.scale_button()
                ]
            ),
            
            # Выбор языка приложения из выподающей меню
            ft.Row(
                [
                    language_selection.language_selects,
                    language_selection.error_language,
                    await language_selection.language_submit(),
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
                    delete_dropdown,
                    error_delete_ex,
                    await submit_delete()
                ]
            ),

            # таблица с API ключами
            ft.Row(
                controls=[
                    datatable_add_key,
                ],
            ),
        ],
        scale=await editresizescale.resize_scale()
    )
    
    
    return content