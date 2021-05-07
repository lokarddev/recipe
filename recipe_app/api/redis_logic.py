import redis


class Click:
    """
    This class avoids more boilerplate code in mutations, types and instantiate an object to get access to all uses of
    data manipulation with redis
    """
    _instance = None

    def __new__(cls):
        """
        The goal is to have only one endpoint to all methods.
        Thus here is simple implementation of singleton design pattern
        """
        if cls._instance is None:
            cls._instance = super(Click, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def incr_click(self):
        """Incrementing click amount"""
        return self.r.incr('click', 1)

    def get_click(self):
        """Click amount"""
        if not self.r.get('click'):
            return 0
        return self.r.get('click')

    def reset_click(self):
        """Drop down click count"""
        return self.r.delete('click')


click = Click()
