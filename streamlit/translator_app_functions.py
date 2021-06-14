from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
lang_dict = {v: k for k, v in constants.LANGUAGES.items()}

def translate_word(word, language):
    language = language.lower()
    translation = translator.translate(word, dest=lang_dict[language])
    return f"{(translation.origin).replace('_', ' ')} ({translation.src}) --> {translation.text} ({translation.dest})"


pred_dict = {0: 'airplanes', 1: 'basket_bin', 2: 'bed', 3: 'bench', 4: 'book', 5: 'cabinet', 6: 'car', 7: 'cat', 8: 'chair', 9: 'clock', 10: 'dog', 11: 'door', 12: 'dress', 13: 'electric_socket', 14: 'fan', 15: 'fire_extinguisher', 16: 'flower', 17: 'headphones', 18: 'house_plant', 19: 'lamp', 20: 'light_bulb', 21: 'microwave', 22: 'motorbikes', 23: 'pants', 24: 'refrigerator', 25: 'shirt', 26: 'shoes', 27: 'shorts', 28: 'table', 29: 'watch', 
}

def prediction(pred):
    
    word = pred_dict[pred]
    return word