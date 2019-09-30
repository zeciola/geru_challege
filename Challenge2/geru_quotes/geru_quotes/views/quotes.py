from dataclasses import dataclass
from datetime import datetime
from geru_quotes.models import UserSession
from geru_quotes.utils.quotes_api_lib import Quote
from pyramid.request import Request
from pyramid.view import view_config, view_defaults
from random import randrange
from requests import Session


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    return {'author': 'José Ricardo Ciola Bricio'}


@view_defaults(renderer='templates/quotes.jinja2')
@dataclass
class QuotesViews:
    request: Request

    def register_session(self, request: Request, session: Session):

        user_session = UserSession()
        user_session.session_date = datetime.now()
        user_session.session_path = session.request.path
        user_session.session_browser = request.user_agent
        user_session.session_timestamp = session.created
        user_session.session_pdtb_id = session.request.pdtb_id

        request.dbsession.add(user_session)
        request.dbsession.flush()


    @view_config(route_name='quotes')
    def show_quotes(self) -> dict:
        try:
            q = Quote()

            session = self.request.session

            session['origin_session'] = str(datetime.now())

            self.register_session(self.request, session)

            return q.get_quotes()

        except Exception as e:
            return dict(error=e)

    @view_config(route_name='quotes_number')
    def show_quote(self) -> dict:
        try:
            q = Quote()

            number = self.request.matchdict['number']

            session = self.request.session

            session['origin_session'] = str(datetime.now())

            self.register_session(self.request, session)

            return q.get_quote(number)
        except Exception as e:
            return dict(error=e)

    @view_config(route_name='quotes_random')
    def show_quote_random(self) -> dict:
        try:
            q = Quote()

            data = q.get_quotes()

            number = randrange(0, len(data['quotes']))

            session = self.request.session

            session['origin_session'] = str(datetime.now())

            self.register_session(self.request, session)

            return q.get_quote(number)
        except Exception as e:
            return dict(error=e)


@view_defaults(renderer='templates/quote.jinja2')
@dataclass
class QuoteView:
    request: str

    @view_config(route_name='quote')
    def show_quote(self) -> dict:
        try:
            q = Quote()

            number = self.request.matchdict['number']

            session = self.request.session

            session['origin_session'] = str(datetime.now())

            self.register_session(self.request, session)

            return q.get_quote(number)
        except Exception as e:
            return dict(error=e)
