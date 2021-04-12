import json
import pprint

from language import *

main_dict = Dictionary()
main_dict.build()
main_dict.print()

input_text = 'eel'
print(main_dict.translate(input_text))
