import io
import json
import logging
import oci

from fdk import response

import llm_handler as llm
import request_handler


def handler(ctx, data: io.BytesIO = None):
    try:
        request_data = request_handler.extractRequest(data)
    except Exception:
        return generate_error_response(ctx, 'request error occur')
    
    code,api_key = request_data['request_body']['code'],request_data['request_body']['api_key']

    message = llm.generate_review(code, api_key)

    return generate_response(ctx, message)

def generate_response(ctx, success_message):
    message = json.dumps({'message' : success_message}, ensure_ascii=False).encode('utf-8')

    return response.Response(
        ctx,
        response_data=message,
        headers={'Content-Type': 'application/json'},
    )

def generate_error_response(ctx, error_message):

    message = json.dumps({'message' : error_message}, ensure_ascii=False).encode('utf-8')

    return response.Response(
        ctx,
        response_data=message,
        headers={'Content-Type': 'application/json'},
        status_code=400
    )
