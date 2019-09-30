from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory(secret='Geru o melhor lugar para pegar emprestimos')

    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('cornice')
        config.set_session_factory(my_session_factory)
        config.scan()
    return config.make_wsgi_app()
