def greet(lang):
    if lang == 'es':
        return '\n**Welcome message**\nHOLA'
    else:
        return "\n**Welcome message**\nHELLO"

def lang():
    lang = input("Enter language: ")
    return lang
def name():
    name = input("Enter Name: ")
    return name

# print(greet('es'), " John!")
try:
    print(greet(lang()), name())
except TypeError:
    print(greet('en'), name())