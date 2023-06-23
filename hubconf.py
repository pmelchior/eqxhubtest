dependencies = ['equinox']
import equinox as eqx
from eqxhubtest import WhatEver as _WhatEver

def test():
    model = _WhatEver()
    url = "https://hub.pmelchior.net/test.eqx"
    file = hub.get_leave_file_from_url(url)
    filter_spec = lambda f,x: (
        str(f.read(), 'utf-8') if isinstance(x, str) else eqx.default_deserialise_filter_spec(f,x)
    )
    model_loaded = eqx.tree_deserialise_leaves(file, model, filter_spec=filter_spec)
    return model_loaded
