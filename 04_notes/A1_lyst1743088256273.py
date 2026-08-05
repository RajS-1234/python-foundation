print("Enter few numbers separated by comma")
s=input()
# s='10,34,21,56,78,45,50'
l1=s.split(',')
# l1 = ['10','34','21',56','78','45','50']
l2=[]
for x in l1:
    l2.append(int(x))

# l2=[10,34,21,56,78,45,50]

l2=[int(x) for x in input("Enter few numbers separated by comma").split(',')]
