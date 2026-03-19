"""| Collection     | Mutable | Ordered         | Syntax Example  |
| -------------- | ------- | --------------- | --------------- |
| **List**       | ✅ Yes   | ✅ Yes           | `[1, 2, 3]`     |
| **Tuple**      | ❌ No    | ✅ Yes           | `(1, 2, 3)`     |
| **Set**        | ✅ Yes   | ❌ No            | `{1, 2, 3}`     |
| **Dictionary** | ✅ Yes   | ✅ (Python 3.7+) | `{"a":1,"b":2}` |
| **String**     | ❌ No    | ✅ Yes           | `"Hello"`       |
"""




my_list = [10, 20, 30, 40]
my_list.insert(1,10)    # add 10 in index 1 without removing their og

print(my_list[2])       # 30
my_list.pop(3)          #remove 3rd index value
my_list.remove(20)      # Remove value 20
print(my_list)

my_list.append(50)      # Add at end
my_list.append("python")
my_list[0]="shruthi"
print(my_list)

for item in my_list:
    print(item)