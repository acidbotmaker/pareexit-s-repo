# *args and **kwargs

`*args` and `**kwargs` allow functions to accept a unknown number of arguments.

### What is *args?
- The `*args` parameter allow a function to accept any number of positional arguments.
- Inside a function, `args` becomes a tuple containing all the passed arguments.

```
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
```
---

### What is **kwargs?
- The `**kwargs` parameter allow a function to accept any number of keyword arguments.
- Inside the function, `kwargs` becomes a dictionary containing  all the keyword arguments.

```
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
```
---

While combining *args and **kwargs in the same function the order must be:
1. regular parameter
2. *args
3. **kwargs