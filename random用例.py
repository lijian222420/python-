# random库的用例
import random
# 设置随机数种子
random.seed (1234)
# 返回一个[0.0, 1.0)之间的随机浮点数
r1 = random.random ()
print("随机浮点数:", r1)
# 返回一个[a, b]之间的随机浮点数
r2 = random.uniform (10, 20)
print("随机浮点数:", r2)
# 返回一个[a, b]之间的随机整数
r3 = random.randint (10, 20)
print("随机整数:", r3)
# 返回一个[start, stop)之间以step为步长的随机整数
r4 = random.randrange (10, 20, 2)
print("随机整数:", r4)
# 从序列seq中随机选择一个元素
seq = ["a", "b", "c", "d"]
r5 = random.choice (seq)
print("随机元素:", r5)
# 打乱序列seq中的元素顺序
random.shuffle (seq)
print("打乱后的序列:", seq)
# 从序列seq中随机选择k个不重复的元素
r6 = random.sample (seq, 2)
print("随机选择的两个元素:", r6)
