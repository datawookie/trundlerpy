import requests
import json
import pandas as pd

from ._checkfuncions import check_params, check_response
from ._params import parameters

def _get_products(self, host, headers, params):
    """Describe this method here."""
    endpoint = '/product'

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers, params=params)

    # Check response
    check_response(response)

    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    # Rename and order columns
    df.rename(columns={'id': 'product_id'}, inplace=True)
    df = df.reindex(['product_id', 'retailer_id', 'product', 'brand', 'model', 'sku'],
                    axis=1)
    return df


def _get_product(self, host, headers, params):
    """Describe this method here."""
    id = str(params['id'])
    endpoint = f"/product/{id}"

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers)
    
    # Check response
    check_response(response)

    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    # Rename and order columns
    df.rename(columns={'id': 'product_id', 'url': 'product_url'}, inplace=True)
    df = df.reindex(['product_id', 'retailer_id', 'product_url', 'product', 'brand', 'model', 'sku', 'barcodes'],
                    axis=1)
    return df


def _get_product_prices(self, host, headers, params):
    """Describe this method here."""
    id = str(params['id'])
    endpoint = f"/product/{id}/price"
    del params['id']

    response = requests.get(f"{self.host}{endpoint}", headers=self.headers, params=params)

    # Check response
    check_response(response)

    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    return df


def products(self, **kwargs):
    """Find products by name, brand or sku."""
    # Set required and optional params
    req_params      = parameters['products']['req_params']
    req_or_params   = parameters['products']['req_or_params']
    opt_params      = parameters['products']['opt_params']

    # Check params
    params = check_params(req_params, req_or_params, opt_params, kwargs)

    return _get_products(self, self.host, self.headers, params)


def product(self, id=None):
    """Details for a specific product."""
    # Set required and optional params
    req_params      = parameters['product']['req_params']
    req_or_params   = parameters['product']['req_or_params']
    opt_params      = parameters['product']['opt_params']

    # Convert to dict to check
    if id is not None:
        args = {'id': id}
    else:
        args = {}

    # Check params
    params = check_params(req_params, req_or_params, opt_params, args)

    return _get_product(self, self.host, self.headers, params)


def product_prices(self, id=None):
    """Prices for a specific product."""
    # Set required and optional params
    req_params      = parameters['product_prices']['req_params']
    req_or_params   = parameters['product_prices']['req_or_params']
    opt_params      = parameters['product_prices']['opt_params']

    # Convert to dict to check
    if id is not None:
        args = {'id': id}
    else:
        args = {}

    # Check params
    params = check_params(req_params, req_or_params, opt_params, args)

    return _get_product_prices(self, self.host, self.headers, params)
