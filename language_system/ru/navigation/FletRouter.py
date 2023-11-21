import flet as ft
# views
from language_system.ru.settings.settings import SettingsView
from language_system.ru.parsing_news.news import Parsing_News
from language_system.ru.backtestings.backtesting import Backtesting
from language_system.ru.ai_trading.ai_trading import Ai_Trading
from language_system.ru.statisc.stat import Statistic
from language_system.ru.trading_strategy.strategy import Trading_Strategy
from language_system.ru.index.index import IndexView
from language_system.ru.crypto_arbitrage.arbitrage import Crypto_Arbitrage
from language_system.ru.support.support import Support
from language_system.ru.settings.update import Update_app
from language_system.ru.notes.notes import Notes

class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": Trading_Strategy(page),
            "/trading_strategy": Trading_Strategy(page),
            "/ai_trading": Ai_Trading(page),
            "/crypto_arbitrage": Crypto_Arbitrage(page),
            "/parsing_news": Parsing_News(page),
            "/backtestings": Backtesting(page),
            "/statistics": Statistic(page),
            "/notes": Notes(page),
            "/support": Support(page),
            "/settings": SettingsView(page),
            "/settings/update": Update_app(page),

        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()