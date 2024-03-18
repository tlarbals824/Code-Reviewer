from openai import OpenAI

import logging

import prompt

def generate_review(review_target_code, request_api_key, llm_type='chat_gpt'):
    if(llm_type == 'chat_gpt'):
        return generate_message_from_chat_gpt(review_target_code, request_api_key)
    return ""


def generate_message_from_chat_gpt(review_target_code, request_api_key):
    client = OpenAI(api_key=request_api_key)

    logging.getLogger().info("generating message")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": prompt.getChatGptSystemPrompt()},
            {"role": "user",
             "content": """
            {0}""".format(review_target_code)}
        ]
    )

    return response.choices[0].message.content