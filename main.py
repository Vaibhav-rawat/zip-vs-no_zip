#This program extracts bigger number between two list
'''Author - Vaibhav Rawat
Purpose - Python problem solveing'''
l1=[1,4,3,8,5]
l2=[2,3,6,10,10]

#without list comprehension and indexing
l3=[]
for i in range(len(l1)):
    if l1[i]>l2[i]:
        l3.append(l1[i])
    else:
        l3.append(l2[i])
print(l3)

#with list comprehension and indexing
l4=[l1[i] if l1[i]>l2[i] else l2[i] for i in range(len(l1))]
print(l4)

#with zip without list comprehension
l5=[]
for pair in zip(l1,l2):
    l5.append(max(pair))
print(l5)

#with list comprehension and zip - this really reduces the code length by using max()
l6=[max(pair) for pair in zip(l1,l2)]
print(l6)
