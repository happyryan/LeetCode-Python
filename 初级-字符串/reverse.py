'''
执行用时：64 ms
'''

def reverse(i):
        if str(i)[0] != '-':
                s = ''.join(reversed(str(i)))
                newi = int(s)
        else:
                s = ''.join(reversed(str(i)[1:]))
                newi = int('-' + s)
        
        if newi > 2**31 -1 or newi < -2**31:
                return 0
        else:
                return newi
