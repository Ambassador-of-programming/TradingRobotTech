import flet as ft

def NavBar(page):
    NavBar = ft.AppBar(
            # leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
            leading_width=40,
            # title=ft.Text("Flet Router"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                # ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.TASK_ALT, on_click=lambda _: page.go('/trading_strategy')),
                ft.IconButton(ft.icons.ROCKET, on_click=lambda _: page.go('/ai_trading')),
                ft.IconButton(ft.icons.TASK_ROUNDED, on_click=lambda _: page.go('/crypto_arbitrage')),
                ft.IconButton(ft.icons.NEWSPAPER, on_click=lambda _: page.go('/parsing_news')),
                ft.IconButton(ft.icons.SETTINGS_CELL, on_click=lambda _: page.go('/backtestings')),
                ft.IconButton(ft.icons.ANALYTICS, on_click=lambda _: page.go('/statistics')),
                ft.IconButton(ft.icons.NOTES, on_click=lambda _: page.go('/notes')),
                ft.IconButton(ft.icons.SUPPORT_AGENT, on_click=lambda _: page.go('/support')),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings')),
            ]
        )
    return NavBar