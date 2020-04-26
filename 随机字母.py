import string
import random
n_int = int(input("请输入随机字母个数："))
def random_letters(n):
    # 定义一个空列表保存随机字母
    letters_list = []
    while len(letters_list) < n :
        a_str = string.ascii_letters 
        random_letter = random.choice(a_str)
        if (random_letter not in letters_list) :
            letters_list.append(random_letter)
        else:
            pass
    # 将列表转换成元组输出
    return tuple(letters_list)
print(random_letters(n_int))
