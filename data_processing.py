import pprint
import pandas as pd
from main import get_responses


def find_response(query):
    responses = get_responses()['responses']

    for r in responses:
        if query in str(r):
            print(r)


def all_responses():
    responses = get_responses()['responses']

    response_list = []

    for itx, r in enumerate(responses):
        df = pd.DataFrame.from_dict(r['answers'], orient='index')
        text_answers = df.loc[:, 'textAnswers']
        internal_response_list = [itx]
        for answer in text_answers:
            answer_value = answer['answers'][0]['value']
            internal_response_list.append(answer_value)

        response_list.append(internal_response_list)

    return response_list

print(all_responses())