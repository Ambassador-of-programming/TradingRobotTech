import flet as ft
import json

from current_version import current_version

def main(page: ft.Page):
    page.title = f'TradingRobotTech {current_version}'
    page.theme_mode = "dark"
    page.window_full_screen = True

    with open('config\settings_secret.json', 'r') as file:
        data = json.load(file)
        language_system = data['system_language']

    if language_system == 'Russian':
        # Russian language
        from language_system.ru.navigation.FletRouter import Router
        from language_system.ru.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

    elif language_system == 'English':
        # English language
        from language_system.en.navigation.FletRouter import Router
        from language_system.en.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

    elif language_system == 'Greek':
        # English language
        from language_system.en.navigation.FletRouter import Router
        from language_system.en.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

    elif language_system == 'Kyrgyz':
        # English language
        from language_system.en.navigation.FletRouter import Router
        from language_system.en.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

    else:
        # Russian language
        from language_system.ru.navigation.FletRouter import Router
        from language_system.ru.navigation.navbar import NavBar

        page.appbar = NavBar(page)
        myRouter = Router(page)

        page.on_route_change = myRouter.route_change

        page.add(
            myRouter.body
        )
        page.go('/')

    # elif language_system == 'gr':
    #     page.appbar = NavBar(page)
    #     myRouter = Router(page)

    #     page.on_route_change = myRouter.route_change

    #     page.add(
    #         myRouter.body
    #     )
    #     page.go('/')

ft.app(target=main, assets_dir="assets")