import json
import pprint


with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.loads(dictionary_file.read())

def find_words(word):
    return filter(lambda x: x['english'] == word, dictionary)

def translate_word(word):
    translation = next(find_words(word))['translation']
    # if translation == '[AUTO]':
    #     translation = compile_word(translation)
    # print(translation)
    return translation

def translate(text):
    input_words = text.split(' ')
    output = ''
    # Loop through words in input phrase
    for word in input_words:
        output += translate_word(word)
    return output

def compile_word(term):
    lit = term['literal']
    components = lit.split(' ')
    # Start the translation with just the translation of the last word in the literal definition phrase (e.g., water + snake should start with snake, which is then modified)
    # translation = [translate_word(components.pop())]
    translation = []

    # Loop through component words and translate each
    for c in components:
        t = translate_word(c)
        if t == '[AUTO]':
            t = compile_word(next(find_words(c)))

        translation.append(t)
    # translation = translation[:-1]
    # change word order?
    return "'".join(translation)

# Build dictionary
for term in dictionary:
    # Generate compound terms from translations of parts (e.g., eel --> water + snake)
    if term['translation'] == '[AUTO]':
        # Combine translated terms and save
        term['translation'] = compile_word(term)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dictionary)

input_text = 'eel'
print(translate(input_text))
