
# テスト用
def add(x, y):
    ret = x + y
    return ret


if __name__ == "__main__": 
    n = add(1, 2)
    print(n)
    m = add(3, 4)  
    print(m)
    p = add(n, m)
    print(p)