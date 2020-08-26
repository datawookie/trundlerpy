
trundlerPy
==========

.. image:: https://readthedocs.org/projects/trundlerpy/badge/?version=latest
   :target: https://trundlerpy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://travis-ci.org/lcalcagni/trundlerPy.svg?branch=master
   :target: https://travis-ci.org/lcalcagni/trundlerPy
   :alt: Build Status
.. image:: https://codecov.io/gh/lcalcagni/trundlerPy/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lcalcagni/trundlerPy
   :alt: codecov
.. image:: https://api.codacy.com/project/badge/Grade/a19d4a42c8ef4106827a910d447f4462
   :target: https://app.codacy.com/manual/lcalcagni/trundlerPy?utm_source=github.com&utm_medium=referral&utm_content=lcalcagni/trundlerPy&utm_campaign=Badge_Grade_Dashboard
   :alt: Codacy Badge


This is a Python package for the Trundler API

|

Installation
------------

Install from GitHub.

.. code-block:: python

   pip install git+https://github.com/lcalcagni/trundlerPy

|

Set the API Key
---------------

To access the full API you’ll need to first specify an API key.
To obtain a key, please get in touch. Contact details are in DESCRIPTION (Will be).

Storing your keys received from APIs and other sensitive information in a secure file or as an environment variable is considered best practice to avoid any potential malicious activity. Therefore, we save the API key as environment variables to keep our credentials safe.

.. code-block:: python

   import os

.. code-block:: python

   key = os.getenv('API_KEY')

|

Usage
-----

.. code-block:: python

   from trundlerPy import trundlerPy

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

.. container::

   +-----+-----------+-----------+-----------+----------+---------+
   |     | re        | retailer  | ret       | currency | visible |
   |     | tailer_id |           | ailer_url |          |         |
   +=====+===========+===========+===========+==========+=========+
   | 0   | 1         | EEM       | https     | USD      | True    |
   |     |           | Tec       | ://www.ee |          |         |
   |     |           | hnologies | mtechnolo |          |         |
   |     |           |           | gies.com/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 1   | 2         | Clicks    | htt       | ZAR      | True    |
   |     |           |           | ps://clic |          |         |
   |     |           |           | ks.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 2   | 3         | Dischem   | https://  | ZAR      | True    |
   |     |           |           | www.disch |          |         |
   |     |           |           | em.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 3   | 4         | Game      | https     | ZAR      | True    |
   |     |           |           | ://www.ga |          |         |
   |     |           |           | me.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 4   | 5         | W         | ht        | ZAR      | True    |
   |     |           | oolworths | tps://www |          |         |
   |     |           |           | .woolwort |          |         |
   |     |           |           | hs.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | ... | ...       | ...       | ...       | ...      | ...     |
   +-----+-----------+-----------+-----------+----------+---------+
   | 122 | 123       | Cellar    | https://c | ZAR      | True    |
   |     |           | Direct    | ellardire |          |         |
   |     |           |           | ct.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 123 | 124       | Getwine   | https://  | ZAR      | True    |
   |     |           |           | www.getwi |          |         |
   |     |           |           | ne.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 124 | 125       | Wickes    | https:/   | GBP      | False   |
   |     |           |           | /www.wick |          |         |
   |     |           |           | es.co.uk/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 125 | 126       | Order     | https:    | ZAR      | True    |
   |     |           | Wine      | //orderwi |          |         |
   |     |           |           | ne.co.za/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+
   | 126 | 127       | Debenhams | https://  | GBP      | False   |
   |     |           |           | www.deben |          |         |
   |     |           |           | hams.com/ |          |         |
   +-----+-----------+-----------+-----------+----------+---------+

   127 rows × 5 columns

|

Specific Retailer
~~~~~~~~~~~~~~~~~

You can access the details for a specific retailer.

.. code-block:: python

   tr.retailer(45)

.. container::

   +---+-------------+--------------------+-----------------------------+----------+---------+
   |   | retailer_id | retailer           | retailer_url                | currency | visible |
   +===+=============+====================+=============================+==========+=========+
   | 0 | 45          | Builders Warehouse | https://www.builders.co.za/ | ZAR      | True    |
   +---+-------------+--------------------+-----------------------------+----------+---------+



