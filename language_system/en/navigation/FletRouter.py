import flet as ft
# views
from language_system.en.settings.settings import SettingsView
from language_system.en.parsing_news.news import Parsing_News
from language_system.en.backtestings.backtesting import Backtesting
from language_system.en.parsing_airdrops.airdrops import Parsing_Airdrops
from language_system.en.statisc.stat import Statistic
from language_system.en.trading_strategy.strategy import Trading_Strategy
from language_system.en.index.index import IndexView
from language_system.en.crypto_arbitrage.arbitrage import Crypto_Arbitrage
from language_system.en.support.support import Support

class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/trading_strategy": Trading_Strategy(page),
            "/crypto_arbitrage": Crypto_Arbitrage(page),
            "/parsing_news": Parsing_News(page),
            "/parsing_airdrops": Parsing_Airdrops(page),
            "/backtestings": Backtesting(page),
            "/statistics": Statistic(page),
            "/support": Support(page),
            "/settings": SettingsView(page),

        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()