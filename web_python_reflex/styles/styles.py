import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import TextColor, Colors

MAX_WIDTH = "1000px"

class Size(Enum):
    DEFAULT = "1em"
    MEDIUM = "0.8em"
    SMALL = "0.5em"
    BIG = "2em"
    VERY_BIG = "4em"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Colors.PRIMARY.value,
    rx.Heading:{
        "color": TextColor.ACCENT.value,
        "font_family": Font.DEFAULT.value
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover":{
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },
    rx.Span: {
        "font_size": Size.MEDIUM.value
    }
}

max_width_style = dict(
    align_items="start",
    padding_x = Size.BIG.value,
    width = "100%",
    max_width = MAX_WIDTH
)


