class Trundler(object):
    r"""
    Wrapper class for the Trundler API.
    Attributes
    ----------
    Fill this space

    Methods
    -------
    Fill this space
    """
    def __init__(self, key):
        r"""
        Initialization method of the :code:`trundlerPy` class.
        Parameters
        ----------
        key : str
            The API key from the Trundler API.
        host : str
            The base URL of the Trundler API.
        headers:  dict
            header to perform API requests.
        """
        self.key = key
        self.host = 'https://api.trundler.dev/'
        self.headers = {
            'accept': 'aplication/json',
            'X-Api-Key': self.key,
        }

    from ._retailer import retailer, retailer_products
    from ._product import products, product, product_prices
    from ._checkfuncions import check_params, check_response
