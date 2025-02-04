class Repository:
    def notfound(func):
        def wrapper(*args, **kwargs):
            return DoesNotExist(func(*args, **kwargs))

        class DoesNotExist:
            def __init__(self, data):
                self.data = data

            def NotFound(self, exception_class):
                if self.data is None:
                    raise exception_class
                return self.data
            
        return wrapper