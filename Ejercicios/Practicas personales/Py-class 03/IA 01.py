import re 
import random

def get_response(user_input):
    split_message = re.split(r'\s|,|;|:', user_input.lower())
    response = check_for_greeting(split_message)
    return response

def mesage_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_for_greeting(message):
    high_prob={}

    def reponse(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal high_prob
        high_prob[bot_response] = mesage_probability(message, list_of_words, single_response, required_words)

    reponse('Hola', ['hola', 'saludos', 'buenas'], single_response=True)
    reponse('Estoy bien y tú?', ['como', 'estas', 'buenas'], required_words=['como'])
    reponse('Estamos ubicados en Senati Chiclayo', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
    reponse('Hasta luego', ['adios', 'hasta', 'luego'], single_response=True)

    best_match = max(high_prob, key=high_prob.get)
    print(high_prob)
    
    return unknown() if high_prob[best_match] < 1 else best_match

def unknown():
    reponse = ['No entiendo lo que dices', 'No sé qué quieres decir', '¿Podrías repetirlo?', 'Búscalo en algún navegador'][random.randint(0, 3)]
    return reponse

while True:
    print('Bot: ' + get_response(input('You: ')))
