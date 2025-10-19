# 1. 用字典列表存储原始数据
students = [
    {"姓名": "张三", "语文": 85, "数学": 92, "英语": 78},
    {"姓名": "李四", "语文": 95, "数学": 91, "英语": 93},
    {"姓名": "王五", "语文": 56, "数学": 56, "英语": 96},
    {"姓名": "赵六", "语文": 87, "数学": 78, "英语": 95},
    {"姓名": "孙七", "语文": 89, "数学": 68, "英语": 94}
]

# 2. 计算每名学生的总分和平均分
for s in students:
    total = s["语文"] + s["数学"] + s["英语"]
    avg = total / 3
    s["总分"] = total
    s["平均分"] = round(avg, 1)

for s in students:
    print(f"{s['姓名']}: 总分={s['总分']}, 平均分={s['平均分']}")

# 3. 补充遗漏数据
new_student = {"姓名": "郑十", "语文": 92, "数学": 91, "英语": 86}
students.append(new_student)
# 同时计算新学生的总分和平均分
total = new_student["语文"] + new_student["数学"] + new_student["英语"]
avg = total / 3
new_student["总分"] = total
new_student["平均分"] = round(avg, 1)

# 4. 找出总分最高的学生
max_student = max(students, key=lambda x: x["总分"])
print(f"总分最高的学生是：{max_student['姓名']}, 总分={max_student['总分']}")

# 5. 给赵六的数学成绩加5分，并更新总分和平均分
for s in students:
    if s["姓名"] == "赵六":
        s["数学"] += 5
        s["总分"] = s["语文"] + s["数学"] + s["英语"]
        s["平均分"] = round(s["总分"] / 3, 1)
        print(f"修改后：{s['姓名']}: 总分={s['总分']}, 平均分={s['平均分']}")
        break

# 6. 输出每科平均分和每科最高分的学生
subjects = ["语文", "数学", "英语"]
for subj in subjects:
    # 计算该科平均分
    avg_score = sum(s[subj] for s in students) / len(students)
    print(f"{subj}平均分：{avg_score:.1f}")
    # 找出该科最高分
    max_score = max(s[subj] for s in students)
    top_students = [s["姓名"] for s in students if s[subj] == max_score]
    print(f"{subj}最高分学生：{', '.join(top_students)} (分数：{max_score})")