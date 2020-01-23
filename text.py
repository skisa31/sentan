from glob import glob

files = glob('./text/*.txt')
z = 0
for file_name in files:
    z += 1
    text_file = open(file_name, encoding='utf-8')

    li = []     # 1行ごとに読み込んだテキストの入る配列
    li2 = []
     # ele = []    # (P)で区切ったテキストの入る配列
    txt = []    # (P)で区切ったテキストをjoinしてものが入る配列
    num = []      # (P)で区切られる配列のインデックスの数字を保持する配列
    a = []

    for line in text_file:
        e = line.split("\n")
        li.append(e[0])

    for ind, ele in enumerate(li):
        if "(P)" in ele and "用言" in ele:
            a.append(ind)
            ele + "*"
        else:
            pass

    for x in range(len(li)):
        ex = li[x].strip()
        g = ex.split("─")
        li2.append(g[0])

    # print(li2)

    li3 = []
    for index, element in enumerate(li2):
        if "(P)" in element or "。" in element:
            li3.append(element)
            num.append(index)
        else:
            li3.append(element)

    # print(a)

    for i in range(len(num)):
        if i == 0:
            txt.append("".join(li3[:num[i]+1]))
            # print(''.join(li3[:num[i]+1]))
        elif i == num[-1]:
            txt.append("".join(li3[num[i]:]))
            # print(''.join(li3[num[i]:]))
        else:
            txt.append("".join(li3[num[i-1]+1:num[i]+1]))
            # print(''.join(li3[num[i-1]+1:num[i]+1]))

    ele = []
    for index, element in enumerate(txt):
        if index in a or "。" in element:
            ele.append(element)
        else:
            ele.append(element)

    # print(txt)

    for i in range(len(num)):
        if "<" in ele[i]:
            b = ele[i]
            ele[i] = b.split("<")[0]
        elif "(P)" in ele[i]:
            b = ele[i]
            ele[i] = b.split("(")[0]
        else:
            pass

    if z < 10:
        create_file_path = './splited_text/splited_text_0' + str(z) + '.txt'
    else:
        create_file_path = './splited_text/splited_text_' + str(z) + '.txt'
    with open(create_file_path, 'w', encoding='utf-8') as f:

        for j in range(len(ele)):
            # print(txt[j])
            print(ele[j], file=f)
            if "。" in ele[j]:
                # print("\n")
                print('\n', file=f)

    text_file.close
