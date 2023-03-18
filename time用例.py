# time库的用例
import time
# 获取当前时间戳（秒）
t1 = time.time ()
print("当前时间戳（秒）:", t1)
# 将时间戳转换为本地时间元组
lt = time.localtime (t1)
print("本地时间元组:", lt)
# 将时间戳转换为UTC时间元组
gt = time.gmtime (t1)
print("UTC时间元组:", gt)
# 将本地时间元组转换为时间戳
t2 = time.mktime (lt)
print("转换回的时间戳（秒）:", t2)
# 将本地时间元组转换为可读字符串
s1 = time.asctime (lt)
print("可读字符串:", s1)
# 将时间戳或当前时间转换为可读字符串
s2 = time.ctime (t1)
print("可读字符串:", s2)
# 将本地时间元组或当前时间按照指定格式转换为字符串
f1 = "%Y-%m-%d %H:%M:%S"
s3 = time.strftime (f1, lt)
print("按照格式%s转换后的字符串:" % f1, s3)
# 将字符串按照指定格式转换为本地时间元组
f2 = "%d/%m/%Y"
s4 = "31/12/2020"
lt2 = time.strptime (s4, f2)
print("按照格式%s解析后的本地时间元组:" % f2, lt2)
