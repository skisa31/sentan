text_file = open("knp.txt", encoding='utf-8')

li = []     # 1行ごとに読み込んだテキストの入る配列
ele = []    # (P)で区切ったテキストの入る配列
txt = []    # (P)で区切ったテキストをjoinしてものが入る配列
num = []      # (P)で区切られる配列のインデックスの数字を保持する配列

for line in text_file:
    knp = line.strip()
    e = knp.split("─")
    li.append(e[0])

for index, element in enumerate(li):
    if "(P)" in element or "。" in element:
        ele.append(element)
        num.append(index)
    else:
        ele.append(element)

# print(a)

for i in range(len(num)):
    if i == 0:
        txt.append("".join(ele[:num[i]+1]))
        # print(''.join(ele[:num[i]+1]))
    elif i == num[-1]:
        txt.append("".join(ele[num[i]:]))
        # print(''.join(ele[num[i]:]))
    else:
        txt.append("".join(ele[num[i-1]+1:num[i]+1]))
        # print(''.join(ele[num[i-1]+1:num[i]+1]))

# print(txt)

for i in range(len(num)):
    if "<" in txt[i]:
        b = txt[i]
        txt[i] = b.split("<")[0]

with open('sample.txt', 'w', encoding='utf-8') as f:

    for j in range(len(txt)):
        # print(txt[j])
        print(txt[j], file=f)
        if "。" in txt[j]:
            # print("\n")
            print('\n', file=f)

text_file.close
