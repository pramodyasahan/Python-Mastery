def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print(f"You added sprinkles")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")


get_ice_cream('vanilla')