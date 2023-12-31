import flet as ft
import json

from current_version import current_version

def main(page: ft.Page):
    
    page.title = f'TradingRobotTech {current_version}'
    page.theme_mode = "dark"
    # page.window_full_screen = True

    with open('config\settings_secret.json', 'r') as file:
        data = json.load(file)
        language_system = data['system_language']

    if language_system == 'Russian':
        from language_system.ru.navigation.FletRouter import Router
        from language_system.ru.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

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

    else:
        from language_system.ru.navigation.FletRouter import Router
        from language_system.ru.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

ft.app(target=main, assets_dir="assets")