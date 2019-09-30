# from cornice import Service
# from geru_quotes.views.api.schema import UserSessionSchema
# from pyramid.httpexceptions import HTTPOk
# from cornice.validators import marshmallow_body_validator
# from geru_quotes.models import user_session
# from geru_quotes.utils.quotes_api_lib import Quote
#
# quote = Service(name='quote', path='api/quotes')
#
#
# @quote.get(
#     schema=UserSessionSchema,
#     validators=marshmallow_body_validator,
# )
# @view_defaults(render='templates/quotes.jinja2')
# def show_quoutes(request):
#
#     q = Quote()
#
#     return q.get_quotes()
#
#     ...
