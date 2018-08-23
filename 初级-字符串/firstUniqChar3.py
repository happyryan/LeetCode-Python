def firstUniqChar(s):
	dchar = dict()
	for c in s:
		if c in dchar:
			dchar[c] = dchar[c] + 1
		else:
			dchar[c] = 1

	for i in range(len(s)):
		if dchar[s[i]] == 1:
			return i
			break
	
	return -1

str = 'helloh'
print(firstUniqChar(str))
