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
    eo_words = ('esperanto', 'birdo', 'domo', 'amiko', 'patro', 'libro', 'tago', 'jaro', 'bela', 'bona', 'nova', 'rapida', 'facile', 'bone', 'ami', 'vidi', 'esti', 'havi', 'iri', 'voli', 'povi', 'la', 'kaj', 'kun', 'por', 'pri', 'ĉar', 'tamen', 'sub', 'sur', 'apud', 'hodiaŭ', 'morgaŭ', 'tiam', 'ĉiam', 'kiam', 'tio', 'kio', 'ĉio', 'nenio', 'tiu', 'kiu', 'ĉiu', 'neniu', 'tie', 'kie', 'ĉie', 'nenie', 'tiel', 'kiel', 'ĉiel', 'neniel', 'tial', 'kial', 'ĉial', 'nenial')
    is_eo = any(word in strip_text for word in eo_words) or any(car in strip_text for car in eo_special_chars) or strip_text.isascii()

    if is_eo:
        input_lang = 'eo'
        output_lang = 'ru'
    else:
        input_lang = 'ru'
        output_lang = 'eo'

    return GoogleTranslator(source=input_lang, target=output_lang, proxies=proxy).translate(strip_text)