from termcolor import colored


class Color:

    @staticmethod
    def colored(text: str, color: str) -> str:
        return colored(
            text,
            color,
        )

    @staticmethod
    def colored_bold(text: str, color: str) -> str:
        return colored(text, color, attrs=["bold"])

    @staticmethod
    def colored_underlined(text: str, color: str) -> str:
        return colored(text, color, attrs=["underline"])


"""HOW TO USE"""

# ATTRIBUTES: dict[Attribute, int] = {
#     "bold": 1,
#     "dark": 2,
#     "underline": 4,
#     "blink": 5,
#     "reverse": 7,
#     "concealed": 8,
# }

# HIGHLIGHTS: dict[Highlight, int] = {
#     "on_black": 40,
#     "on_grey": 40,  # Actually black but kept for backwards compatibility
#     "on_red": 41,
#     "on_green": 42,
#     "on_yellow": 43,
#     "on_blue": 44,
#     "on_magenta": 45,
#     "on_cyan": 46,
#     "on_light_grey": 47,
#     "on_dark_grey": 100,
#     "on_light_red": 101,
#     "on_light_green": 102,
#     "on_light_yellow": 103,
#     "on_light_blue": 104,
#     "on_light_magenta": 105,
#     "on_light_cyan": 106,
#     "on_white": 107,
# }

# COLORS: dict[Color, int] = {
#     "black": 30,
#     "grey": 30,  # Actually black but kept for backwards compatibility
#     "red": 31,
#     "green": 32,
#     "yellow": 33,
#     "blue": 34,
#     "magenta": 35,
#     "cyan": 36,
#     "light_grey": 37,
#     "dark_grey": 90,
#     "light_red": 91,
#     "light_green": 92,
#     "light_yellow": 93,
#     "light_blue": 94,
#     "light_magenta": 95,
#     "light_cyan": 96,
#     "white": 97,
# }
