#!/bin/python3
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    s = list(s)
    ost = []
    open_brackets = ('{', '[', '(')
    close_brackets = ('}', ']', ')')
    while len(s) > 0 :
        if len(ost) == 0:
            if s[0] in close_brackets:
                return 'NO'
            elif s[0] in open_brackets:
                ost.append(s.pop(0))
                
        elif len(ost) > 0:
            if s[0] in open_brackets:
                ost.append(s.pop(0))
            elif s[0] in close_brackets:
                for i,e in enumerate(open_brackets):
                    if ost[-1] == e and s[0] != close_brackets[i]:
                        return 'NO'
                    elif ost[-1] == e and s[0] == close_brackets[i]:
                        ost.pop(-1)
                        s.pop(0)
                        break
                        
    if len(ost) > 0:
        return 'NO'
    else:
        return 'YES'
            
            
            
            
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
