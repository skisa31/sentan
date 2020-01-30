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

    # （P)と用言が含まれる行番号をnumPに記録
    for numP, ele in enumerate(li):
        if "(P)" in ele and "用言" in ele or "。" in ele:
            a.append(numP)
        else:
            pass

    print(a)

    # 空白と─を削除してli2に入れる
    for index, element in enumerate(li):
        el = li[index].strip()
        splited_el = el.split("─")
        li2.append(splited_el[0])
        """
        if index in a:
            li2.append(splited_el[0])
            num.append(index)
        else:
            li2.append(splited_el[0])
        """

    # print(li2)

    li3 = []
    for index, element in enumerate(li2):
        if index in a:
            li3.append(element)
            num.append(index)
        else:
            li3.append(element)

    print(li3)

    if not num:
        txt.append("".join(li3[0:len(li3)]))
    else:
        for i in range(len(num)):
            if i == 0:
                txt.append("".join(li3[:num[i]+1]))
                print(''.join(li3[:num[i]+1]))
            elif i == num[-1]:
                txt.append("".join(li3[num[i]:len(li3)]))
                print(''.join(li3[num[i]:len(li3)]))
            else:
                txt.append("".join(li3[num[i-1]+1:num[i]+1]))
                print(''.join(li3[num[i-1]+1:num[i]+1]))


    ele = []
    for index, element in enumerate(txt):
        if index in a or "。" in element:
            ele.append(element)
        else:
            ele.append(element)

    # print(txt)

    if not num:
        if "<" in ele[0]:
            b = ele[0]
            ele[0] = b.replace("(P)", "")
            c = ele[0]
            ele[0] = c.split("<")[0]
    else:
        for i in range(len(num)):
            if "<用言" in ele[i] or "<体言" in ele[i]:
                b = ele[i]
                ele[i] = b.replace("(P)", "")
                c = ele[i]
                ele[i] = c.replace("-PARA", "")
                d = ele[i]
                ele[i] = d.split("<")[0]
            else:
                b = ele[i]
                ele[i] = b.replace("-PARA", "")
                c = ele[i]
                ele[i] = c.replace("(P)", "")
                d = ele[i]
                ele[i] = d.replace("<I>", "")

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
