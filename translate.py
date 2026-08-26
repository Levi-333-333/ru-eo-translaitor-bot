from dotenv import load_dotenv
from deep_translator import GoogleTranslator

def translate(text: str) -> str:
    strip_text = text.strip()
    if not strip_text:
        return ""

    PROXY_URL = load_dotenv("PROXY_URL")
    proxy = {
        "http": PROXY_URL,
        "https": PROXY_URL
    }

    eo_special_chars = ['ĉ', 'ĝ', 'ĥ', 'ĵ', 'ŝ', 'ŭ', 'Ĉ', 'Ĝ', 'Ĥ', 'Ĵ', 'Ŝ', 'Ŭ']
    is_eo = any(car in strip_text for car in eo_special_chars) or strip_text.isascii()

    if is_eo:
        input_lang = 'eo'
        output_lang = 'ru'
    else:
        input_lang = 'ru'
        output_lang = 'eo'

    return GoogleTranslator(source=input_lang, target=output_lang, proxies=proxy).translate(strip_text)