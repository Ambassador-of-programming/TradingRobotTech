import flet as ft

async def appbar(page):
    async def go_trading_strategy(event):
        return await page.go_async('/trading_strategy')
    async def go_ai_trading(event):
        return await page.go_async('/ai_trading')
    async def go_crypto_arbitrage(event):
        return await page.go_async('/crypto_arbitrage')
    async def go_backtestings(event):
        return await page.go_async('/backtestings')
    async def go_statistics(event):
        return await page.go_async('/statistics')
    async def go_support(event):
        return await page.go_async('/support')
    async def go_settings(event):
        return await page.go_async('/settings')
    async def go_careers(event):
        return await page.go_async('/careers')
    
    appbar = ft.AppBar(
            
            # leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
            leading_width=40,
            toolbar_height=40,
            # title=ft.Text("Flet Router"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                # ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.TASK_ALT, on_click=go_trading_strategy),
                ft.IconButton(ft.icons.ROCKET, on_click=go_ai_trading),
                ft.IconButton(ft.icons.TASK_ROUNDED, on_click=go_crypto_arbitrage),
                ft.IconButton(ft.icons.SETTINGS_CELL, on_click=go_backtestings),
                ft.IconButton(ft.icons.ANALYTICS, on_click=go_statistics),
                ft.IconButton(ft.icons.SUPPORT_AGENT, on_click=go_support),
                ft.IconButton(ft.icons.SUPPORT, on_click=go_careers),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=go_settings),
                
            ]
        )
    return appbar