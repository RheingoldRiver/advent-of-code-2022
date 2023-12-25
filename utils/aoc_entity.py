class AOCEntity:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        properties = ', '.join(f'{key}={repr(value)}' for key, value in self.__dict__.items())
        return f'<{self.__class__.__name__}: {properties}>'
