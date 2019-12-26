import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster-pastedeploy==0.7',
    'pyramid==1.10.4',
    'pyramid==1.10.4',
    'pyramid-debugtoolbar==4.5',
    'waitress==1.4.1',
    'alembic==1.2.0',
    'pyramid-retry==2.0',
    'pyramid-tm==2.2.1',
    'SQLAlchemy==1.3.8',
    'transaction==2.4.0',
    'zope.sqlalchemy==1.1',
    'cornice==3.6.0',
    'marshmallow==3.2.0'
]

tests_require = [
    'WebTest==2.0.33 ',
    'pytest==5.1.3',
    'pytest-cov==2.7.1',
]

setup(
    name='geru_quotes',
    version='0.0',
    description='geru_quotes',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = geru_quotes:main',
        ],
        'console_scripts': [
            'initialize_geru_quotes_db=geru_quotes.scripts.initialize_db:main',
        ],
    },
)
