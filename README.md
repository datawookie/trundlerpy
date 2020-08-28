# trundlerpy

[![Documentation Status](https://readthedocs.org/projects/trundlerpy/badge/?version=latest)](https://trundlerpy.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/datawookie/trundlerpy.svg?branch=master)](https://travis-ci.com/github/datawookie/trundlerpy)
[![codecov](https://codecov.io/gh/datawookie/trundlerpybranch/master/graph/badge.svg)](https://codecov.io/gh/datawookie/trundlerpy)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8c15645191c04d50b4f98efee6cee435)](https://www.codacy.com/manual/datawookie/trundlerpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=datawookie/trundlerpy&amp;utm_campaign=Badge_Grade)

This is a Python package for the Trundler API.

## Installation

Install from GitHub.

```bash
!pip3 install git+https://github.com/datawookie/trundlerpy
```

## Testing

To run the test suite:

1. Set the `TRUNDLER_KEY` environment variable.
2. Launch the tests with

```bash
pytest
```

## Documentation

To build the documentation:

```bash
make -C docs/ html
```

## Set the API Key

To access the full API you’ll need to first specify an API key.
To obtain a key, please [get in touch](https://www.trundler.dev/).

Storing your keys received from APIs and other sensitive information in a
secure file or as an environment variable is considered best practice to avoid
any potential malicious activity.

```python
import os

key = os.getenv('TRUNDLER_KEY')
```

## Usage

```python
from trundlerpy import Trundler

tr = Trundler(key = key)
```

### Retailers

Use `retailer()` to get a list of retailers.

```python
tr.retailer()
```

You can access the details for a specific retailer.

```python
tr.retailer(45)
```

### Products

Get a list of products for a specific retailer.

```python
tr.retailer_products(5)
```

Products can be filtered by name and brand.

```python
tr.retailer_products(5, product = "coffee", brand = "nespresso")
```

Get information on a specific product, filtering it by ID.

```python
tr.product(530290)
```

Get price history data for a specific product.

```python
tr.product_prices(530290)
```

## Documentation

[TrundlerPy Documentation](https://trundlerpy.readthedocs.io/)
