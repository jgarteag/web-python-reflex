import reflex as rx
import web_python_reflex.styles.styles as styles
from web_python_reflex.styles.styles import Size
from web_python_reflex.views.navbar import navbar
from web_python_reflex.views.header import header
from web_python_reflex.views.footer import footer

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                footer(),
                width="100%",
                spacing=Size.VERY_BIG.value
            )
        )
)

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Juanma´s Reflex App",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
)

app.compile()