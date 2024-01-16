import flet as ft

class Router:
    
    def __init__(self, trading_strategy, select_ma_osc, 
                 select_ma_all_strategy, select_osc_all_strategy,
                 ai_trading, crypto_arbitrage, backtestings,
                 statistics, support, settings, settings_update):
        self.routes = {
            "/trading_strategy": trading_strategy,
            "/trading_strategy/select_ma_osc": select_ma_osc,
            "/trading_strategy/select_ma_osc/moving_averages/select_ma_all_strategy": select_ma_all_strategy,
            "/trading_strategy/select_ma_osc/oscillators/select_osc_all_strategy": select_osc_all_strategy,

            "/ai_trading": ai_trading,
            "/crypto_arbitrage": crypto_arbitrage,
            "/backtestings": backtestings,
            "/statistics": statistics,
            "/support": support,
            "/settings": settings,
            "/settings/update": settings_update,

        }
        self.body = ft.Container(content=self.routes['/trading_strategy'])

    async def route_change(self, route):
        self.body.content = self.routes[route.route]
        await self.body.update_async()