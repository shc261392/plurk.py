from enum import Enum


class Qualifier(str, Enum):
    """Every plurk has a qualifier and it will be displayed on Plurk site.

    The display for EMPTY, COLON and FREESTYLE is the same on Plurk site, showing a `:` symbol.
    """
    EMPTY = ''
    COLON = ':'
    FREESTYLE = 'freestyle'
    PLAYS = 'plays'
    BUYS = 'buys'
    SELLS = 'sells'
    LOVES = 'loves'
    LIKES = 'likes'
    SHARES = 'shares'
    HATES = 'hates'
    WANTS = 'wants'
    WISHES = 'wishes'
    NEEDS = 'needs'
    HAS = 'has'
    WILL = 'will'
    HOPES = 'hopes'
    ASKS = 'asks'
    WONDERS = 'wonders'
    FEELS = 'feels'
    THINKS = 'thinks'
    DRAWS = 'draws'
    IS = 'is'
    SAYS = 'says'
    EATS = 'eats'
    WRITES = 'writes'
    WHISPERS = 'whispers'
