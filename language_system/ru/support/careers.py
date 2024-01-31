import flet as ft

async def careers(page):
    
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Станьте частью команды TradingRobotTech", size=30), 
                ft.IconButton(icon=ft.icons.SUPPORT_AGENT, icon_size=30),
            ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),

     
 

            
        ]
    )
    return content