# Реализуйте алгоритм перемешивания списка.

from random import shuffle
 
if __name__ == '__main__':
 
    nums = list(range(10))
    print(nums)
    shuffle(nums)
    print("перемешанный список: ")
    print(nums)