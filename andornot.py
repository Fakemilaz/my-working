# and
# or
# not

a , b , c , d = 10 , 20 , 30 , 10

# AND
print(a > b and a == b) # False False = Flase
print(a < b and a == b) # True False = Flase
print(a < b and a == d) # True True = True

# OR
print(a > b or a == b) # False False = Flase
print(a < b or a == b) # True False = True
print(a < b or a == d) # True True = True

# NOT
print(a != d) # False
