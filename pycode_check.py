def greet(name):
    """Return a greeting message."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello, {name}!"


def main():
    print(greet("Matthew"))


if __name__ == '__main__':
    main()
