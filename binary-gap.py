# soal
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647

def solution(N):
    # write your code in Python 3.6
    denary = N
    binery = 0
    longest_gep = 0
    start = False
    gep = 0
    cek = []
    while(denary > 0):
        binery = denary%2
        cek.append(binery)
        denary = denary//2
        if(binery == 1):
            start = True
            if(gep > 0):
                # start = False    
                gep+=1
                # normalization
                gep = gep-2
                # normalitation
                print("gep now = "+str(gep))
                print("longest gep = "+str(longest_gep))
                if(gep > longest_gep):
                    longest_gep = gep
                gep = 0

        if(start):
            gep+=1

    print(cek)
    print(longest_gep)
    pass

if __name__ == '__main__':
    t = int(input())
    solution(t)