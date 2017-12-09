def find_max(seznam):
    max_value = max(seznam)
    max_index = seznam.index(max_value)
    return(max_index, max_value)

def redistribution(seznam):
    max_index, max_value = find_max(seznam)
    delka = len(seznam)
    seznam[max_index] = 0
    for i in range(max_value):
        seznam[(max_index + 1 + i) % delka] += 1
    return(seznam)



if __name__ == "__main__":
    with open('vstup06') as f:
        vstup0 = f.read()
    vstup = list(map(int, vstup0.split('\t')))
    print(vstup)
    print()
    seznam = []
    for i in range(10):
        vstup1 = redistribution(vstup)
        print(vstup1)
        seznam.append(vstup1)
        print(seznam)
        vstup = vstup1

    print(seznam)