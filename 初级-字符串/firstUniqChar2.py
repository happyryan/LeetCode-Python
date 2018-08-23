import collections

def firstUniqChar(s):
	ans = -1

	c = collections.Counter(s)

	for i, j in enumerate(s):
		if c[j] == 1:
			return i
			break


s = 'gong'
a = firstUniqChar(s)
print(a)
		
