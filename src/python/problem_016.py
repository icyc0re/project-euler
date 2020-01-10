def easy_016(exponent):
    value = 2 ** exponent
    return sum(map(int, str(value)))

def euler_016(exponent):
    digits = [1]
    for _ in range(exponent):
        # square all digits
        digits = [d * 2 for d in digits]
        # then report all carrys
        for i, d in enumerate(digits):
            if d > 9:
                digits[i] = d % 10
                if len(digits) > i+1:
                    digits[i+1] += d // 10
                else:
                    digits.append(d // 10)
    return sum(digits)

if __name__ == '__main__':
    print(easy_016(1000))
    print(euler_016(1000))
