import flet as ft
import time

def Select_ma_all_strategy(page):
    class Select_ma_ocs:
        def __init__(self) -> None:
            self.error_ma_osc = ft.Text(color='red')
            self.ma_all_select = ft.Dropdown(
                width = 280,
                label = 'Выберите стратегию',
                options = [ft.dropdown.Option("EMA10"),
                           ft.dropdown.Option("EMA20"),
                           ft.dropdown.Option("EMA30"),
                           ft.dropdown.Option("EMA50"),
                           ft.dropdown.Option("EMA100"),
                           ft.dropdown.Option("EMA200"),
                           ft.dropdown.Option("HullMA"),
                           ft.dropdown.Option("Ichimoku"),
                           ft.dropdown.Option("SMA10"),
                           ft.dropdown.Option("SMA20"),
                           ft.dropdown.Option("SMA30"),
                           ft.dropdown.Option("SMA50"),
                           ft.dropdown.Option("SMA100"),
                           ft.dropdown.Option("SMA200"),
                           ft.dropdown.Option("VWMA"),
                           ]
                )
        def ma_all_go(self, event):
            if self.ma_all_select.value == None:
                self.error_ma_osc.color = 'red'
                self.error_ma_osc.value = "Нельзя выбрать пустое значение" 
                self.error_ma_osc.update()
                time.sleep(5)
                self.error_ma_osc.value = ''
                self.error_ma_osc.update()
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            elif self.ma_all_select.value == "EMA10":
                pass
            

        def ma_all_submit(self):
            return ft.ElevatedButton(text="Выбрать", icon=ft.icons.LANGUAGE, on_click=self.ma_all_go)

    select_ma_ocs = Select_ma_ocs()
    content = ft.Column(
        [
            ft.Row(
            [
                ft.Text("Выберите нужную стратегию", size=30), 
                ft.IconButton(icon=ft.icons.TASK_ALT, icon_size=30),
                ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
            ft.Row(
                [
                    select_ma_ocs.ma_all_select,
                    select_ma_ocs.error_ma_osc,
                    select_ma_ocs.ma_all_submit()

                ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        
        ]
    )
    return content