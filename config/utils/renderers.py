from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    """
    Here is the code for the custom renderer
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """ Render the data into JSON """
        response_data = {
            "data": {
                "result": {},
                "error": {}
            },
            "responseDetail": "",
            "responseCode": ""
        }

        response_detail = renderer_context.get('response')
        if response_detail.exception:
            response_data['data']['error'] = response_detail.data
        else:
            response_data['data']['result'] = response_detail.data
        response_data['responseCode'] = response_detail.status_code
        response_data['responseDetail'] = response_detail.status_text
        # getattr(renderer_context.get('view').get_serializer().Meta, 'resource_name', 'objects')
        # call super to render the response
        response = super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)
        return response
