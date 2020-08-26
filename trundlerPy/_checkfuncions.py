import requests
import json


# Check params functions -------------------------------------------------------

class Error(Exception):
    """Base class for other exceptions."""

    pass


class RequiredArgMissing(Error):
    """Raised when a required argument is missing."""
    
    pass


def check_params(req_params, opt_params, args):
    """Describe this method here."""
    params = {}
    # Check required params
    if req_params is not None:
        for key in req_params:
            if key not in args:
                raise RequiredArgMissing(f"Required argument '{key}' is missing.")
            else:
                assert isinstance(args[key], req_params[key]), f"'{key} type must be {req_params[key]}."
            params.update({key: args[key]})
            del args[key]

    # Check optional params
    if args is not None:
        for key in args:
            if key not in opt_params:
                raise TypeError(f"'{key}' is not supported")
            else:
                assert isinstance(args[key], opt_params[key]), f"'{key}' type must be {opt_params[key]}."

            params.update({key: args[key]})

    return params


# Check API functions ---------------------------------------------------------

def check_response(response):
    try:
        response = response
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:

        print(err, '\n', json.loads(response.text)['message'] )

        raise SystemExit()
