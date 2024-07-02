import webbrowser
abc_list = ['A', 'h', 'S', 'g', 's', '4', 'f', 'r', '2', '5', '9', '3', '/', ' ', 'R', 'L', 'M', 'C', 'V', '.', '1', 'a', 't', 'B', 'N', 'W', 'w', 'P', 'F', 'l', 'y', 'c', '0', 'q', 'p', 'e', 'n', 'd', 'x', 'z', 'b', '6', 'D', 'k', 'm', 'i', 'I', 'U', 'E', 'u', 'Z', '8', 'J', 'T', 'X', 'G', 'v', 'o', 'Y', 'Q', 'j', 'H', 'K', '7', 'O',':','\\']
def ysqd(ysqd):
    jg = [[]]
    a = ''
    n = 0
    for i in ysqd:
        n += 1
        for i_for in i:
            jg[n-1].append(abc_list[i_for])
    for jg_for in jg:
        for l in jg_for:
            a = a + l
        webbrowser.open(a)
        a = ''
    while True:
        print('你被骗了')
ysqd([[1, 22, 22, 34, 4, 65, 12, 12, 26, 26, 26, 19, 40, 45, 29, 45, 40, 45, 29, 45, 19, 31, 57, 44, 12, 56, 45, 37, 35, 57, 12, 23, 18, 20, 49, 53, 5, 30, 20, 27, 63, 17, 54, 12]])
