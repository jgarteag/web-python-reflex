import reflex as rx
import web_python_reflex.styles.styles as styles
from web_python_reflex.views.navbar import navbar

def index() -> rx.Component:
    return rx.box(
        navbar()
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