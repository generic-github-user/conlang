import json
import pprint

class Dictionary:
    def __init__(self, dictionary='dictionary.json'):
        # self.dictionary = self.load_dict(dictionary)
        self.load_dict(dictionary)
        self.printer = pprint.PrettyPrinter(indent=4)
        # print(self.dictionary)

    def load_dict(self, dictionary):
        with open(dictionary, 'r') as dictionary_file:
            self.dictionary = json.loads(dictionary_file.read())
        return True

    def find_words(self, word):
        return list(filter(lambda x: x['english'] == word, self.dictionary))

    def translate_word(self, word):
        # translation = next(self.find_words(word))['translation']
        # print(next(self.find_words(word)))
        translation = self.find_words(word)[0]['translation']
        # if translation == '[AUTO]':
        #     translation = compile_word(translation)
        # print(translation)
        return translation

    def translate(self, text):
        input_words = text.split(' ')
        output = ''
        # Loop through words in input phrase
        for word in input_words:
            output += self.translate_word(word)
        return output

    def compile_word(self, term):
        lit = term['literal']
        components = lit.split(' ')
        # Start the translation with just the translation of the last word in the literal definition phrase (e.g., water + snake should start with snake, which is then modified)
        # translation = [translate_word(components.pop())]
        translation = []

        # Loop through component words and translate each
        for c in components:
            try:
                t = self.translate_word(c)
                if t == '[AUTO]':
                    t = self.compile_word(self.find_words(c)[0])
            except:
                print(c)

            translation.append(t)
        # translation = translation[:-1]
        # change word order?
        return "'".join(translation)

    def build(self):
        # Build dictionary
        for term in self.dictionary:
            # Generate compound terms from translations of parts (e.g., eel --> water + snake)
            if term['translation'] == '[AUTO]':
                # Combine translated terms and save
                term['translation'] = self.compile_word(term)
        return True

    def print(self):
        self.printer.pprint(self.dictionary)
