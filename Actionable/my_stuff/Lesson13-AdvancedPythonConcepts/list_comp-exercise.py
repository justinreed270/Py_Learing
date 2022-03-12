
def perm():
    roll_dice = [
        (a, b, c, d, e)
        for a in range(1,7)
        for b in range(1,7)
        for c in range(1,7)
        for d in range(1,7)
        for e in range(1,7)
    ]
    return len(roll_dice)

def comb():
    roll_dice = [
        (a, b, c, d, e)
        for a in range(1,7)
        for b in range(a,7)
        for c in range(b,7)
        for d in range(c,7)
        for e in range(d,7)
    ]
    return len(roll_dice)


def main():
    print(f'permutations (where order matter: {perm()}')
    print(' ')
    print(f'combinations (where order does NOT matter: {comb()}')




if __name__=='__main__':
    main()
