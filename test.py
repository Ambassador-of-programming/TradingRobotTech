import json

# # Открываем файл secret.json для чтения
# with open('config\secret.json', 'r') as file:
#     data = json.load(file)
#     lang_api = data["system_language"]


# # # # Обновляем значение api_key
# # data["keys_api"]["binance"]['api_key'] = 'dsdfura'

# # # # Записываем изменения обратно в файл
# # with open('config\secret.json', 'w') as file:
# #     json.dump(data, file, indent=4)

# # # # Выводим содержимое файла
# # api_key_values = []  # Здесь будем хранить значения api_key
# # secret_key_values = []  # Здесь будем хранить значения secret_key

# # for key, value in keys_api.items():
# #     if "api_key" in value:
# #         api_key_values.append(value["api_key"])
# #     if "secret_key" in value:
# #         secret_key_values.append(value["secret_key"])
# print(f'язык системы: {lang_api}')

with open('tests.json', "w") as file:
    file.write("""{"cars":
    [{"Year": "1997", "Make": "Ford", "Model": "E350", "Price": "3200.00"},
    {"Year": "1999", "Make": "Chevy", "Model": "Venture", "Price": "4800.00"},
    {"Year": "1996", "Make": "Jeep", "Model": "Grand Cherokee", "Price":
    "4900.00"}
]}""")