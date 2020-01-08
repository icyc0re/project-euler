def is_palindrom(n):
    s = str(n)
    return s == s[::-1]

def euler_004():
    highest = 0
    for a in range(100, 999):
        for b in range(a + 1, 1000):
            n = a * b
            if n > highest and is_palindrom(n):
                highest = n
    return highest

if __name__ == '__main__':
    print('Highest: {}'.format(euler_004()))