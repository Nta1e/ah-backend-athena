import json

from rest_framework.renderers import JSONRenderer


class ArticleJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        """
        If the view throws an error (such as the user can't be authenticated
        or something similar), `data` will contain an `errors` key. We want
        the default JSONRenderer to handle rendering errors, so we need to
        check for this case.
        """
    
        errors = data.get('errors', None)

        if errors is not None:
            """
            As mentioned about, we will let the default JSONRenderer handle
            rendering errors.
            return super(ArticlesJSONRenderer, self).render(data)
            """
        """Finally, we can render our data under the "user" namespace."""
        return json.dumps({
            'article': data
        })


class ListArticlesJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        return json.dumps({
            "articles": data,
        })

class ArticleReportJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        errors = data.get('errors', None)

        if errors is not None:

            return super(ArticleReportJSONRenderer, self).render(data)

        return json.dumps({
            'reported': data
        })


class ArticleListReportJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        return json.dumps({
            'reported': data
        })