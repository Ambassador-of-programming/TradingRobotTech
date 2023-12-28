from tradingview_ta import TA_Handler, Interval
import flet as ft
from binance.client import Client
import json

import time

def Select_osc_all_strategy(page):
    class Select_osc:
        def __init__(self) -> None:
            self.error_osc = ft.Text(color='red')
            self.osc_all_select = ft.Dropdown(
                width = 280,
                label = 'Выберите стратегию',
                options = [ft.dropdown.Option("RECOMMENDATION"),
                            ft.dropdown.Option("RSI"),
                           ft.dropdown.Option("STOCH.K"),
                           ft.dropdown.Option("CCI"),
                           ft.dropdown.Option("ADX"),
                           ft.dropdown.Option("AO"),
                           ft.dropdown.Option("Mom"),
                           ft.dropdown.Option("MACD"),
                           ft.dropdown.Option("Stoch.RSI"),
                           ft.dropdown.Option("W%R"),
                           ft.dropdown.Option("BBP"),
                           ft.dropdown.Option("UO"),
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
            
        def osc_all_go(self, event):
            if all([self.osc_all_select.value, self.symbol.value, 
                    self.exchange.value, self.amount.value, 
                    self.interval.value, self.trade_types.value]):
                
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                    keys_api = data["keys_api"]
                client = Client(keys_api['binance']['api_key'], keys_api['binance']['secret_key'], {"verify": True, "timeout": None})
                
                if self.osc_all_select.value == "RECOMMENDATION":
                    print(self.osc_all_select.value)

                    last_order = {
                        self.symbol.value: 'sell',
                        'amount': None,
                        'transactTime': None,
                        'cummulativeQuoteQty': None,
                        }
                    
                    while True:
                        ta_handler = TA_Handler(
                            symbol=self.symbol.value,
                            exchange=self.exchange.value,
                            screener="CRYPTO",
                            interval=getattr(Interval, self.interval.value),   # Здесь ставится интервал времени трейдинга
                        )

                        try:
                            rec = ta_handler.get_analysis().oscillators[self.osc_all_select.value]
                        except:
                            continue

                        # закрываем сделку
                        if last_order[self.symbol.value] == "buy" and ("SELL" in rec):
                            try:
                                sell_order = client.order_market_sell(
                                    symbol=self.symbol.value,
                                    quantity=last_order['amount'])
                                # print(sell_order)
                            except:
                                last_order['amount'] = int(last_order['amount'])
                                continue
                        
                        # открываем сделку
                        if last_order[self.symbol.value] == "sell" and ("BUY" in rec):
                            buy_order = client.order_market_buy(
                                symbol=self.symbol.value,
                                quoteOrderQty=self.amount.value)
                            last_order['cummulativeQuoteQty'] = buy_order['cummulativeQuoteQty']
                            last_order['orderId'] = buy_order['orderId']
                            last_order['origQty'] = buy_order['origQty']
                            last_order['commission'] = buy_order['fills'][0]['commission']
                            last_order['price'] = buy_order['fills'][0]['price']
                            if last_order['commission'] > 0:
                                proverka = last_order['origQty'] - last_order['commission'] - last_order['commission'] # здесь количество монет 2 раза отнимает от суммы коммисии
                                last_order['origQty'] = proverka
                                step_size = float(client.get_symbol_info(self.symbol.value)['filters'][2]['stepSize'])
                                a = step_size  # общая длина шага (к примеру 45.444)
                                c = str(a) # конвертируем шаг в стринг
                                c.split('.') # разбиваем строку шаг по . и получаем список ['0', '005']
                                dot_position = len(c.split('.')[1]) # получаем длину второго элемента списка шага '005'
                                last_order['stepSize'] = dot_position # сохраняем длину шага в dict в значениях (индекс 5)
                                n = dot_position
                                a = last_order['origQty']
                                last_order['origQty'] = int(a*10**n)/10**n
                                if dot_position == 0:
                                    last_order['origQty'] = int(last_order['origQty'])
                
                else:
                    print(self.osc_all_select.value)
                    last_order = {
                        self.symbol.value: 'sell',
                        'transactTime': None,
                        'cummulativeQuoteQty': None,
                        'price': None,
                        'commission': None,
                        'origQty': None,
                        'orderId': None,
                        'stepSize': None,

                        }
                    while True:                        
                        ta_handler = TA_Handler(
                            symbol=self.symbol.value,
                            exchange=self.exchange.value,
                            screener="CRYPTO",
                            interval=getattr(Interval, self.interval.value),   # Здесь ставится интервал времени трейдинга
                        )
                        try:
                            rec = ta_handler.get_analysis().oscillators['COMPUTE'][self.osc_all_select.value]
                        except:
                            continue
                        
                        # закрываем сделку
                        if last_order[self.symbol.value] == "buy" and ("SELL" in rec):
                            try:
                                sell_order = client.order_market_sell(
                                    symbol=self.symbol.value,
                                    quantity=last_order['origQty'])
                                # print(sell_order)
                            except:
                                last_order['origQty'] = int(last_order['origQty'])
                                continue
                            last_order["transactTime"] = sell_order['transactTime']
                            last_order['cummulativeQuoteQty'] = sell_order['cummulativeQuoteQty']
                            last_order['price'] = sell_order['fills'][0]['price']
                            last_order = "sell"

                        # открываем сделку
                        if last_order[self.symbol.value] == "sell" and ("BUY" in rec):
                            buy_order = client.order_market_buy(
                                symbol='BTCUSDT',
                                quoteOrderQty=self.amount.value)
                            last_order['cummulativeQuoteQty'] = buy_order['cummulativeQuoteQty']
                            last_order['orderId'] = buy_order['orderId']
                            last_order['origQty'] = buy_order['origQty']
                            last_order['commission'] = buy_order['fills'][0]['commission']
                            last_order['price'] = buy_order['fills'][0]['price']
                            if last_order['commission'] > 0:
                                proverka = last_order['origQty'] - last_order['commission'] - last_order['commission'] # здесь количество монет 2 раза отнимает от суммы коммисии
                                last_order['origQty'] = proverka
                                step_size = float(client.get_symbol_info(self.symbol.value)['filters'][2]['stepSize'])
                                a = step_size  # общая длина шага (к примеру 45.444)
                                c = str(a) # конвертируем шаг в стринг
                                c.split('.') # разбиваем строку шаг по . и получаем список ['0', '005']
                                dot_position = len(c.split('.')[1]) # получаем длину второго элемента списка шага '005'
                                last_order['stepSize'] = dot_position # сохраняем длину шага в dict в значениях (индекс 5)
                                n = dot_position
                                a = last_order['origQty']
                                last_order['origQty'] = int(a*10**n)/10**n
                                if dot_position == 0:
                                    last_order['origQty'] = int(last_order['origQty'])   
            else:
                self.error_osc.color = 'red'
                self.error_osc.value = "Нельзя выбрать пустое значение" 
                self.error_osc.update()
                time.sleep(5)
                self.error_osc.value = ''
                self.error_osc.update()
        
        def screener(self, event):
            if all([self.symbol.value, self.exchange.value, self.interval.value, self.osc_all_select.value]):
                if self.osc_all_select.value == 'RECOMMENDATION':
                    recommendation  = TA_Handler(
                        symbol=self.symbol.value,
                        screener="crypto",
                        exchange=self.exchange.value,
                        interval=getattr(Interval, self.interval.value)
                    ).get_analysis().oscillators['RECOMMENDATION']
                    self.error_osc.color = 'green'
                    self.error_osc.value = recommendation 
                    self.error_osc.update()
                    time.sleep(5)
                    self.error_osc.value = ''
                    self.error_osc.update()

                else:
                    all_  = TA_Handler(
                        symbol=self.symbol.value,
                        screener="crypto",
                        exchange=self.exchange.value,
                        interval=getattr(Interval, self.interval.value)
                    ).get_analysis().oscillators['COMPUTE'][self.osc_all_select.value]
                    self.error_osc.color = 'green'
                    self.error_osc.value = all_
                    self.error_osc.update()
                    time.sleep(5)
                    self.error_osc.value = ''
                    self.error_osc.update()
                    

        def osc_all_submit(self):
            return ft.ElevatedButton(text="Старт",icon=ft.icons.LANGUAGE, on_click=self.osc_all_go)
        
        def screener_submit(self):
            return ft.ElevatedButton(text="Скринер",icon=ft.icons.SAFETY_CHECK_OUTLINED, on_click=self.screener)

    select_osc = Select_osc()
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Выберите нужную стратегию", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ALT, icon_size=30),
            ], alignment=ft.MainAxisAlignment.CENTER),

            ft.Row([select_osc.osc_all_select], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.symbol], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.interval], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.trade_types], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.exchange], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.amount], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.error_osc], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.osc_all_submit()], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([select_osc.screener_submit()], alignment=ft.MainAxisAlignment.CENTER),
        ], 
        auto_scroll=True,
    )
    return content