if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    distinctscores = []
    for k in scores:
        if k not in distinctscores:
            distinctscores.append(k)
            
    distinctscores.sort()
    print(distinctscores)
    secondLow = distinctscores[1]
    names = []
    for i in range(len(students)):
        if students[i][1] == secondLow:
            names.append(students[i][0])
            
    names.sort()
    for j in names:
        print(j)
