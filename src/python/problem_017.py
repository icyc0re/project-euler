numbers = '_ one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')
tens = '_ ten twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')

def wordify(value):
    if value < 20:
        return numbers[value]
    elif value < 100:
        res = tens[value // 10]
        rest = wordify(value % 10)
        if '_' not in rest:
            res += f'-{rest}'
        return res
    elif value < 1000:
        res = numbers[value // 100] + ' hundred'
        rest = wordify(value % 100)
        if '_' not in rest:
            res += f' and {rest}'
        return res
    else:
        return 'one thousand'

def euler_017():
    count_letters = lambda s: len([c for c in s if c.isalpha()])
    letters = [count_letters(wordify(n)) for n in range(1, 1001)]
    return sum(letters)

if __name__ == '__main__':
    print(euler_017())
