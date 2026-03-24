# 1. Sum of any number of inputs
def sum_all(*args):
    return sum(args)

# 2. Multiply all numbers
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 3. Print all positional arguments
def show_args(*args):
    for i, val in enumerate(args):
        print(f"Arg {i}: {val}")

# 4. Filter even numbers
def get_even_numbers(*args):
    return [x for x in args if x % 2 == 0]

# 5. Combine words into sentence
def make_sentence(*args):
    return " ".join(args)

# 6. Display user info (dynamic fields)
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 7. Configuration handler
def config_settings(**kwargs):
    default = {"theme": "light", "language": "EN"}
    default.update(kwargs)
    return default

# 8. Mixed args + kwargs
def display_data(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

# 9. Calculator with flexible inputs
def calculator(*args, operation="add"):
    if operation == "add":
        return sum(args)
    elif operation == "mul":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Invalid operation"

# 10. Find max with optional label
def find_max(*args, **kwargs):
    max_val = max(args)
    label = kwargs.get("label", "Max value")
    return f"{label}: {max_val}"

if __name__ == "__main__":
    print(sum_all(1, 2, 3))
    print(multiply_all(2, 3, 4))
    
    show_args("A", "B", "C")
    
    print(get_even_numbers(1, 2, 3, 4))
    print(make_sentence("Hello", "world"))
    
    user_profile(name="Ganesh", age=19)
    
    print(config_settings(theme="dark"))
    
    display_data(1, 2, a=10, b=20)
    
    print(calculator(1, 2, 3, operation="mul"))
    
    print(find_max(5, 9, 2, label="Highest"))