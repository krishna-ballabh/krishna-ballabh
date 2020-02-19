l=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
y=[]
for i in l:
	if len(i)!=0:
		y.append(i)
print(y)
		
