my_dict = {"name":"Shruthi","age":20}
print(my_dict["name"])  # Shruthi

my_dict["cgpa"] = 8.5    # Add
my_dict["age"] = 21      # Update
del my_dict["name"]       # Delete
print(my_dict)


for key, value in my_dict.items():
    print(key, value)