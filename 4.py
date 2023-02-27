# [4]Matrix Determinant
def determinant(matr):
    if len(matr) == 1:
        return matr[0][0]
    elif len(matr) == 2:
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
    else:
        new_matrixs = list()

        for itemRow in range(len(matr)):
            matr_deter = list()
            for itemCol in range(len(matr[0])):
                a = list(matr[itemCol])
                a.pop(itemRow)
                matr_deter.append(a)

            matr_deter.pop(0)
            new_matrixs.append(matr_deter)

    return sum([(-1)**i*matr[0][i]*determinant((new_matrixs[i])) for i in range(len(new_matrixs))])

# [4]Range Extraction
def solution(args):
    string = ""
    count = 1
    index = 0
    mas = list()
    a = 1

    for i in range(len(args)):

        if i >= index:
            for j in range(i+1, len(args)):
                if args[i] + 1*a == args[j]:
                    count = count + 1
                    a += 1
                    continue
                else:
                    break

            index = i + count
            mas.append([i, i + count - 1])
            count = 1
            a = 1

    for item in mas:
        if item[1] - item[0] == 1:
            string += f"{args[item[0]]},{args[item[1]]},"
        elif item[1] - item[0] == 0:
            string += f"{args[item[0]]},"
        else:
            string += f"{args[item[0]]}-{args[item[1]]},"

    return string[0:len(string)-1]
