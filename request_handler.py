import json
import logging


def extractRequest(data):
    request_data = {}

    request_body_str = data.getvalue()
    if request_body_str:
        request_data["request_body"] = json.loads(request_body_str)
    else:
        raise AttributeError("request body is empty. request must contain json body")

    return request_data
