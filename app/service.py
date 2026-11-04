def add(a: int, b: int) -> int:
    return abs(a + b)


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
