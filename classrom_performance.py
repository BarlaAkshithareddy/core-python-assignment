def average(values):
  avg_list=[]
  for i in values:
    sum_values=0
    sum_values=sum(i)
    avg=sum_values/len(i)
    av1=round(avg,2)
    avg_list.append(av1)
  return avg_list
students=eval(input("students = "))
marks=list(students.values())
res=average(marks)
names=list(students.keys())
output=dict(zip(names,res))
maximum_avg=max(output,key=output.get)
print("Average Marks: ",output)
print("Top performer: ",maximum_avg)