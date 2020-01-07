# Approach the problem with a generator of multiples (up to a high bound, for simplicity)
#
# This could be further extended with:
# - an infinite generator
# - 

def generate_multiples(factors, high_bound):
    """ Generate values that are multiple of any of the given factors,
    up to the high_bound (excluded) """

    for n in range(min(factors), high_bound):
        if any(map(lambda x: n % x == 0, factors)):
            yield n
    return

def main():
    multiples_3_5 = generate_multiples([3, 5], 10)
    print(f'Sum to 10: {sum(multiples_3_5)}')

    multiples_3_5 = generate_multiples([3, 5], 1000)
    print(f'Sum to 1000: {sum(multiples_3_5)}')

if __name__ == '__main__':
    main()
