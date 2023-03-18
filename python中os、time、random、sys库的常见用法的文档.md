# Python中os、time、random、sys库的常见用法

## os库

os库提供了许多与操作系统交互的函数，例如：

- os.getcwd ()：返回当前工作目录
- os.chdir (path)：改变当前工作目录到指定路径
- os.system (command)：在系统shell中运行指定命令
- os.listdir (path)：返回指定路径下的文件和目录列表
- os.path.join (path1, path2, ...)：将多个路径组合成一个路径
- os.path.split (path)：将路径分割成目录和文件名两部分
- os.path.exists (path)：判断路径是否存在
- os.path.isfile (path)：判断路径是否是一个文件
- os.path.isdir (path)：判断路径是否是一个目录
- os.path.getsize (path)：返回路径对应的文件或目录的大小（字节）
- os.path.getmtime (path)：返回路径对应的文件或目录的最后修改时间（秒）
- os.rename (src, dst)：重命名文件或目录
- os.remove (path)：删除文件
- os.rmdir (path)：删除空目录
- os.mkdir (path)：创建目录

## time库

time库提供了访问和转换时间的函数，例如：

- time.time ()：返回当前时间戳（秒）
- time.localtime ([secs])：将时间戳转换为本地时间元组（年，月，日，时，分，秒，周几，一年中第几天，夏令时标志）
- time.gmtime ([secs])：将时间戳转换为UTC时间元组（同上）
- time.mktime (tupletime)：将本地时间元组转换为时间戳
- time.asctime ([tupletime])：将本地时间元组转换为可读字符串（如'Mon Dec 20 15:30:00 2021'）
- time.ctime ([secs])：将时间戳或当前时间转换为可读字符串（同上）
- time.strftime (format [, tupletime])：将本地时间元组或当前时间按照指定格式转换为字符串（如'%Y-%m-%d %H:%M:%S'）
- time.strptime (string, format) ：将字符串按照指定格式转换为本地时间元组

## random库

random库提供了生成随机数和随机选择的函数，例如：

-random.seed ([x]) ：设置随机数种子，如果不提供参数，则使用系统时钟作为种子[^1^][1]
-random.random () ：返回一个[0.0, 1.0]之间的随机浮点数[^2^][2]
-random.uniform (a, b) ：返回一个[a, b]之间的随机浮点数[^2^][2]
-random.randint (a, b) ：返回一个[a, b]之间的随机整数[^2^][2]
-random.randrange ([start], stop [, step]) ：返回一个[start, stop）之间以step为步长的随机整数[^2^][2]
-random.choice (seq) ：从序列seq中随机选择一个元素[^2^][2]
-random.shuffle （seq） ：打乱序列seq中的元素顺序[^2^][2]
-random.sample （seq, k） ：从序列seq中随机选择k个不重复的元素[^2^][2]

## sys库

sys库提供了访问和操作系统相关信息和功能的函数，例如：

-sys.argv ：存储命令行参数的列表[^3^][3]
-sys.stdin ， sys.stdout ， sys.stderr ：标准输入流，标准输出流和标准错误流对象
-sys.exit ([arg]) ：

