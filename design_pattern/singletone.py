""" Singleton Pattern

インスタンスが一つしか存在しないことを保証する。

"""


class Singleton(object):
    _singleton = None

    @classmethod
    def get_instance(cls):
        if cls._singleton is None:
            cls._singleton = cls()

        return cls._singleton


if __name__ == "__main__":
    obj1 = Singleton.get_instance()
    obj2 = Singleton.get_instance()

    print(f"The id of obj1: {id(obj1)}")
    print(f"The id of obj2: {id(obj2)}")

    print(f"obj1 is obj2: {obj1 is obj2}")

    # This is not perfect since we can build instance with normal way.
    obj3 = Singleton()
    print(f"The id of obj3: {id(obj3)}")
