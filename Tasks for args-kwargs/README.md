# *args/**kwargs

### What is *args?
- The `*args` parameter allows a function to accept any number of positional arguments.
- Inside the function, `args` becomes a tuple containing all the passed arguments.
- It is like multiple regular arguments (like a list)

```
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40))
```

**Output:**
```
6
100
```
---

### What is **kwargs?
- The `**kwargs` parameter allows a function to accept any number of keyword arguments.
- Inside the function, kwargs becomes a dictionary containing all the keyword arguments.
- It is like multiple keyword arguments (like a dictionary)

```
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Alice', age=25, city='NYC')
```

**Output:**
```
name: Alice
age: 25
city: NYC
```
---

We can use both `*args` and `**kwargs` in the same function but the order must be:
1. regular parameter
2. *args
3. **kwargs

```
def create_user(username, *hobbies, **details):
    print(f"Username: {username}")
    print(f"Hobbies: {hobbies}")
    print(f"Details: {details}")

create_user('john123', 'reading', 'gaming', age=25, city='LA')
```

**Output:**
```
Username: john123
Hobbies: ('reading', 'gaming')
Details: {'age': 25, 'city': 'LA'}
```
---

The `*` and `**` operators can also be used to unpack a list or dictionery into seperate arguments.

*Using `*` to unpack a list into arguments.*
```
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)
```

**Output:**
```
6
```
---
*Using `**` to unpack a dict into keyword arguments.*
```
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)
```

**Output:**
```
Hello Emil Refsnes
```