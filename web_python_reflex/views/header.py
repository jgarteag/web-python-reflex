import reflex as rx 
import web_python_reflex.styles.styles as styles   
from web_python_reflex.styles.styles import Size, TextColor
import web_python_reflex.constants as constants

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Welcome to my page!",
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="logojuan.png",
                alt="Logo juanma",
                width = "16em",
                height = "16em",
                margin_right = Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("¡Hi Coders!"),
                    rx.text("I´m Juan Manuel"),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    "I am a dedicated software engineer with a track record of leading projects and crafting inventive solutions. My emphasis lies in enhancing operational efficiency and ensuring code quality for ",
                    rx.span(
                        "outstanding outcomes",
                        color= TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!"
                ),
                rx.span(
                    "My website, built in Python using the REFLEX framework, aims to deliver an exceptional user experience by creating intuitive and efficient user interfaces."
                ),
                rx.link(
                    "#REFLEX",
                    href=constants.HASHTAG_URL,
                    is_external=True,
                    color = TextColor.TERTIARY.value,
                    padding_top = Size.BIG.value,
                    font_size = Size.MEDIUM.value
                ),
                align_items="start"
            ),
            flex_direction=["column","column","column","row","row"]
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )