import os
import requests


def translate_file(inpath, outpath, inlang, outlang='ru'):
    """
    Translates text in infile from inlang and writes translated to outlang text to outfile
    :param inpath: <str> path to the file with text
    :param outpath: <str> path to write translated text
    :param inlang: <str> language to translate from
    :param outlang: <str> language to translate to
    :return: None
    """
    lang = '-'.join((inlang, outlang))
    with open(inpath) as f:
        translated_text = translate_it(f.read(), lang=lang)
    with open(outpath, 'w') as f:
        f.write(translated_text)


def translate_it(text, lang='ru-en'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

files = [f for f in os.listdir(os.path.dirname(__file__)) if '.txt' in f]

for file in files:
    name, ext = os.path.splitext(file)
    translate_file(file, name + '-RU.txt', name.lower(), 'ru')