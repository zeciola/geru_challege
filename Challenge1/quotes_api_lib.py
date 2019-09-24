from dataclasses import dataclass
from requests import get


@dataclass
class Quote:
    """API class for access the quotes."""

    link: str = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'

    def get_quotes(self) -> dict:
        """
        Function for show quotes in API
        :return: dict
        """
        return get(self.link).json()

    def get_quote(self, number) -> dict:
        """
        Function for show a one quote by number
        :param number: int
        :return: dict
        """
        return get(f'{self.link}/{number}').json()
