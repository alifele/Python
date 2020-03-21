class Test():
    _shared_state =   {}
    def __init__(self):
        self.x = 12
        self.__dict__ = self._shared_state
        pass



test = Test()
test.x = 132

test2 = Test()

print(test.__dict__)
print(test2.__dict__)
