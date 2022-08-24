n= {int(i) for i in range(1,70)}
le = {int(i) for i in range(1,13)}
#print(n)

absentees1 = []
absentees2 = []
print("Enter the roll numbers of presentees: ")

presentees = set(int(i) for i in input().split())
print( "Enter the roll number of LEs : ")

lep = set(int(i) for i in input().split())

for i in n.difference(presentees):
    absentees1.append(i)
    
for i in le.difference(lep):
    absentees2.append(i)
    
sorted(absentees2)
sorted(absentees1)

print("AI&DS : Absentees ")
print(absentees1 )
print(absentees2 )
