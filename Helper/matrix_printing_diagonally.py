'''
author : https://github.com/Harnek'''

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12],
     [13,14,15,16],]

r = 4
c = 4

#Diagonally Up
'''
1 
5 2 
9 6 3 
13 10 7 4 
14 11 8 
15 12 
16 
'''
for i in range(r + c - 1):
    k1 = 0 if i < c else i - c + 1
    k2 = 0 if i < r else i - r + 1
    for j in range(i - k2, k1-1, -1):
        print(a[j][i-j], end=" ")
    print()

print()

#Diagonally Down
'''
13 
9 14 
5 10 15 
1 6 11 16 
2 7 12 
3 8 
4 
'''
for i in range(r + c - 1):
    k1 = 0 if i < c else i - c + 1
    k2 = 0 if i < r else i - r + 1
    for j in range(i - k2, k1-1, -1):
        print(a[r-j-1][i-j], end=" ")
    print()


'''Also try
Easier to print by understanding the pattern

Observing the pattern::
+-------------------------+---------------------------+
|   1  2  3  4            |            1  2  3  4     |
|      5  6  7  8         |         5  6  7  8        |
|         9  10 11 12     |      9  10 11 12          |
|            13 14 15 16  |   13 14 15 16             |
+-------------------------|---------------------------+
Just add blank spaces and print vertically 
'''
