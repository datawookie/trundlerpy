parameters = {
  'retailer': {
    'req_params': {},
    'opt_params': {
      'id': int
    }
  },
  'retailer_products': {
    'req_params': {
      'id': int
    },
    'opt_params': {
      'limit': int,
      'offset': int,
      'regex': bool,
      'ignore_case': bool,
      'product': str,
      'brand': str,
      'head': bool
    }
  },
  'product': {
    'req_params': {
      'id': int
    },
    'opt_params': {}
  },
  'products': {
    'req_params': {},
    'opt_params': {
      'limit': int,
      'offset': int,
      'regex': bool,
      'ignore_case': bool,
      'product': str,
      'brand': str,
      'barcode': str
    }
  },
  'product_prices': {
    'req_params': {
      'id': int
    },
    'opt_params': {
      'limit': int,
      'offset': int
    }
  }
}