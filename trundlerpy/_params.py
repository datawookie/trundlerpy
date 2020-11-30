parameters = {
  'retailer': {
    'req_params': {},
    'req_or_params': {},
    'opt_params': {
      'id': int
    }
  },
  'retailer_products': {
    'req_params': {
      'id': int
    },
    'req_or_params': {},
    'opt_params': {
      'limit': int,
      'offset': int,
      'regex': bool,
      'ignore_case': bool,
      'product': str,
      'brand': str,
      'sku':str,
      'head': bool
    }
  },
  'product': {
    'req_params': {
      'id': int
    },
    'req_or_params': {},
    'opt_params': {}   
  },
  'products': {
    'req_params': {},
    'req_or_params': {},
    'opt_params': {
      'limit': int,
      'offset': int,
      'regex': bool,
      'ignore_case': bool,
      'product': str,
      'brand': str,
      'barcode': str,
      'sku':str
    }
  },
  'product_prices': {
    'req_params': {
      'id': int
    },
    'req_or_params': {},
    'opt_params': {
      'limit': int,
      'offset': int
    }
  }
}