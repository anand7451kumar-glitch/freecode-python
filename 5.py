def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return 'hello'

print(greet('es'), 'Glenn')
print(greet('en'), 'Sally')