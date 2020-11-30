import requests
import json
import pandas as pd

from ._checkfuncions import check_params, check_response
from ._params import parameters


def _get_retailer(self, host, headers, params):
    """Describe this method here."""
    if not params:
        endpoint = '/retailer'

        response = requests.get(f"{self.host}{endpoint}", headers=self.headers)

        # Check response
        check_response(response)

    else:
        id = str(params['id'])
        endpoint = f"/retailer/{id}"

        response = requests.get(f"{self.host}{endpoint}", headers=self.headers)

        # Check response
        check_response(response)

    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    # Rename columns
    df.rename(columns={
        'id': 'retailer_id',
        'url': 'retailer_url'}, inplace=True)

    return df


def _get_retailer_prods(self, host, headers, params):
    """Describe this method here."""
    id = str(params['id'])
    endpoint = f"/retailer/{id}/product"

    del params['id']

    response = requests.get(self.host + endpoint, headers=self.headers, params=params)

    # Check response
    check_response(response)

    j_response = json.loads(response.text)
    df = pd.DataFrame(pd.json_normalize(j_response))

    n_prods = len(df.index)

    # Rename and delete columns
    if n_prods != 0:
        df = df[['id', 'product', 'brand', 'model', 'sku']]
        df.rename(columns={
            'id': 'product_id'}, inplace=True)

    if ('head' not in params) or (not params['head']):
        if n_prods == 0:
            message = "No products are currently available for this retailer."
            return message
        else:
            return df
    elif params['head']:

        message = str(n_prods) + " products will be returned."
        return message


def retailer(self, id=None, **kwargs):
    """Describe this method here."""
    # Set required and optional params
    req_params      = parameters['retailer']['req_params']
    req_or_params   = parameters['retailer']['req_or_params']
    opt_params      = parameters['retailer']['opt_params']

    # Add to dict to check
    if id is not None:
        kwargs.update({'id': id})

    # Check params
    params = check_params(req_params, req_or_params, opt_params, kwargs)

    return _get_retailer(self, self.host, self.headers, params)


def retailer_products(self, id=None, **kwargs):
    """Describe this method here."""
    req_params      = parameters['retailer_products']['req_params']
    req_or_params   = parameters['retailer_products']['req_or_params']
    opt_params      = parameters['retailer_products']['opt_params']

    # Add to dict to check
    if id is not None:
        kwargs.update({'id': id})

    # Check params
    params = check_params(req_params, req_or_params, opt_params, kwargs)

    return _get_retailer_prods(self, self.host, self.headers, params)
