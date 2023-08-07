def swap_case(s):
    lis = []
    for i in s:
        if i.isupper() == True:
            lis.append(i.lower())
        elif i.isupper() == False:
            lis.append(i.upper())

    return "".join(lis)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)