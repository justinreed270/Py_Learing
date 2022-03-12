def main():
    with open('states.txt') as f:
        states = f.read().splitlines()
    
    print(f'The file contains {len(states)} states.')

main()
