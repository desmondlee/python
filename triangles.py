# -*- coding:utf-8 -*-

def triangles():
	L = [1]
	while True:
		yield L
		L = [ L[x]+L[x+1] for x in range(len(L)-1) ]
		L.insert(0,1)
		L.append(1)

n = 0
for t in triangles():
	print(t)
	n = n +1
	if n == 10:
		break