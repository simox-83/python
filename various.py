def length (s):
	count=0
	for c in s:
		count +=1
	print count

def frequency (s):
	d=dict()
	for c in s:
		if c in d:
			d[c]+=1
		else:
			d[c]=1
	return d


def firstlast2 (s):
	if len(s) < 2 :
		return ''
	else:
		return s[:2]+ s[-2:]

def overlap (l,m):
	r=list()
	for num in l:
		if num in m:
				r.append (num)
	return r


def palindrome ():
	inputString = input ('Give me a string: ')
	j=len(inputString)-1
	for i in range (0,j):
		if (inputString[i]!=inputString[j]):
			return False
		else:
			i=i+1
			j=j-1
	print ('Yes it is')
	return True


def comprehensions (a):
	l=[n for n in a if n%2==0]
	print l
	return l

def isPrime (n):
	if hasDivisors(n) is True:
		return False
	return True

def hasDivisors(n):
	for i in range (2,n-1):
		if (n%i==0):
			return True
	return False

def listEnds (l):
	if (len(l)==1):
		return l
	m=[l[n] for n in (0,-1)]
	return m


def noDuplicates (l):
	m=[]
	for x in l:
		if x not in m:
			m.append (x)
	return m


# Positional parameters

def makePizza (size, *toppings):
	print size,toppings

def make_car (manufacturer, model, **info):
	d={}
	d['man'] = manufacturer
	d['mod'] = model
	for k,v in info.items():
		d[k] = v
	return d


def main():
	car = make_car('ferrari', 'f2017', pilot='sebastian vettel', position='first')
	print car
	#l=[5,3,8,3,9,5]
	#print noDuplicates(l)
	#number=int(input('Give me a number: '))
	#print (isPrime(number))


if __name__== '__main__':
	main()


