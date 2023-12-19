# from pprint import pprint
# from tradingview_ta import TA_Handler, Interval

# x = 'INTERVAL_1_MINUTE'
# # while True:
# tesla = TA_Handler(
#     symbol="JSTUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=getattr(Interval, x)
# ).get_analysis().moving_averages
# print(tesla)
import json
with open('config\settings_secret.json', 'r') as file:
                data = json.load(file)
                keys_api = data["keys_api"]


print(keys_api['binance'])