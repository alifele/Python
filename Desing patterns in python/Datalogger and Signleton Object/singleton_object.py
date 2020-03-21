class Singleton_object(object):
    class __Singleto_object():
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r}{1}".format(self, self.val)


    instance = None


    def __new__(cls):
        if not Singleton_object.instance:
            Singleton_object.instance = Singleton_object.__Singleto_object


        return Singleton_object.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
        








test = Singleton_object()
#print(test.__str__())


class Test():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "{}".format('hello there it is the print of the class')


test = Test(177)
print(test)
