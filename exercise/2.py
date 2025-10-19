class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.__scores = scores

    # 自我介绍方法
    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁，成绩：{self.__scores}")

    # 计算并返回平均成绩
    def get_average(self):
        if self.__scores:
            return round(sum(self.__scores.values()) / len(self.__scores), 1)
        else:
            return 0

    # 更新某一科的成绩
    def update_score(self, subject, value):
        if subject in self.__scores:
            self.__scores[subject] = value
            print(f"{self.name}的{subject}成绩已更新为{value}")
        else:
            print(f"科目 {subject} 不存在于成绩记录中！")


# 创建两个学生对象
s1 = Student("张三", 18, {"语文": 90, "数学": 85, "英语": 92})
s2 = Student("李四", 17, {"语文": 88, "数学": 95, "英语": 87})

# 调用 introduce 和 get_average
s1.introduce()
print(f"{s1.name}的平均成绩：{s1.get_average()}\n")

s2.introduce()
print(f"{s2.name}的平均成绩：{s2.get_average()}\n")

# 测试封装效果：尝试直接修改私有属性
print("尝试直接修改私有属性 __scores...")
try:
    s1.__scores['数学'] = 100
except Exception as e:
    print(f"错误：{e}")

# 查看是否真的修改了（实际上没有）
print("直接修改后，调用 introduce 查看实际成绩：")
s1.introduce()
print("→ 可见私有属性未被修改，说明封装起作用了。\n")

# 正确方式：使用 update_score 方法修改成绩
s1.update_score("数学", 100)

# 再次查看信息和平均分
print()
s1.introduce()
print(f"{s1.name}更新后的平均成绩：{s1.get_average()}")