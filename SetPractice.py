sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]



print(sampleSet.union(sampleList))

print("Excercise 2")

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

print("Excercise 1")

set3 = {10, 20, 30}
set4 = {20,40,50}

print(set3.difference(set3.intersection(set4)))

print("Excercise 2")
set5= {10,20,30,40,50}
print(set5.difference({10,20,30}))

print("Excercise 3")
set6 = {10,20,30,40,50}
set7 ={60, 70, 80, 90, 10}

if(set6.isdisjoint(set7)):
    print("Not element existed in a both table")
else:
    print(set6.intersection(set7))

print("Excercise 4")
set8 = {10,20,30,40,50}
set9 = {30,40,50,60,70}
setx = set8.difference(set8.intersection(set9)).union(set9.difference(set8.intersection(set9)))
print(setx)
setXI = set8.copy()
setXII = set9.copy()
setXI.symmetric_difference_update(setXII)
print(setXI)


print("Excercise 5")
print(set8.difference(set8.difference(set8.intersection(set9))))
setXIII = set8.copy()
setXIV = set9.copy()
setXIII.intersection_update(setXIV)
print(setXIII)




