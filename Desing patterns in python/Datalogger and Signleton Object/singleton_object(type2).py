class Singleton_object():
    def __new__(cls):
        if not hasattr(cls, instance):
            cls.instance = super().__new__(cls)
        return cls.instance

s1 = Singleton_object()
print('s1 is : ', s1)

s2 = Singleton_object()
print('s2 is :' , s2)
