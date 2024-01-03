import reflex as rx 
import web_python_reflex.styles.styles as styles
from web_python_reflex.styles.styles import Size, TextColor

def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "© 2024 Juan Manuel Guerrero",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value
            ),
            rx.link(
                "Creado con ",
                rx.box(class_name="nes-icon is-small heart"),
                " por Juanmgart",
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value
            ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="juanmgart.png",
            alt="Logo juanma y simbolo coder",
            class_name="nes-avatar is-large",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"
    )