from openai import OpenAI

import logging

import prompt


def generate_review(review_target_code, request_api_key):
    client = OpenAI(api_key=request_api_key)

    logging.getLogger().info("generating review")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": prompt.getCodeReviewSystemPrompt()},
            {"role": "user",
             "content": """
            first summary provided code,
            Review your provided code about method naming, logic flow, or handling exeception and provide a list of recommendations. and also provide a brief explanation of the code.

            {0}""".format(review_target_code)}
        ]
    )

    return response.choices[0].message.content
