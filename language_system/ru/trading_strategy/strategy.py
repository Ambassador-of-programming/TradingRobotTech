import flet as ft
import time

def Trading_Strategy(page):
    class Select_strategy:
        def __init__(self) -> None:
            self.error_language = ft.Text(color='red')
            self.language_selects = ft.Dropdown(
                width = 280,
                label = 'Выберите стратегию',
                options = [
                    ft.dropdown.Option("Tradingview-ta"),
                ]
            )

        def language_select(self, event):
            if self.language_selects.value == None:
                self.error_language.color = 'red'
                self.error_language.value = "Нельзя выбрать пустое значение" 
                self.error_language.update()
                time.sleep(5)
                self.error_language.value = ''
                self.error_language.update()
            elif self.language_selects.value == 'Tradingview-ta':
                page.go('/trading_strategy/select_ma_osc')

        def language_submit(self):
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=self.language_select)
        
    select_strategy_instance = Select_strategy()
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Мои стратегии", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ALT, icon_size=30),
            ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),
            
            ft.Row(
                [   
                    select_strategy_instance.language_selects,
                    select_strategy_instance.error_language,
                    select_strategy_instance.language_submit(),

                ],
            alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row(
                [
                     
                ]
            )


        
        ]
    )
    return content