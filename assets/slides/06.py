# Lecture 06: Functional Abstraction

def is_even(x):
    return x % 2 == 0
val = is_even(2)  # True

if val == True:
    print("In True block")
else:
    print("In False block")

if val:
    print("In True block")
else:
    print("In False block")

if bool(val):
    print("In True block")
else:
    print("In False block")

def check_is_true(x):
    if x:
        print(f"x is a True value: {x}")
        return True
    else:
        print(f"x is a False value: {x}")
        return False

print(check_is_true(True))
print(check_is_true(False))
print(check_is_true(1))
print(check_is_true(0))
