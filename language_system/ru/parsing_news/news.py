import flet as ft
import json
import time

def Parsing_News(page):

    
    class DataTable:
            
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
                
            headers: list = ["Api Key", "secret key", ]

            self.table.columns = [
                title for title in options_colomns
            ]
            # self.table.columns = [
            # ft.DataColumn(label=ft.Text(title), visible=True) for title in headers]

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

            

    class Form():
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
            
        def create_data_row(self, values: list):
            data = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(values[0], no_wrap=False, width=70, selectable=True)),
                ]
            )
            return data
        
        def update_data_table(self, data: ft.DataRow):
            # now, w/ access to the dt table ...
            self.table.rows.append(data)
            self.table.update()

        def save_data(self, event):
            values: list = [self.dropdown.value,self.text_apikey.value.strip(), self.text_secretkey.value.strip()]
            # check all fields first ...
            if all(values):
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                data["keys_api"][self.dropdown.value]['api_key'] = self.text_apikey.value
                with open('config\settings_secret.json', 'w') as file:
                    json.dump(data, file, indent=4)
                data["keys_api"][self.dropdown.value]['secret_key'] = self.text_secretkey.value
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

                # next, update the data table (pass the instance of it)
                # self.update_data_table(data)
                # print(self.table.rows)
                # self.table.rows.pop(0)
                # print(self.table.rows)
                # self.table.update()

    datatable = DataTable()   
    form = Form(datatable.table)
    content = ft.Column(
        
        controls=[
            # Добавление API ключей в json файл
            ft.Row(
                [   
                    form.dropdown,
                    form.text_apikey,
                    form.text_secretkey,
                    form.error_apikey,
                    form.add
                ]
            ),

            # таблица
            ft.Row(
                controls=[
                    datatable.table,
                    
    
                    # ft.DataTable(
                    #     columns=options_colomns
                    #     ,

                    #     rows=[
                    #             ft.DataRow(
                    #                 cells=options_api_key_values,
                    #             ),
                    #             ft.DataRow(
                    #                 cells=options_secret_key_values,
                    #             ),
                                
                        ],
                    )
        ],
        on_scroll=True
    )
    
    return content