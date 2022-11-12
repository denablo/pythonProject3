try:
    print("start code")
    print()
    print("no error")
except NameError:
    print("we have an error")
except ZeroDivisionError:
    print("we have an ZeroDivisionError")

print("code after capsule")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError) as error:
    print(error)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    try:
        print("start code")
        print(dinisik)
        print("no errors")
    except SyntaxError:
        print("Wrong syntax")
except NameError as dinisik:
    print(dinisik)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    try:
        print("start code")
    print(dinisik)
    print("no errors")
except NameError as dinisik:
    print(dinisik)

else:
    print("I am ELSE")
finally:
    print("КІНЕЦЬ!!!")