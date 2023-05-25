"""def diff(a, b, energy):
    flag = 1
    if a > b:
        val = (a - b)
        for i in range(val):
            flag *= energy
        print(flag)
    elif a == b:
        print(flag)
    else:
        val = (b - a)
        for i in range(val):
            flag *= energy
        print(flag)


a, b = map(int, input().split())
energy = 32

diff(a, b, energy)"""

def get_the_amount_of_energy(magnitude_a, magnitude_b):
    magnitudes_difference = magnitude_a - magnitude_b
    amount_of_energy = 32 ** magnitudes_difference
    return amount_of_energy

def main():
    magnitude_a, magnitude_b = input().split()
    magnitude_a, magnitude_b = int(magnitude_a), int(magnitude_b)
    amount_of_energy = get_the_amount_of_energy(magnitude_a, magnitude_b)
    print(amount_of_energy)

main()