d1={"name":"hanish","id":1, "age":30,"salary":10000}
d2 = {"name":"John", "id":2}
# Merge dictionaries by adding values of common keys together.
merged_dict = {k: d1[k] + d2.get(k, 0) for k in set(list(d1.keys())+ list(d2.keys())) }
print("Merged dictionary is : ", merged_dict)