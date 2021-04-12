import json
import pprint

input_text = 'eel'

with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.loads(dictionary_file.read())

# Build dictionary
for term in dictionary:
    # Generate compound terms from translations of parts (e.g., eel --> water + snake)
    if term['translation'] == 'AUTO':
        lit = term['literal']
        components = lit.split(' ')
        translation = []
        for c in components:
            translation.append(list(filter(lambda x: x['english'] == c, dictionary))[0]['translation'])
        term['translation'] = ''.join(translation)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dictionary)
