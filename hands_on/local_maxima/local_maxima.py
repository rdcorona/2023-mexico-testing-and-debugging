
def local_maxima(x):
    idx = []
    num1 = num2 = float('-inf')
    idx1 = idx2 = None
    for i, num in enumerate(x):
        if num > num1:
            num2 = num1
            idx2 = idx1
            num1 = num
            idx1 = i
        elif num > num2:
            num2 = num
            idx2 = i
    idx.append(idx1)
    idx.append(idx2)
    return idx

if __name__ == "__main__":
    print(local_maxima([1,3,-2,0,2,1]))
