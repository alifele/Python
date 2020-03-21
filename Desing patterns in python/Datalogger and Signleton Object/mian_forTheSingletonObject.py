from singleton_object import Singleton_object

sng_ob1 = Singleton_object()

sng_ob1.val = 12

print(sng_ob1.val)

sng_ob2 = Singleton_object()

sng_ob1.val = 14

print(sng_ob1.val)
print(sng_ob2.val)