|
|

Products
^^^^^^^^
|

List of product for specific retailer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of products for a specific retailer.

.. code-block:: python

   tr.retailer_products(5)


.. container::

   +-----+------------+------------+-----------+-------+------------+
   |     | product_id | product    | brand     | model | sku        |
   +=====+============+============+===========+=======+============+
   | 0   | 607273     | CLINIQUE   | Clinique  | None  | 2          |
   |     |            | 3-Step     |           |       | 0714464080 |
   |     |            | In         |           |       |            |
   |     |            | troduction |           |       |            |
   |     |            | Kit Skin   |           |       |            |
   |     |            | Type 4     |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 1   | 607283     | CLINIQUE   | Clinique  | None  | 2          |
   |     |            | 3-Step     |           |       | 0714598983 |
   |     |            | In         |           |       |            |
   |     |            | troduction |           |       |            |
   |     |            | Kit Skin   |           |       |            |
   |     |            | Type 2     |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 2   | 607289     | CLINIQUE   | Clinique  | None  | 2          |
   |     |            | 3-Step     |           |       | 0714598976 |
   |     |            | In         |           |       |            |
   |     |            | troduction |           |       |            |
   |     |            | Kit Skin   |           |       |            |
   |     |            | Type 1     |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 3   | 607298     | NUXE       | Nuxe      | None  | 326        |
   |     |            | Prodigieux |           |       | 4680019104 |
   |     |            | Le Parfum  |           |       |            |
   |     |            | Set        |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 4   | 607305     | R5000      | None      | None  | 600        |
   |     |            | Country    |           |       | 9173975959 |
   |     |            | Ro         |           |       |            |
   |     |            | ad/Trenery |           |       |            |
   |     |            | Gift Card  |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | ... | ...        | ...        | ...       | ...   | ...        |
   +-----+------------+------------+-----------+-------+------------+
   | 95  | 607891     | 144TC      | None      | None  | 600        |
   |     |            | Cotton     |           |       | 5000602036 |
   |     |            | Blend      |           |       |            |
   |     |            | C          |           |       |            |
   |     |            | ontinental |           |       |            |
   |     |            | Pillowcase |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 96  | 607896     | Medallion  | None      | None  | 600        |
   |     |            | Embroidery |           |       | 9214948300 |
   |     |            | Quilt      |           |       |            |
   |     |            | 230x230cm  |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 97  | 607902     | Soft Touch | None      | None  | 600        |
   |     |            | Hangers 5  |           |       | 9214478456 |
   |     |            | Pack       |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 98  | 607903     | 200TC      | Studio. W | None  | 600        |
   |     |            | Cotton     |           |       | 9204812369 |
   |     |            | Flat Sheet |           |       |            |
   +-----+------------+------------+-----------+-------+------------+
   | 99  | 607905     | Satin      | None      | None  | 600        |
   |     |            | Stitch     |           |       | 9214591858 |
   |     |            | 180TC      |           |       |            |
   |     |            | Cotton     |           |       |            |
   |     |            | Blend      |           |       |            |
   |     |            | Duvet      |           |       |            |
   |     |            | Cover Set  |           |       |            |
   +-----+------------+------------+-----------+-------+------------+

   100 rows × 5 columns



|

Products can be filtered by name and brand.

.. code-block:: python

   tr.retailer_products(5, product = "coffee", brand = "nespresso")


