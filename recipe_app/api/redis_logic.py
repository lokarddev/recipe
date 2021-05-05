import redis


class Click:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def __init__(self):
        pass

    @classmethod
    def incr_click(cls):
        return cls.r.incr('click', 1)

    @classmethod
    def get_click(cls):
        if not cls.r.get('click'):
            return 0
        return cls.r.get('click')

    @classmethod
    def reset_click(cls):
        return cls.r.delete('click')
