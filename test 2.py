from math import sin,cos

s = "((a+b)+c/sin[d]+atan2[ x+z , sin[y]]+(c+d))"


priority = {
	"+":0,
	"-":0,
	"/":1,
	"*":1,
	"^":2
}

funcs = {
	"sin":lambda x: sin(x),
	"cos":lambda x: cos(x),
	"abs":lambda x: abs(x)
}

def minDepth(s):
	depth = 0
	minDepth = None
	for c in s:
		if c ==  "(":
			depth+=1
		elif c == ")":
			depth-=1
		elif minDepth ==None or depth<minDepth:
			minDepth = depth
	return minDepth

def clearBrackets(s):
	md = minDepth(s)
	if md>0:
		return s[md:-md]
	else:
		return s


def split(s):
	s = clearBrackets(s)
	simple = True
	for c in ['+','-','*','/','^','(',')','[',']']:
		simple = simple and (c in s)
	if simple:
		return s
	else:
		minPriority = None
		minIndex = None
		depth = 0
		for i in range(len(s)):
			c = s[i]
			if c in ['(','[']:
				depth +=1
			elif c in [')',']']:
				depth -= 1
			elif depth == 0:
				if c in priority:
					if minPriority == None or priority[c]<=minPriority:
						minPriority = priority[c]
						minIndex = i

		return [s[0:minIndex],s[minIndex+1:]]


s = split(s)
print(type(s))
print(len(s))

def toEnd(args):
	print(type(args))
	print(args)
	for j in range(len(args)):
		args[j] = split(args[j])
	return args



def exp(s):
	s = split(s)
	for i in s:
		print(i)

print(toEnd(s))