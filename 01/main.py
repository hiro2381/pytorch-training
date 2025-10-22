# import utils.function as function

# if __name__ == "__main__":
#     n = function.add(1, 2)
#     print(n)

# from utils.function import add

# if __name__ == "__main__":
#     n = add(1, 2)
#     print(n)

from utils.count import count_word

if __name__ == "__main__":
    s = "hello world"
    print("e:", count_word(s , "e"))
    print("o:", count_word(s , "o"))
    print("l:", count_word(s , "l"))