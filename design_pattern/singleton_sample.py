""" The better idea of singleton pattern.
ref: https://blog.bitmeister.jp/?p=4806

インスタンス生成時の __new__() メソッドを変更することで、インスタンスの生成を制御
"""


class Singleton(object):
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton == super(Singleton, cls).__new__(cls)

        return cls._singleton


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()

    print(id(obj1))
    print(id(obj2))
    print(obj1 is obj2)
