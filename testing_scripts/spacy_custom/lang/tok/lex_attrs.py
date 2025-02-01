from ...attrs import LIKE_NUM

# fmt: off
_num_words = [
    "wan", "tu", "luka", "mute", "ala", "ale"
]
_ordinal_words = [
    "wan", "tu", "luka", "mute", "ala", "ale"
]
# fmt: on


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    text_lower = text.lower()
    if text_lower in _num_words:
        return True
    # Check ordinal number
    if text_lower in _ordinal_words:
        return True
    # if text_lower.endswith(("st", "nd", "rd", "th")):
    #     if text_lower[:-2].isdigit():
    #         return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
