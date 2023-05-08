try:

    def product(a, b):
        return a / b

    a, b = input().split()
    a, b = int(a), int(b)
    res = product(a, b)
    print(res)

except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")
except:
    print("Something went worng")
