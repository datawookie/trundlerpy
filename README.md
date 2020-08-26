# trundlerPy

[![Documentation Status](https://readthedocs.org/projects/trundlerpy/badge/?version=latest)](https://trundlerpy.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/lcalcagni/trundlerPy.svg?branch=master)](https://travis-ci.org/lcalcagni/trundlerPy)
[![codecov](https://codecov.io/gh/lcalcagni/trundlerPy/branch/master/graph/badge.svg)](https://codecov.io/gh/lcalcagni/trundlerPy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a19d4a42c8ef4106827a910d447f4462)](https://app.codacy.com/manual/lcalcagni/trundlerPy?utm_source=github.com&utm_medium=referral&utm_content=lcalcagni/trundlerPy&utm_campaign=Badge_Grade_Dashboard)

This is a Python package for the Trundler API.

## Installation

Install from GitHub.

```bash
!pip install git+https://github.com/lcalcagni/trundlerPy
```

## Set the API Key

To access the full API you’ll need to first specify an API key.
To obtain a key, please get in touch. Contact details are in DESCRIPTION
(Will be).

Storing your keys received from APIs and other sensitive information in a
secure file or as an environment variable is considered best practice to avoid
any potential malicious activity. Therefore, we save the API key as environment
variables to keep our credentials safe.  

```python
import os

key = os.getenv('TRUNDLER_KEY')
```

## Usage

```python
from trundlerPy import trundlerPy

tr = trundlerPy(key = key)
```

### Retailers

#### List of Retailers

Use `retailer()` to get a list of retailers.

```python
tr.retailer()
```

#### Specific Retailer

You can access the details for a specific retailer.

```python
tr.retailer(45)
```

### Products

#### List of product for specific retailer

Get a list of products for a specific retailer.

```python
tr.retailer_products(5)
```

Products can be filtered by name and brand.

```python
tr.retailer_products(5, product = "coffee", brand = "nespresso")
```

#### Product Details

Get information on a specific product, filtering it by ID

```python
tr.product(530290)
```

#### Product Prices

Get price history data for a specific product.

```python
tr.product_prices(530290)
```

## Documentation

[TrundlerPy Documentation](https://trundlerpy.readthedocs.io/)
