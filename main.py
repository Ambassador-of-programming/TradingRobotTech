import flet as ft
import json
import aiofiles
from current_version import current_version

async def main(page: ft.Page):
    
    page.title = f'TradingRobotTech {current_version}'
    page.theme_mode = "dark"
    page.scroll = 'HIDDEN'

    page.bgcolor = None
    # page.padding = 50

    # page.window_full_screen = True

    async with aiofiles.open('config/settings_secret.json', 'r') as file:
        data = json.loads(await file.read())
        language_system = data['system_language']

    # async def save_router_page_json(**kwargs):
    #     # Асинхронное чтение данных из файла JSON
    #     async with aiofiles.open('config/settings_secret.json', mode='r') as file:
    #         data = json.loads(await file.read())

    #     # Обновление данных в page_router
    #     data['page_router'] = list(kwargs.keys())

    #     # Асинхронная запись обновленных данных обратно в файл JSON
    #     async with aiofiles.open('config/settings_secret.json', mode='w') as file:
    #         await file.write(json.dumps(data, indent=4))

    # if language_system == 'Russian':
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
    from language_system.ru.support.careers import careers
    
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
        '/careers': await careers(page),
        '/settings': await settings_view(page),
        '/settings/update': await update_app(page),
    }
    myRouter = Router(**router_page)
    # await save_router_page_json(**router_page)
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
        
ft.app(
    target=main, 
    assets_dir="assets", 
    view=ft.AppView.FLET_APP,
)