import json
import pprint

class Dictionary:
    """Stores words with associated translations and metadata and provides methods for updating/adding to the list"""
    def __init__(self, dictionary:String='dictionary.json'):
        """Create a new dictionary object and load data from local file"""
        # self.dictionary = self.load_dict(dictionary)
        self.load_dict(dictionary)
        self.printer = pprint.PrettyPrinter(indent=4)
        # print(self.dictionary)
        self.build()

    def add_term(self, english, type, translation='[AUTO]'):
        """Add a term to the dictionary"""

        word = {
            'english': english,
            'translation': translation,
            'type': type
        }
        self.dictionary.append(word)

    def load_dict(self, dictionary):
        """Load dictionary from local file"""
        with open(dictionary, 'r') as dictionary_file:
            self.dictionary = json.loads(dictionary_file.read())
        return True

    def save_dict(self):
        """Save the dictionary to a JSON dump"""
        with open('dictionary.json', 'w') as savefile:
            json.dump(self.dictionary, savefile)
        return True

    def find_words(self, word):
        """Get word objects matching criteria"""
        return list(filter(lambda x: x['english'] == word, self.dictionary))

    def translate_word(self, word):
        """Find translation for word in dictionary"""
        # translation = next(self.find_words(word))['translation']
        # print(next(self.find_words(word)))
        translation = self.find_words(word)[0]['translation']
        # if translation == '[AUTO]':
        #     translation = compile_word(translation)
        # print(translation)
        return translation

    def translate(self, text):
        """Translate a phrase using the dictionary"""
        input_words = text.split(' ')
        output = ''
        # Loop through words in input phrase
        for word in input_words:
            output += self.translate_word(word)
        return output

    def compile_word(self, term):
        """Assemble a compound word from its parts"""
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
        """Fill in any data in the dictionary that needs to be created dynamically"""

        # Build dictionary
        for term in self.dictionary:
            # Generate compound terms from translations of parts (e.g., eel --> water + snake)
            if term['translation'] == '[AUTO]':
                # Combine translated terms and save
                term['translation'] = self.compile_word(term)
        return True

    def print(self):
        """Print the dictionary to the console"""
        self.printer.pprint(self.dictionary)
