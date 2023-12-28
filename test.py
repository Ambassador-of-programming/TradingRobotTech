# from pprint import pprint
from tradingview_ta import TA_Handler, Interval

x = 'INTERVAL_1_MINUTE'
# while True:
tesla = TA_Handler(
    symbol="JSTUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=getattr(Interval, x)
).get_analysis().oscillators
print(tesla)
# import json
# with open('config\settings_secret.json', 'r') as file:
#                 data = json.load(file)
#                 keys_api = data["keys_api"]


# print(keys_api['binance'])


# # Пример индексации данных
# documents = {
#     1: "Это пример текста для индексации",
#     2: "Пример другого текста",
#     3: "другие докуметы",
#     # ... другие документы
# }

# # Создание индекса
# index = {}
# for doc_id, text in documents.items():
#     words = text.split()
#     for word in words:
#         if word not in index:
#             index[word] = []
#         index[word].append(doc_id)

# # Функция поиска
# def search(query, index):
#     query_words = query.split()
#     result = set()
#     for word in query_words:
#         if word in index:
#             result.update(index[word])
#     return list(result)

# # Пример использования
# query = "пример текста"
# result_ids = search(query, index)
# print("Результаты поиска:", [documents[id] for id in result_ids])

