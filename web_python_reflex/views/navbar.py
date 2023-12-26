import reflex as rx
from web_python_reflex.styles.styles import Size, Colors

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="logojuan.png",
                alt="Juanmas Logo",
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value,
            ),
            rx.text("Juanma´s Page"),
            rx.spacer(),
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