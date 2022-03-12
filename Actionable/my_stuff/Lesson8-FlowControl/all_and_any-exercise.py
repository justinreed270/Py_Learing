def all_true(iterable):
    t = set(iterable)
    count = len(t)
    if count >= 2:
        return False
    else:
        return True


def any_true(iterable):
    t = set(iterable)
    count = len(t)
    if count == 2:
        return False
    else:
        return True


def main():
    a = all_true([1, 0, 1, 1, 1])
    b = all_true([1, 1, 1, 1, 1])
    c = any_true([0, 0, 0, 1, 1])
    d = any_true([0, 0, 0, 0, 0])

    print(a, b, c, d) # Should be: False True True False

main()
