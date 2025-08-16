class demo:
    a=4
o= demo()
print(o.a)  # This will print the class attribute a
o.a = 0 #instance attribute a is created
print(o.a)
print(demo.a)  # This will still print the class attribute a, which is unchanged