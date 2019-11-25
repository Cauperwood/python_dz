
 # task_1

file_1 = open("file_1.txt", 'w', encoding='UTF-8')
file_1.write(input("enter your data: "))
file_1.close()
file_1 = open("file_1.txt", "r")
fo_read = file_1.readlines()
file_1.close()
for k in fo_read:
    for_read = k.split()
s =[]
for l in for_read:
    g = l + '\n'
    s.append(g)
file_1 = open("file_1.txt", "w")
file_1.writelines(s)
file_1.close()
file_1 = open("file_1.txt", "r")
for h in file_1:
    print(h)
file_1.close()

# task_2

g2 = open('file_2.txt', 'r')
j = g2.readlines()
a = []
for h in j:
    i = 0
    for l in j[j.index(h)]:
        if l == ' ':
            i += 1
    a.append(i)
for idx, n in enumerate(a, 1):
    print(f'number of words in {idx} string is {n}')
g2.close()

# task_3

with open('file_3.txt') as f:
    av_sal = []
    us_list = f.read().split('\n')
    for line in us_list:
        line = line.split()
        if int(line[0]) < 20000:
            print(f'small salary {line}')
        av_sal.append((line[0]))
    print(f'average salary {sum(map(int, av_sal)) / len(av_sal)}')


# task_4

with open('file_4.txt', 'r', encoding='UTF-8') as digit:
    old_list_digit = digit.readlines()
    new_list_digit = []
    for line in old_list_digit:
        if 'One' in line:
            new_list_digit.append(line.replace('One', 'Один'))
        elif 'Two' in line:
            new_list_digit.append(line.replace('Two', 'Два'))
        elif 'Three' in line:
            new_list_digit.append(line.replace('Three', 'Три'))
        else:
            new_list_digit.append(line.replace('Four', 'Четыре'))
    print(new_list_digit)
    print(old_list_digit)

# task_5
with open('file_5.txt', 'w', encoding='utf-8') as new_digit:
    new_digit.writelines(new_list_digit)

# task_6

with open('file_6.txt', 'w', encoding='utf-8') as dit:
    dit.write('1 2 3 4 5 6 7 8 9')
with open('file_6.txt', 'r') as dit_ch:
    digit_sum = dit_ch.readline().split(' ')
    print(sum(map(int, digit_sum)))

# task_7

with open('file_7.txt', 'r') as g:
    les_data = g.readlines()
les_d = {}
#     # les_l = []
#     for line in les_data:
#         k = line.split()
#         # print(line)
#         # les_d.setdefault(k[0])
#         t = ''.join(k)
#         num = 0
#         for el in t:
#             if t.isdigit():
#                 num += int(t)
#                 # les_l.append(t)
#         les_d.update({t: num})
#     print(les_d)
#     # print(les_l)
for el in les_data:
    lesson = ''.join(el.split()[0])[:-1]
    oth = el.split()[1:]
    num = 0
    for t in oth:
        if t.isdigit():
                num += int(t)
    les_d.update({lesson: num})
print(les_d)

# task_8

