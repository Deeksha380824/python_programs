m1=int(input("enter the 1 subject marks"))
m2=int(input("enter the 2 subject marks"))
m3=int(input("enter the 3 subject marks"))
m4=int(input("enter the 4 subject marks"))
average=(m1+m2+m3+m4)/4
print("average")
if average>91 and average<=100:
  print("grade A")
elif average>81 and average<=90:
  print("grade B")
elif average>71 and average<=80:
  print("gradeC")
elif average>61 and average<=70:
  print("grade D")
elif average>=1 and average<=60:
  print("grade F")