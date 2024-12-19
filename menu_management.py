def add1(x):
  list1.append(x)
def remove1(x):
  if x in list1:
    list1.remove(x)
  else:
    print("The item is not present")
def check1(x):
  if x in list1:
    print(f"Availability: {x} is available")
  else:
    print(f"Availability: {x} is not available")
list1=eval(input("initial_menu = "))
add_item=input("add_item = ")
add1(add_item)
remove_item=input("remove_item = ")
remove1(remove_item)
check_item=input("check_item = ")
print(f"Updated menu: {list1}")
check1(check_item)