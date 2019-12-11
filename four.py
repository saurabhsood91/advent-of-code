MIN = 254032
MAX = 789860


def in_range(num):
    return num >= MIN and num <= MAX


def ltr_does_not_decrease(num):
    digits = [int(char) for char in str(num)]
    prev = digits[0]
    for digit in digits[1:]:
        if digit < prev:
            return False
        prev = digit
    return True


def contains_double(num):
    digits = [int(char) for char in str(num)]
    prev = digits[0]
    for digit in digits[1:]:
        if digit == prev:
            return True
        prev = digit
    return False


def is_valid_password(num):
    return in_range(num) and ltr_does_not_decrease(num) and contains_double(num)


def tests_ltr_does_not_decrease():
    assert ltr_does_not_decrease(223450) == False


def tests_contains_double():
    assert contains_double(123789) == False


def test_is_valid_password():
    assert is_valid_password(111111) == True


def find_number_of_passwords_in_range():
    n_valid_passwords = 0
    for num in range(MIN, MAX + 1):
        if is_valid_password(num):
            n_valid_passwords += 1
    return n_valid_passwords


if __name__ == '__main__':
    tests_contains_double()
    tests_ltr_does_not_decrease()
    # test_is_valid_password()
    print(find_number_of_passwords_in_range())
