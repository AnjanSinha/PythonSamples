def count_substring(string, sub_string):
    count = 0
    iterable_length = len(string)-(len(sub_string)-1)
    for i in range(0,iterable_length):
        if (string[i:(i+len(sub_string))]) == sub_string:
            count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)