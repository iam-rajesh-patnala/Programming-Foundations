CP = int(input())
SP = int(input())

profit = SP > CP
loss = SP < CP
equal = SP == CP

if profit:
    print("Profit")
elif loss:
    print("Loss")
elif equal:
    print("No Profit - No Loss")
