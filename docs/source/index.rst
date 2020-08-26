
trundlerpy
==========

.. image:: https://readthedocs.org/projects/trundlerpy/badge/?version=latest
   :target: https://trundlerpy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://travis-ci.com/datawookie/trundlerpy.svg?branch=master
   :target: https://travis-ci.com/github/datawookie/trundlerpy
   :alt: Build Status
.. image:: https://codecov.io/gh/datawookie/trundlerpybranch/master/graph/badge.svg
   :target: https://codecov.io/gh/datawookie/trundlerpy
   :alt: codecov
.. image:: https://app.codacy.com/project/badge/Grade/8c15645191c04d50b4f98efee6cee435
   :target: https://www.codacy.com/manual/datawookie/trundlerpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=datawookie/trundlerpy&amp;utm_campaign=Badge_Grade
   :alt: Codacy Badge


This is a Python package for the Trundler API

|

Installation
------------

Install from GitHub.

.. code-block:: python

   pip install git+https://github.com/datawookie/trundlerpy

|

Set the API Key
---------------

To access the full API you’ll need to first specify an API key.
To obtain a key, please get in touch. Contact details are in DESCRIPTION (Will be).

Storing your keys received from APIs and other sensitive information in a secure file or as an environment variable is considered best practice to avoid any potential malicious activity. Therefore, we save the API key as environment variables to keep our credentials safe.

.. code-block:: python

   import os

.. code-block:: python

   key = os.getenv('TRUNDLER_KEY')

|

Usage
-----

.. code-block:: python

   from trundlerpy import trundlerPy

.. code-block:: python

   tr = trundlerPy(key = key)

|

Retailers
^^^^^^^^^

List of Retailers
~~~~~~~~~~~~~~~~~

Use retailer() to get a list of retailers.

.. code-block:: python

   tr.retailer()

|

Specific Retailer
~~~~~~~~~~~~~~~~~

You can access the details for a specific retailer.

.. code-block:: python

   tr.retailer(45)

|

Products
^^^^^^^^
|

List of product for specific retailer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of products for a specific retailer.

.. code-block:: python

   tr.retailer_products(5)

|

Products can be filtered by name and brand.

.. code-block:: python

   tr.retailer_products(5, product = "coffee", brand = "nespresso")

|

Product Details
~~~~~~~~~~~~~~~

Get information on a specific product, filtering it by ID

.. code-block:: python

   tr.product(530290)

|

Product Prices
~~~~~~~~~~~~~~

Get price history data for a specific product.

.. code-block:: python

   tr.product_prices(530290)