'''
You are given a binary string S.
You can perform the following operations on S any number of times (possibly zero):
    • Select an index i such that S[i] is equal to 1 and 
        S[i+1] is equal to 0 for 0 ≤ i < len(S) -1.
    • Remove exactly one of the character from S.

Find the smallest string S that you can get after performing operations on S.
'''

num= input()
i=0

while(i<len(num)-1):
    if num[i]=='1' and num[i+1]=='0':
        num = num[:i] + num[i+1:]
        i=0
    else:
        i+=1
print(num)
