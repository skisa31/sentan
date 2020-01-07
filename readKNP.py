text_file = open("resultKNP.txt", encoding='utf-8')

li = []     # 1行ごとに読み込んだテキストの入る配列
ele = []    # (P)で区切ったテキストの入る配列
txt = []    # (P)で区切ったテキストをjoinしてものが入る配列
a = []      # (P)で区切られる配列のインデックスの数字を保持する配列

for line in text_file:
    knp = line.strip()
    e = knp.split("─")
    li.append(e[0])

for index, element in enumerate(li):
    if "(P)" in element or "。" in element:
        ele.append(element)
        a.append(index)
    else:
        ele.append(element)

# print(a)

for i in range(len(a)):
    if i == 0:
        txt.append("".join(ele[:a[i]+1]))
        # print(''.join(ele[:a[i]+1]))
    elif i == a[-1]:
        txt.append("".join(ele[a[i]:]))
        # print(''.join(ele[a[i]:]))
    else:
        txt.append("".join(ele[a[i-1]+1:a[i]+1]))
        # print(''.join(ele[a[i-1]+1:a[i]+1]))

# print(txt)

for j in range(len(txt)):
    print(txt[j])
    if "。" in txt[j]:
        print("\n")

text_file.close