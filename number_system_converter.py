import flet as ft


def main(page: ft.Page):
    page.title = "Number Converter"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

    # Input field - CORRECTED syntax
    number_input = ft.TextField(
        label="Enter number",  # Fixed: lowercase 'label' not 'Label'
        width=300,
        bgcolor='blue'
    )

    # From system dropdown - CORRECTED syntax
    from_system = ft.Dropdown(
        label="From",
        width=150,
        bgcolor='green',
        options=[
            ft.dropdown.Option("Binary"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Decimal"
    )

    to_system = ft.Dropdown(
        label="To",
        width=150,
        bgcolor='red',
        options=[
            ft.dropdown.Option("Binary"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Binary"
    )

    # Result display
    result = ft.Text(value="Result will appear here.")

    # Conversion function
    def convert(e):
        try:
            value = number_input.value.strip() if number_input.value else ""
            from_sys = from_system.value
            to_sys = to_system.value

            if not value:
                result.value = "Please enter a number"
                page.update()
                return

            # Convert to decimal first
            if from_sys == "Decimal":
                decimal_val = int(value)
            elif from_sys == "Binary":
                decimal_val = int(value, 2)
            elif from_sys == "Hexadecimal":
                decimal_val = int(value, 16)
            elif from_sys == "Octal":
                decimal_val = int(value, 8)
            else:
                result.value = "Please select a valid system"
                page.update()
                return

            # Convert to target system
            if to_sys == "Decimal":
                converted = str(decimal_val)
            elif to_sys == "Binary":
                converted = bin(decimal_val)[2:]
            elif to_sys == "Hexadecimal":
                converted = hex(decimal_val)[2:].upper()
            elif to_sys == "Octal":
                converted = oct(decimal_val)[2:]
            else:
                result.value = "Please select a valid target system"
                page.update()
                return

            result.value = f"{value} ({from_sys}) = {converted} ({to_sys})"

        except ValueError:
            result.value = "❌ Invalid number for selected system!"
        except Exception as ex:
            result.value = f"❌ Error: {str(ex)}"

        page.update()

    # Clear function
    def clear_input(e):
        number_input.value = ""
        result.value = "Result will appear here."
        page.update()

    # Layout - matching the original design
    page.add(
    ft.Text("Number Converter", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(height=10),

        # Input row
        ft.Row([
            number_input
        ], alignment=ft.MainAxisAlignment.CENTER),

        # Dropdowns row
        ft.Row([
            from_system,
            to_system
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Divider(height=10),

        # Buttons row
        ft.Row([
            ft.ElevatedButton("Convert", on_click=convert, width=150),
            ft.OutlinedButton("Clear", on_click=clear_input, width=150)
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Divider(height=10),

        # Result display
        ft.Container(
            content=result,
            padding=10,
            bgcolor='yellow',
            border_radius=10,
            width=360
        )
    )


# Run the app
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=5000)