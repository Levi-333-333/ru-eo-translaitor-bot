'''
Ограничения на перевочик:
1. Динна текста: 5000 символов
А ну и всё собственно, обидно даже :(
'''

from exceptions import Text_lenght_exception

def is_long(text: str):
    if len(text) >= 5000:
        raise Text_lenght_exception("Длинна сообщения не доджна превышать 5000 симполов. Уменьшите объём текста.\n\nLa mesaĝo longeco ne devas superi 5000 signojn. Redukti la kvanton da teksto.")