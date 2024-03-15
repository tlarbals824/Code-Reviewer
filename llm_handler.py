from openai import OpenAI

import logging


def generate_review(review_target_code, request_api_key):
    client = OpenAI(api_key=request_api_key)

    logging.getLogger().info("generating review")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": """
         당신은 유능한 번역가입니다. 한국어와 영어 모두 원어민 수준으로 유창하게 구사할 수 있으며, 높은 수준의 어휘력을 갖고 있습니다. 사용자의 대답에 대해 모두 한글로 번역하여 제공합니다.
         또한 당신은 프로그래밍에 대한 지식이 풍부하며, 다양한 프로그래밍 언어를 사용하여 코드를 작성할 수 있습니다. 이에 대한 지식을 바탕으로 코드 리뷰를 수행할 수 있습니다.              
                    """},
            {"role": "user",
             "content": """
            first summary provided code,
            Review your provided code about method naming, logic flow, or handling exeception and provide a list of recommendations. and also provide a brief explanation of the code.

            {0}""".format(review_target_code)},
        ]
    )

    return response.choices[0].message.content
