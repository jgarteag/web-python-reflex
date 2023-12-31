import reflex as rx
import web_python_reflex.constants as constants
from web_python_reflex.styles.styles import Size, Colors
from web_python_reflex.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="logojuan.png",
                alt="Logo juanma",
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value,
            ),
            rx.text("Juanma´s Page"),
            rx.spacer(),
            link_icon(
                "github",
                constants.GITHUB_URL,
            ),
            link_icon(
                "youtube",
                constants.YOUTUBE_URL,
            ),
            link_icon(
                "linkedin",
                constants.LINKEDIN_URL,
            ),
            width="100%"
        ),
        bg=Colors.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Colors.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )