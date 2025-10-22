def add(x, y):
    ret = x + y
    return ret

if __name__ == "__main__":
    test = add(1, 2) == 3
    print(f"Test:{test}")