class demo:
    a = 4

o = demo()
print(o.a) # prints the class attribute because instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a)# Print the instance attribute because instance attribute is present
print(demo.a)
