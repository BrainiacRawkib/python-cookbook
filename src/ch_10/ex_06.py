# reloading modules
from ex_05_foo_package.foo_package.spam import blah
import imp

imp.reload(blah)
