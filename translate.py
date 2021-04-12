import json
import pprint

input_text = 'eel'

with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.loads(dictionary_file.read())

def translate_word(word):
    return next(filter(lambda x: x['english'] == word, dictionary))['translation']

def translate(text):
    input_words = text.split(' ')
    output = ''
    for word in input_words:
        output += translate_word(word)
    return output

# Build dictionary
for term in dictionary:
    # Generate compound terms from translations of parts (e.g., eel --> water + snake)
    if term['translation'] == 'AUTO':
        lit = term['literal']
        components = lit.split(' ')
        translation = [translate_word(components.pop())]
        for c in components:
            translation.append(translate_word(c))
        term['translation'] = ''.join(translation)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dictionary)
