age = int(input("INPUT YOUR AGE : "))

if age <= 15:
    print("Mstr. / Miss")
else:
    print("Mr. / Ms.")
    
print("<---------- END PROGRAM ---------->")
    
if age >= 15:
    print("Mr. / Ms.")
else:
    print("Mstr. / Miss")
    
print("<---------- END PROGRAM ---------->")

# --------------- AND --------------- #

if age <= 15:
    print("1")
if age <= 20:
    print("2")
if age <= 30:
    print("3")
else:
    print("4")

# --------------- OR --------------- #

if age <= 15:
    print("1")
elif age <= 20:
    print("2")
elif age <= 30:
    print("3")
else:
    print("4")