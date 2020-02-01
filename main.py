def check_valid(email):
    return True

n=int(input())
l=[]
for i in range(n):
    l.append(raw_input())

l = list (filter(lambda x: check_valid(x),l))
