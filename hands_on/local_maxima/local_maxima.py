# import numpy as np

# def local_maxima2(x):
#     """Find local maxima of x.

#     Input arguments:
#     x -- 1D list of real numbers


#     Output:
#     idx -- list of indices of the local maxima in x
#     """
#     idx=np.argmax(x)
#     x[idx]=np.min(x)-1
#     idx=np.argmax(x)

#     return [idx, idx2]


# def local_maxima(x):
#     """Find local maxima of x.

#     Input arguments:
#     x -- 1D list of real numbers


#     Output:
#     idx -- list of indices of the local maxima in x
#     """
#     a=[]


#     for i in range(len(x)):
#         if x[i-1]<x[i]>x[i+1]:
#             a+=[i]
#     #x[idx]=np.min(x)-1
#     #idx=np.argmax(x)}

#     print(a)

#     return a#[idx, idx2]


# #print(local_maxima([1,3,-2,0,2,1]))
# local_maxima([1,2,2,3,1])

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
