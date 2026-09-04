'''
Ограничения на перевочик:
1. Динна текста: 5000 символов
А ну и всё собственно, обидно даже :(
'''

from exceptions import Text_lenght_exception

def is_long(text: str) -> bool:
    if len(text) >= 5000:
        return True