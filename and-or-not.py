# and
# or
# not

a , b , c , d = 10 , 20 , 30 , 10

# AND                   #   1   |   2  | Result
print(a > b and a == b) # False False = Flase
print(a < b and a == b) # True False = Flase
print(a < b and a == d) # True True = True

# OR                   #   1   |   2  | Result
print(a > b or a == b) # False False = Flase
print(a < b or a == b) # True False = True
print(a < b or a == d) # True True = True

# NOT
print(a != d) # False

z = (10>5) or (10==5)
print(not z) # Let's Try
