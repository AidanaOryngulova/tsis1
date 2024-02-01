#ex1
print(bool("Hello"))
print(bool(15))

#ex2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#ex3
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#ex4
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#ex5
def myFunction() :
  return True

print(myFunction())

#ex6
print((6 + 3) - (6 + 3))

#ex7
print(5 + 4 - 7 + 3)

#ex8
print(100 + 5 * 3)

#ex9
thislist = ["apple", "banana", "cherry"]
print(thislist)

#ex10
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#ex11
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#ex12
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#ex13
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex14
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ex15
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#ex16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ex17
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#ex18
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#ex19
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex20
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#ex21
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex22
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex23
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#ex24
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#ex25
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#ex26
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#ex27
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#ex28
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#ex29
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ex30
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#ex31
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#ex32
if a > b: print("a is greater than b")

#ex33
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#ex34
  i = 1
while i < 6:
  print(i)
  i += 1

#ex35
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#ex36
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#ex37
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#ex38
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex39
for x in "banana":
  print(x)

#ex40
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#ex41
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex41
for x in range(6):
  print(x)

#ex42
for x in range(2, 6):
  print(x)

#ex43
for x in range(2, 30, 3):
  print(x)

#ex44
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#ex45
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")