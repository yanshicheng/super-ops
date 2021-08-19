from rest_framework.views import exception_handler
from base.response import json_error_response

def custom_exception_handler(exc, context):
    """自定义异常"""
    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(response.data, list):
            message = response.data[0]
        else:
            message = response.data.get('detail') if response.data.get('detail') else response.data
    else:
        message = None
    return json_error_response(message)
