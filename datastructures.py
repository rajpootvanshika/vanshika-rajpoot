#data structures
#1. square brackets -> list[]
#2. heterogenous data structure(a list can store diff type of data type)
#list allow storing duplicate values.
#list are ordered bcz they have indexing and indexing starts from 0.
#list are mutable.
#marks =[] #empty list
# marks=[80,78,90,65,88,87,75,"abhishek",3.14]
# marks[3]="modiji"
# marks(marks[3])

#traversing
# a=[10,20,30,40,50]
# for i in a:
#     print(i)

#methods in list
# 1. .append()add the only single value at the last of list.
marks =[10,20,30,40,50]
marks.append(90)
print (marks)

#2. .extend(){takes muktiple value}
marks2=[70,80,90]
marks.extend(marks2)
marks2.extend(marks)
print(marks2)

#3. .insert(index,value){takes only 2 values }
marks.insert(6,90)
print(marks)


