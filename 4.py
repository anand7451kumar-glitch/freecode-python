def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    else:
        print('hello')

print(greet('es'), 'Glenn')
print(greet('en'), 'Sally')