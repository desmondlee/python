# -*- coding:utf-8 -*-

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b)
		yield b
		a, b = b, a+b
		n = n+1
	return 'done'
	

g = fib(6)
while True:
	try:
		x = next(g)
		print(x)
	except StopIteration as e:
		print(e.value)
		break