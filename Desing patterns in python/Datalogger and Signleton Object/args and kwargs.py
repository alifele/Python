def test(arg1, *args, **kwargs):
    print(arg1)

    for arg in args:
        print(arg)

    for val in kwargs.values():
        print(val)

keys = {'a':2, 'b':3,'d':4, 'e':5}
test('ali',123,21,14,45, keys)
