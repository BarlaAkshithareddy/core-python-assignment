def total_price(items):
  total_price=sum(items.values())
  if len(items)==0:
    return "cart is empty"
  elif len(items)<5:
    return total_price
  else:
    return total_price*0.9

items = {}
n = int(input("Enter number of key-value pairs: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    items[key] = value
total_price(items)