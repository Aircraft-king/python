def word_len(s):
    return len([i for i in s.split(' ') if i])
def main():
    s = str(input("请输入字符串："))
    l = word_len(s)
    print("单词个数为：",l)
main()
