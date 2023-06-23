import equinox as eqx
from eqxhubtest import WhatEver

we = WhatEver(1, 2, "test")


filter_spec = lambda f,x: (
     f.write(bytes(x, 'utf-8')) if isinstance(x, str) else eqx.default_serialise_filter_spec(f,x)
)
eqx.tree_serialise_leaves("test.eqx", we, filter_spec=filter_spec)
