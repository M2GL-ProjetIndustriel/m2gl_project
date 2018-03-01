from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        response = renderer_context['response']

        if response.exception:
            new_data = {'error': data}
        else:
            new_data = {'data': data}

        return super().render(new_data, media_type, renderer_context)
