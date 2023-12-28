import flet as ft
# views
from language_system.ru.settings.settings import SettingsView
from language_system.ru.backtestings.backtesting import Backtesting
from language_system.ru.ai_trading.ai_trading import Ai_Trading
from language_system.ru.statisc.stat import Statistic
from language_system.ru.trading_strategy.strategy import Trading_Strategy
from language_system.ru.index.index import IndexView
from language_system.ru.crypto_arbitrage.arbitrage import Crypto_Arbitrage
from language_system.ru.support.support import Support
from language_system.ru.settings.update import Update_app
from language_system.ru.trading_strategy.various_strategies.tradingview_ta.select_ma_s import Select_ta_ma_osc
from language_system.ru.trading_strategy.various_strategies.tradingview_ta.moving_averages.select_ma_ave import Select_ma_all_strategy
from language_system.ru.trading_strategy.various_strategies.tradingview_ta.oscillators.select_osc import Select_osc_all_strategy


class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": Trading_Strategy(page),
            "/trading_strategy": Trading_Strategy(page),
            "/trading_strategy/select_ma_osc": Select_ta_ma_osc(page),
            "/trading_strategy/select_ma_osc/moving_averages/select_ma_all_strategy": Select_ma_all_strategy(page),
            "/trading_strategy/select_ma_osc/oscillators/select_osc_all_strategy": Select_osc_all_strategy(page),

            "/ai_trading": Ai_Trading(page),
            "/crypto_arbitrage": Crypto_Arbitrage(page),
            "/backtestings": Backtesting(page),
            "/statistics": Statistic(page),
            "/support": Support(page),
            "/settings": SettingsView(page),
            "/settings/update": Update_app(page),

        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()