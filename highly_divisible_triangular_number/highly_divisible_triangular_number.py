import itertools
import sys


def calc_triangle_number(number):
    return sum([i for i in range(1, number + 1)])


def calc_factors(number, type_func=int):
    # unittests expects interger items and for app itself str items are easier to format
    return [type_func(i) for i in range(1, number + 1) if number % i == 0]


def find_first_triangle_with_at_least_divisors(number, type_func=int):
    for i in itertools.count():
        factors = calc_factors(i, type_func)
        if len(factors) == number:
            return i, factors


def write_file(path, result):
    with open(path, 'w') as f:
        f.write(result)


def print_1(number):
    term = calc_triangle_number(number)
    result = '{}: {}'.format(
        term,
        ','.join(calc_factors(term, type_func=str)))
    print result
    write_file('Divisors_and_sum_of_{}th_term.txt'.format(number), result)


def print_2(number):
    term, divisors = find_first_triangle_with_at_least_divisors(number, type_func=str)
    divisors_string = ','.join(divisors)
    print 'The triangle number is {} and divisors are {}'.format(
        term, divisors_string)
    write_file(
        'The_first_triangle_number_{}.txt'.format(number),
        '{}: {}'.format(term, divisors_string))


def _ask_positive_number(prompt):
    try:
        number = int(raw_input(prompt))
    except ValueError:
        print 'Bad value'
        return False
    if number <= 0:
        print 'Give positive number'
        return False
    return number


def menu():
    print (
        'Options: \n'
        '1) Print triangle number and factors for given ordinal\n'
        '2) Print the first triangle number and factors for at least given amount of factors\n'
        'q) Quit\n'
    )
    while True:
        opt = raw_input('> ')
        if opt == 'q':
            sys.exit()
        if opt == '1':
            number = _ask_positive_number('Give the ordinal number: ')
            if not number:
                continue
            print_1(number)
        if opt == '2':
            number = _ask_positive_number('Give the number of divisors: ')
            if not number:
                continue
            print_2(number)


if __name__ == '__main__':
    menu()