.. container::

   +---+------------+------------+-----------+-------+------------+
   |   | product_id | product    | brand     | model | sku        |
   +===+============+============+===========+=======+============+
   | 0 | 667365     | NESPRESSO  | Nespresso | None  | 763        |
   |   |            | Essenza    |           |       | 0039618711 |
   |   |            | Mini       |           |       |            |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine    |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 1 | 667426     | NESPRESSO  | Nespresso | None  | 763        |
   |   |            | Citiz&Milk |           |       | 0054430978 |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine    |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 2 | 667654     | NESPRESSO  | Nespresso | None  | 763        |
   |   |            | Lattissima |           |       | 0047615160 |
   |   |            | Touch      |           |       |            |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine    |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 3 | 729093     | NESPRESSO  | Nespresso | None  | 763        |
   |   |            | Creatista  |           |       | 0039648893 |
   |   |            | Plus       |           |       |            |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine    |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 4 | 667815     | NESPRESSO  | Nespresso | None  | 763        |
   |   |            | Lattissima |           |       | 0039646479 |
   |   |            | One Coffee |           |       |            |
   |   |            | Machine    |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 5 | 2918572    | Creatista  | Nespresso | None  | 763        |
   |   |            | Plus       |           |       | 0039648893 |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine -  |           |       |            |
   |   |            | SILVER     |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 6 | 2918582    | Citiz&Milk | Nespresso | None  | 763        |
   |   |            | Coffee     |           |       | 0054430978 |
   |   |            | Machine -  |           |       |            |
   |   |            | WHITE      |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 7 | 2918584    | Lattissima | Nespresso | None  | 763        |
   |   |            | One Coffee |           |       | 0039646479 |
   |   |            | Machine -  |           |       |            |
   |   |            | WHITE      |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 8 | 2918599    | Essenza    | Nespresso | None  | 763        |
   |   |            | Mini       |           |       | 0039618711 |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine -  |           |       |            |
   |   |            | BLACK      |           |       |            |
   +---+------------+------------+-----------+-------+------------+
   | 9 | 2918601    | Lattissima | Nespresso | None  | 763        |
   |   |            | Touch      |           |       | 0047615160 |
   |   |            | Coffee     |           |       |            |
   |   |            | Machine -  |           |       |            |
   |   |            | SILVER     |           |       |            |
   +---+------------+------------+-----------+-------+------------+



|

Product Details
~~~~~~~~~~~~~~~

Get information on a specific product, filtering it by ID

.. code-block:: python

   tr.product(530290)

.. container::

   +---+-------+-------+-------+-------+-------+-------+-------+-------+
   |   | produ | r     | p     | pr    | brand | model | sku   | bar   |
   |   | ct_id | etail | roduc | oduct |       |       |       | codes |
   |   |       | er_id | t_url |       |       |       |       |       |
   +===+=======+=======+=======+=======+=======+=======+=======+=======+
   | 0 | 5     | 9     | http  | Ola   | None  | None  | 0     | [6001 |
   |   | 30290 |       | s://w | Rich  |       |       | 00000 | 08737 |
   |   |       |       | ww.pn | 'n    |       |       | 00000 | 8543] |
   |   |       |       | p.co. | C     |       |       | 07776 |       |
   |   |       |       | za/pn | reamy |       |       | 19_EA |       |
   |   |       |       | pstor | Ma    |       |       |       |       |
   |   |       |       | efron | gical |       |       |       |       |
   |   |       |       | t/pnp | Un    |       |       |       |       |
   |   |       |       | /en/A | icorn |       |       |       |       |
   |   |       |       | ll... | Ice   |       |       |       |       |
   |   |       |       |       | Cream |       |       |       |       |
   |   |       |       |       | 1.8l  |       |       |       |       |
   +---+-------+-------+-------+-------+-------+-------+-------+-------+

|

Product Prices
~~~~~~~~~~~~~~

Get price history data for a specific product.

.. code-block:: python

   tr.product_prices(530290)


.. container::

   === ========== ========================= ===== =============== =========
   \   product_id time                      price price_promotion available
   === ========== ========================= ===== =============== =========
   0   530290     2020-07-13T03:32:27+00:00 54.99 NaN             None
   1   530290     2020-07-10T03:35:11+00:00 54.99 NaN             None
   2   530290     2020-07-08T02:54:34+00:00 54.99 NaN             None
   3   530290     2020-07-06T15:21:13+00:00 54.99 NaN             None
   4   530290     2020-07-03T04:00:57+00:00 54.99 NaN             None
   ... ...        ...                       ...   ...             ...
   73  530290     2020-03-07T00:32:36+00:00 49.99 39.99           None
   74  530290     2020-02-22T00:31:17+00:00 49.99 NaN             None
   75  530290     2020-02-15T00:32:47+00:00 49.99 37.99           None
   76  530290     2020-02-08T00:32:37+00:00 49.99 37.99           None
   77  530290     2020-02-01T00:34:24+00:00 49.99 44.99           None
   === ========== ========================= ===== =============== =========

   78 rows × 5 columns




