import flet as ft

class Router:
    
    def __init__(self, **kwargs):
        self.routes = kwargs
        self.body = ft.Container(content=self.routes['/trading_strategy'])

    async def route_change(self, route):
        self.body.content = self.routes[route.route]
        await self.body.update_async()