'''
超出时间限制
'''
def firstUniqChar(s)


        if len(s) == 0:
            return -1
        else:
            for i in range(len(s)):
                if s.count(s[i]) == 1:
                    return i
                    break
                else:
                    if i == len(s) - 1:
                        return -1


print(firstUniqChar("hheell"))