import equinox as eqx
from eqxhubtest import WhatEver as _WhatEver

model = _WhatEver()
file = "test.eqx"


filter_spec = lambda f,x: (
      str(f.read(), 'utf-8') if isinstance(x, str) else eqx.default_deserialise_filter_spec(f,x)
)
model_loaded = eqx.tree_deserialise_leaves(file, model, filter_spec=filter_spec)
print (model_loaded)
