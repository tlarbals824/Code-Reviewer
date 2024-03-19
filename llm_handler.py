from openai import OpenAI
# import google.generativeai as genai

import logging

import prompt


def generate_review(review_target_code, request_api_key, llm_type='chat_gpt'):
    # if (llm_type == 'chat_gpt'):
    return generate_message_from_chat_gpt(review_target_code, request_api_key)
    # return generate_message_from_gemini(review_target_code, request_api_key)


def generate_message_from_chat_gpt(review_target_code, request_api_key):
    client = OpenAI(api_key=request_api_key)

    logging.getLogger().info("generating message")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": prompt.get_code_review_system_prompt()},
            {"role": "user",
             "content": prompt.get_code_review_user_prompt()+review_target_code}
        ]
    )

    return response.choices[0].message.content


# def generate_message_from_gemini(review_target_code, request_api_key):
#     genai.configure(api_key=request_api_key)
#     model = genai.GenerativeModel("gemini-pro")

#     request_message = prompt.get_code_review_system_prompt()+ prompt.get_code_review_user_prompt() + review_target_code

#     return model.generate_content(request_message).text