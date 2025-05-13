# Name: Torreno, Lerrica Jeremy S.
# Course/Year: BSCS-DS 1st YEAR
# Date: November 9, 2023
# Work title: Midterm Lab Work #1 

import re
import long_responses_bot as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    other_message = 0

    # Counts how many words are present in each predefined message 
    for word in user_message:
        if word in recognised_words:
            message_certainty += 100
        elif word == 'coffee':
            message_certainty += 2
        else: 
            other_message += 1


    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))
    other_percentage = float(other_message) / float(len(recognised_words))

    # Checks that the required words are in the string
    has_required_words = all(word in user_message for word in required_words)

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return int(other_percentage * 2)


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Longer responses
    response(long.R_BEAN, ['bean', 'beans'], single_response=True)
    response(long.R_BENEFITS, ['health', 'healthy', 'healthiest'], single_response=True)
    response(long.R_COMMODITY, ['biggest', 'largest', 'traded', 'trading', 'commodity'], single_response=True)
    response(long.R_CONS, ['drink', 'morning', 'coffee'], required_words=['morning'])
    response(long.R_CREATIVITY, ['music', 'sound', 'song'], required_words=['boost'])
    response(long.R_EFFECTS, ['discovered', 'noticed', 'effects', 'effect', 'stimulating', 'coffee'], required_words=['stimulating'])
    response(long.R_EXPENSIVE, ['pricey', 'costly', 'expensive', 'overpriced'], single_response=True)
    response(long.R_PRODUCER, ['brazil', 'biggest', 'largest', 'producer', 'produce', 'produces'], single_response=True)
    response(long.R_RCONTEXT, ['religion', 'religious', 'history', 'culture'], single_response=True)
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    if highest_prob_list[best_match] > 200: 
        return best_match
    elif highest_prob_list[best_match] > 10 and highest_prob_list[best_match] <= 100:
        return "I'm still researching about it, I only have limited knowledge." 
    else:
        return "I only know about coffee." 

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))