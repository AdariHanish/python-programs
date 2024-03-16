def a(f):
  return [f.title() for f in f]
f=["banana", "apple", "orange", "mango"]
c = a(f)
print("Original names:", f)
print("Capitalized names:", c)
