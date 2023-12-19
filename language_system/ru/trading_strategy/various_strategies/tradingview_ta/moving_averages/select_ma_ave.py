from tradingview_ta import TA_Handler, Interval
from binance.client import Client
import flet as ft
import json
import time

def Select_ma_all_strategy(page):
    class Select_ma:
        def __init__(self) -> None:
            self.error_ma_osc = ft.Text(color='red')
            self.ma_all_select = ft.Dropdown(
                width = 280,
                label = 'Выберите стратегию',
                options = [ft.dropdown.Option("RECOMMENDATION"),
                            ft.dropdown.Option("EMA10"),
                           ft.dropdown.Option("EMA20"),
                           ft.dropdown.Option("EMA30"),
                           ft.dropdown.Option("EMA50"),
                           ft.dropdown.Option("EMA100"),
                           ft.dropdown.Option("EMA200"),
                           ft.dropdown.Option("HullMA"),
                           ft.dropdown.Option("Ichimoku"),
                           ft.dropdown.Option("SMA10"),
                           ft.dropdown.Option("SMA20"),
                           ft.dropdown.Option("SMA30"),
                           ft.dropdown.Option("SMA50"),
                           ft.dropdown.Option("SMA100"),
                           ft.dropdown.Option("SMA200"),
                           ft.dropdown.Option("VWMA"),
                           ]
                )
            self.symbol = ft.TextField(label='Введите Symbol', hint_text='пример: BTCUSDT', width = 280,)
            self.exchange = ft.TextField(label='Введите Exchange', hint_text='пример: BINANCE', width = 280,)
            self.amount = ft.TextField(label='Введите сумму', hint_text='сумма в долларах: 50', width = 280,)
            self.interval = ft.Dropdown(
                width = 280,
                label = 'Выберите интервал',
                options = [ft.dropdown.Option("INTERVAL_1_MINUTE"),
                           ft.dropdown.Option("INTERVAL_5_MINUTES"),
                           ft.dropdown.Option("INTERVAL_15_MINUTES"),
                           ft.dropdown.Option("INTERVAL_30_MINUTES"),
                           ft.dropdown.Option("INTERVAL_1_HOUR"),
                           ft.dropdown.Option("INTERVAL_2_HOURS"),
                           ft.dropdown.Option("INTERVAL_4_HOURS"),
                           ft.dropdown.Option("INTERVAL_1_DAY"),
                           ft.dropdown.Option("INTERVAL_1_WEEK"),
                           ft.dropdown.Option("INTERVAL_1_MONTH"),
                           ],
                )
            self.trade_types = ft.Dropdown(
                width = 280,
                label = 'Типы торгов',
                options = [ft.dropdown.Option("Спот")],
            )
            
        def ma_all_go(self, event):
            if all([self.ma_all_select.value, self.symbol.value,self.exchange.value,
                    self.amount.value, self.interval.value, self.trade_types.value]):
                if self.ma_all_select.value == "EMA10":
                    with open('config\settings_secret.json', 'r') as file:
                        data = json.load(file)
                        keys_api = data["keys_api"]
                        client = Client(keys_api['binance']['api_key'], keys_api['binance']['secret_key'], {"verify": True, "timeout": None})
                        
                        balance = float(client.get_asset_balance(asset='USDT')['free'])
                        print(f'Ваш баланс на USDT: {balance}')

                elif self.ma_all_select.value == "EMA20":
                    pass
                elif self.ma_all_select.value == "EMA30":
                    pass
                elif self.ma_all_select.value == "EMA50":
                    pass
                elif self.ma_all_select.value == "EMA100":
                    pass
                elif self.ma_all_select.value == "EMA200":
                    pass
                elif self.ma_all_select.value == "HullMA":
                    pass
                elif self.ma_all_select.value == "Ichimoku":
                    pass
                elif self.ma_all_select.value == "SMA10":
                    pass
                elif self.ma_all_select.value == "SMA20":
                    pass
                elif self.ma_all_select.value == "SMA30":
                    pass
                elif self.ma_all_select.value == "SMA50":
                    pass
                elif self.ma_all_select.value == "SMA100":
                    pass
                elif self.ma_all_select.value == "SMA200":
                    pass
                elif self.ma_all_select.value == "VWMA":
                    pass
            else:
                self.error_ma_osc.color = 'red'
                self.error_ma_osc.value = "Нельзя выбрать пустое значение" 
                self.error_ma_osc.update()
                time.sleep(5)
                self.error_ma_osc.value = ''
                self.error_ma_osc.update()
        
        def screener(self, event):
            if all([self.symbol.value, self.exchange.value, self.interval.value, self.ma_all_select.value]):
                if self.ma_all_select.value == 'RECOMMENDATION':
                    tesla = TA_Handler(
                        symbol=self.symbol.value,
                        screener="crypto",
                        exchange=self.exchange.value,
                        interval=getattr(Interval, self.interval.value)
                    ).get_analysis().moving_averages['RECOMMENDATION']
                    self.error_ma_osc.color = 'green'
                    self.error_ma_osc.value = tesla
                    self.error_ma_osc.update()
                    time.sleep(5)
                    self.error_ma_osc.value = ''
                    self.error_ma_osc.update()
                else:
                    tesla = TA_Handler(
                        symbol=self.symbol.value,
                        screener="crypto",
                        exchange=self.exchange.value,
                        interval=getattr(Interval, self.interval.value)
                    ).get_analysis().moving_averages['COMPUTE'][self.ma_all_select.value]
                    self.error_ma_osc.color = 'green'
                    self.error_ma_osc.value = tesla
                    self.error_ma_osc.update()
                    time.sleep(5)
                    self.error_ma_osc.value = ''
                    self.error_ma_osc.update()
            
        def ma_all_submit(self):
            return ft.ElevatedButton(text="Выбрать",icon=ft.icons.LANGUAGE, on_click=self.ma_all_go)
        
        def screener_submit(self):
            return ft.ElevatedButton(text="Скринер",icon=ft.icons.SAFETY_CHECK_OUTLINED, on_click=self.screener)

    select_ma = Select_ma()
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Выберите нужную стратегию", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ALT, icon_size=30),
            ], alignment=ft.MainAxisAlignment.CENTER),

            ft.Row([select_ma.ma_all_select], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.symbol], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.interval], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.trade_types], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.exchange], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.amount], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.error_ma_osc], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.ma_all_submit()], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_ma.screener_submit()], alignment=ft.MainAxisAlignment.CENTER),
        ], 
        auto_scroll=True,
    )
    return content