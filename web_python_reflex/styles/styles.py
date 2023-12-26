import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import TextColor, Colors

class Size(Enum):
    DEFAULT = "1em"
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
    "background": Colors.PRIMARY.value
}


