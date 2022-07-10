l1, student_name, student_name1 ,no_report= [], [], [], []
mo, lun, din, n = 0, 0, 0, 0
num_student = ['崔宇鑫', '田乐', '杜泽红', '李志鹏', '曹凯杰', '张靳宜', '王浩峰', '唐帅洋',
               '余琼', '董梦迪', '高洁', '李旭鹏', '闫飞', '阚玉常', '赵勇', '王赵辉', '徐稳栋',
               '杨政利', '贾云吉', '汪扬', '段越晋', '崔雅芳', '张宇', '赵旗浩', '徐志远', '周金保',
               '游凯歌', '赵长生', '张聪颖','陈志贤']

fin = open("word.txt", 'r')
fin1 = open("new-word.txt", 'w')
l2 = fin.readlines()

# 该操作是删除前三行
for i in range(3):
    l2.pop(0)


# 将所有的序号删除
for student in l2:
    s1 = student.split()
    s1.pop(0)
    l1.append(s1)

# 将所有的名字提取到另一个列表中
for i in range(len(l1)):
    student_name.append(l1[i][0])

# 规整数据惊醒换行（没五个元素换行）
for i in student_name:
    n += 1
    student_name1.append(i)
    if n % 5 == 0:
        student_name1.append('\n')
str1 = " ".join(student_name1)

# 将数据进行归纳处理，统计早中晚的个数
for oneself in l1:
    for i in range(len(oneself)):
        time = oneself[i]
        if time == "早":
            mo += 1
        elif time == "中" or time == "午":
            lun += 1
        elif time == "晚":
            din += 1
        elif time == "早中" or time == "早午":
            mo += 1
            lun += 1
        elif time == "中晚" or time == "午晚":
            lun += 1
            din += 1
        elif time == "早晚":
            mo += 1
            din += 1
        elif time == "早中晚" or time == "早午晚":
            mo += 1
            lun += 1
            din += 1

# 判断谁没有报，将其添加到一个列表中
for name in num_student:
    for line in l2:
        if name in line:
            break
    else:
        no_report.append(name)



fin1.write("这是所有的报餐同学名单：\n")
fin1.write(str1)
fin1.write("\n总计：{}人\n".format(len(student_name)))
fin1.write("早{}人，中{}人，晚{}人".format(mo, lun, din))
fin1.write("\n没有报的人是：\n")
fin1.write("、".join(no_report))
fin1.write("\n总计{}人".format(len(no_report)))
fin.close()
fin1.close()
