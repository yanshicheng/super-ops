from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """自定义异常"""
    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(response.data, list):
            message = response.data[0]
        else:
            message = response.data.get('detail') if response.data.get('detail') else response.data

        notification_response = dict()
        notification_response['code'] = -1
        notification_response['message'] = message
        notification_response['data'] = None
        response.data = notification_response
    print(response.data)
    return response
