import flet as ft

# Data Table styling dictionary
data_table_style: dict = {
    "main": {
        "expand": 3,
        "bgcolor": "#fdfdfe",
    },
    "data_table": {
        "heading_row_color": "#e3e4ea",
        "expand": True,
        "heading_row_height": 35,
        "data_row_max_height": 40,
    },
}

# Data Table class ...
class DataTable(ft.Container):
    def __init__(self):
        super().__init__(**data_table_style["main"])

        self.table = ft.DataTable(
            **data_table_style["data_table"],
        )

        headers: list = ["Full name", "Email Address", "Role",]

        self.table.columns = [
            ft.DataColumn(ft.Text(title, weight="w600", 
            size=12)) for title in headers
        ]

        self.content = ft.Column(
            scroll="hidden", controls=[ft.Row(controls=[self.table])]
        )

form_style: dict = {
    "main": {
        "expand": 2,
        "bgcolor": "#fdfdfe",
        "padding": ft.padding.only(left=35, right=35),
    },
    "input": {
        "height": 38,
        "border_color": "#aeaeb3",
        "focused_border_color": "black",
        "border_radius": 5,
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "border_width": 1.5,
        "text_size": 12,
    },
}

# form class styling ++ logic ...
class Form(ft.Container):
    def __init__(self, table: ft.DataTable):
        super().__init__(**form_style['main'])
        self.table = table

        # create input fields ...
        self.name = ft.TextField(**form_style['input'])
        self.email = ft.TextField(**form_style['input'])
        self.role = ft.TextField(**form_style['input'])

        # lists for logic and or loops
        data: list = ["Full name", "Email Address", "Role"]
        fields: list = [self.name, self.email, self.role]

        # list comprehension to create the input fields + titles
        items: list = [
            ft.Column(
                expand=True, spacing=4,
                controls=[
                    ft.Text(title, size=12, weight="w500"),
                    fields[index]
                ]
            )
            for index, title in enumerate(data)
        ]

        # finally, a save button to push the data to the UI + CSV file (later) ,,,
        self.add = ft.ElevatedButton(
            text="Save",
            color="white",
            bgcolor="blue600",
            height=40,
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data,
        )

        # self.content is ft.Container.content property since this inherits from ft.Container ...
        self.content = ft.Column(
            controls=[
                ft.Divider(height=10, color="transparent"),
                ft.Text("Records System", size=28, width="w900"),
                ft.Divider(height=30, color="transparent"),
                ft.Row(spacing=20, expand=True, controls=items),
                ft.Divider(height=10, color="transparent"),
                ft.Row(
                    alignment="end",
                    controls=[self.add], 
                    expand=True),
                ]
            )
        
    def create_data_row(self, values: list):
        data = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(values[0], size=12, weight="600")),
                ft.DataCell(ft.Text(values[1], size=12, weight="600")),
                ft.DataCell(ft.Text(values[2], size=12, weight="600")),
            ]
        )

        return data
    
    def update_data_table(self, data: ft.DataRow):
        # now, w/ access to the dt table ...
        self.table.rows.append(data)
        self.table.update()

    def save_data(self, event):
        values: list = [self.name.value, self.email.value, self.role.value]
        # check all fields first ...
        if all(values):
            # fist, create the data row and return it
            data = self.create_data_row(values)
            # next, update the data table (pass the instance of it)
            self.update_data_table(data)


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT

    dataTable: ft.Container = DataTable()
    form: ft.Container = Form(table=dataTable.table)

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Column(
                    expand=5,
                    controls=[form, dataTable],
                    on_scroll=True
                )
            ],
        )
    )

if __name__ == "__main__":
    ft.app(target=main)