import pprint
import pandas as pd
from main import get_responses, push_to_sheet



def find_response(query=None):
    responses = get_responses()['responses']

    if query is None:
        return format_responses(responses)
    else:

        if query in str(responses):
            return format_responses(responses)
        else:
            return 'Query not found'


def format_responses(responses):
    response_list = []
    for response in responses:
        pprint.pprint(response)
        df = pd.DataFrame.from_dict(response['answers'], orient='index')
        text_answers = df.loc[:, 'textAnswers']
        internal_response_list = []
        for answer in text_answers:
            answer_value = answer['answers'][0]['value']
            internal_response_list.append(answer_value)

        response_list.append(internal_response_list)

        print(response_list)

    response_dataframe = pd.DataFrame(response_list)

    return response_dataframe

push_to_sheet(find_response())
