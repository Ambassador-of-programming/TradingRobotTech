import flet as ft
import time

def Select_ta_ma_osc(page):
    class Select_ma_ocs:
        def __init__(self) -> None:
            self.error_ma_osc = ft.Text(color='red')
            self.ma_osc_select = ft.Dropdown(
                width = 280,
                label = 'Выберите стратегию',
                options = [ft.dropdown.Option("Moving Averages"),
                           ft.dropdown.Option("Oscillators"),
                           ]
                )
        def ma_osc_go(self, event):
            if self.ma_osc_select.value is not None:
                if self.ma_osc_select.value == "Moving Averages":
                    return page.go("/trading_strategy/select_ma_osc/moving_averages/select_ma_all_strategy")

                elif self.ma_osc_select.value == "Oscillators":
                    return page.go("/trading_strategy/select_ma_osc/oscillators/select_osc_all_strategy")
            else:
                self.error_ma_osc.color = 'red'
                self.error_ma_osc.value = "Нельзя выбрать пустое значение" 
                self.error_ma_osc.update()
                time.sleep(5)
                self.error_ma_osc.value = ''
                self.error_ma_osc.update()
            
        def ma_osc_submit(self):
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=self.ma_osc_go)

    select_ma_ocs = Select_ma_ocs()
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("""Благодаря библиотеке tradingview-ta, вы можете автоматизировать\nпроцесс торговли, создавая и тестируя свои торговые стратегии на\n основе технического анализа финансовых рынков. Это позволяет вам трейдеру\n автоматически выполнять торговые решения, опираясь на аналитику и индикаторы от\n платформы TradingView.""")  
            ],
            on_scroll=True,
            alignment=ft.MainAxisAlignment.CENTER
        ),
            ft.Row(
                [
                    select_ma_ocs.ma_osc_select,
                    select_ma_ocs.error_ma_osc,
                    select_ma_ocs.ma_osc_submit()

                ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        
        ]
    )
    return content