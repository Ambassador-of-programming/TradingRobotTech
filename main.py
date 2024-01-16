import flet as ft
import json
import aiofiles
import asyncio
from current_version import current_version

async def main(page: ft.Page):
    
    page.title = f'TradingRobotTech {current_version}'
    page.theme_mode = "dark"
    # page.window_full_screen = True

    async with aiofiles.open('config\settings_secret.json', 'r') as file:
        data = json.loads(await file.read())
        language_system = data['system_language']

    if language_system == 'Russian':
        from language_system.ru.navigation.FletRouter import Router
        from language_system.ru.navigation.appbar import appbar

        from language_system.ru.settings.settings import settings_view
        from language_system.ru.backtestings.backtesting import backtesting
        from language_system.ru.ai_trading.ai_trading import ai_trading
        from language_system.ru.statisc.stat import statistic
        from language_system.ru.trading_strategy.strategy import trading_strategy
        from language_system.ru.index.index import IndexView
        from language_system.ru.crypto_arbitrage.arbitrage import crypto_arbitrage
        from language_system.ru.support.support import support
        from language_system.ru.settings.update import update_app
        from language_system.ru.trading_strategy.various_strategies.tradingview_ta.select_ma_s import select_ta_ma_osc
        from language_system.ru.trading_strategy.various_strategies.tradingview_ta.moving_averages.select_ma_ave import select_ma_all_strategy
        from language_system.ru.trading_strategy.various_strategies.tradingview_ta.oscillators.select_osc import select_osc_all_strategy
        
        page.appbar = await appbar(page)
        router_page = {
            '/trading_strategy': await trading_strategy(page),
            '/trading_strategy/select_ma_osc': await select_ta_ma_osc(page),
            '/trading_strategy/select_ma_osc/moving_averages/select_ma_all_strategy': await select_ma_all_strategy(page),
            '/trading_strategy/select_ma_osc/oscillators/select_osc_all_strategy': await select_osc_all_strategy(page),
            '/ai_trading': await ai_trading(page),
            '/crypto_arbitrage': await crypto_arbitrage(page),
            '/backtestings': await backtesting(page),
            '/statistics': await statistic(page),
            '/support': await support(page), 
            '/settings': await settings_view(page),
            '/settings/update': await update_app(page),
        }

        myRouter = Router(trading_strategy=router_page['/trading_strategy'],
                          select_ma_osc=router_page['/trading_strategy/select_ma_osc'],
                          select_ma_all_strategy=router_page['/trading_strategy/select_ma_osc/moving_averages/select_ma_all_strategy'],
                          select_osc_all_strategy=router_page['/trading_strategy/select_ma_osc/oscillators/select_osc_all_strategy'],
                          ai_trading=router_page['/ai_trading'],
                          crypto_arbitrage=router_page['/crypto_arbitrage'],
                          backtestings=router_page['/backtestings'],
                          statistics=router_page['/statistics'],
                          support=router_page['/support'],
                          settings=router_page['/settings'],
                          settings_update=router_page['/settings/update'])

        page.on_route_change = myRouter.route_change

        await page.add_async(
            myRouter.body
        )
        await page.go_async('/trading_strategy')

    # elif language_system == 'English':
    #     from language_system.en.navigation.FletRouter import Router
    #     from language_system.en.navigation.navbar import NavBar

    #     page.appbar = NavBar(page)
    #     myRouter = Router(page)

    #     page.on_route_change = myRouter.route_change

    #     page.add(
    #         myRouter.body
    #     )
    #     page.go('/')

    # elif language_system == 'Greek':
    #     from language_system.en.navigation.FletRouter import Router
    #     from language_system.en.navigation.navbar import NavBar

    #     page.appbar = NavBar(page)
    #     myRouter = Router(page)

    #     page.on_route_change = myRouter.route_change

    #     page.add(
    #         myRouter.body
    #     )
    #     page.go('/')

    # elif language_system == 'Kyrgyz':
    #     from language_system.en.navigation.FletRouter import Router
    #     from language_system.en.navigation.navbar import NavBar

    #     page.appbar = NavBar(page)
    #     myRouter = Router(page)

    #     page.on_route_change = myRouter.route_change

    #     page.add(
    #         myRouter.body
    #     )
    #     page.go('/')
        
ft.app(target=main, assets_dir="assets")