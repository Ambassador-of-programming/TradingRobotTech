from tradingview_ta import TA_Handler, Interval
from binance.client import Client
import flet as ft
import json
import asyncio

async def select_ma_all_strategy(page):
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
            self.exchange = ft.Dropdown(
                width = 280,
                label = 'Выберите Exchange',
                options = [ft.dropdown.Option("Binance"),
                          ],
                )
            self.symbol = ft.TextField(label='Введите Symbol', hint_text='пример: BTCUSDT', width = 280,)
            self.amount = ft.TextField(label='Введите сумму', hint_text='сумма в долларах: 50', width = 280,)
            self.trade_types = ft.Dropdown(
                width = 280,
                label = 'Типы торгов',
                options = [ft.dropdown.Option("Спот")],
            )
            
        async def ma_all_go(self, event):
            if all([self.ma_all_select.value, self.symbol.value,self.exchange.value,
                    self.amount.value, self.interval.value, self.trade_types.value]):
                
                with open('config\settings_secret.json', 'r') as file:
                    data = json.load(file)
                    keys_api = data["keys_api"]
                client = Client(keys_api['binance']['api_key'], keys_api['binance']['secret_key'], {"verify": True, "timeout": None})
                
                if self.ma_all_select.value == "RECOMMENDATION":
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
                            rec = ta_handler.get_analysis().moving_averages[self.ma_all_select.value]
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
                            rec = ta_handler.get_analysis().moving_averages['COMPUTE'][self.ma_all_select.value]
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
                self.error_ma_osc.color = 'red'
                self.error_ma_osc.value = "Нельзя выбрать пустое значение" 
                await self.error_ma_osc.update_async()
                await asyncio.sleep(5)
                self.error_ma_osc.value = ''
                await self.error_ma_osc.update_async()
        
        async def screener(self, event):
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
                    await self.error_ma_osc.update_async()
                    await asyncio.sleep(5)
                    self.error_ma_osc.value = ''
                    await self.error_ma_osc.update_async()
                else:
                    tesla = TA_Handler(
                        symbol=self.symbol.value,
                        screener="crypto",
                        exchange=self.exchange.value,
                        interval=getattr(Interval, self.interval.value)
                    ).get_analysis().moving_averages['COMPUTE'][self.ma_all_select.value]
                    self.error_ma_osc.color = 'green'
                    self.error_ma_osc.value = tesla
                    await self.error_ma_osc.update_async()
                    await asyncio.sleep(5)
                    self.error_ma_osc.value = ''
                    await self.error_ma_osc.update_async()
            else:
                self.error_ma_osc.color = 'red'
                self.error_ma_osc.value = "Нельзя выбрать пустое значение" 
                await self.error_ma_osc.update_async()
                await asyncio.sleep(5)
                self.error_ma_osc.value = ''
                await self.error_ma_osc.update_async()
            
        async def ma_all_submit(self):
            return ft.ElevatedButton(text="Старт",icon=ft.icons.LANGUAGE, on_click=self.ma_all_go)
        
        async def screener_submit(self):
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
            ft.Row([await select_ma.ma_all_submit()], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([await select_ma.screener_submit()], alignment=ft.MainAxisAlignment.CENTER),
        ], 
        auto_scroll=True,
    )
    return content