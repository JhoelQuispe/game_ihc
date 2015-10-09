
import unicodedata

def quitar_tildes(s):
    if type(s) == str:
        s = s.decode('utf-8')

    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def quitar_words(texto , word):
    texto = texto.split(' ')
    return ' '.join([i for i in texto if i != word])


def preprocesar(texto):
    texto = quitar_tildes(texto)
    texto = texto.lower()
    return texto
