class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            # super()works even if there is no explicit base class listed.
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)
