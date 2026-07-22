'''
Ограничения на перевочик:
1. Динна текста: 5000 символов
А ну и всё собственно, обидно даже :(
'''

def is_long(text: str) -> bool:
    if len(text) >= 5000: return True
    return False