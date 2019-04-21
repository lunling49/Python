import os

path, path1, path2, cmd = '', '', '', ''
# 当前使用平台：
print(os.name)       # 返回当前使用平台的代表字符，Windows用'nt'表示，Linux用'posix'表示
# 当前路径和文件
os.getcwd()          # 返回当前工作目录
os.listdir(path)     # 返回path目录下所有文件列表
# 绝对路径
os.path.abspath(path)   # 返回path的绝对路径
# 系统操作：
os.system()          # 运行shell命令
os.system('cmd')     # Windows下打开终端
os.system('ls')      # Linux下查看当前目录所有文件
# 查看文件名或目录：
os.path.split(path)                 # 将path的目录和文件名分开为元组
os.path.join(path1, path2, ...)     # 将path1，path2，...进行组合，若path2为绝对路径，则会将path1删除
os.path.dirname(path)                # 返回path中的目录（文件夹部分），结果不包含'\'
os.path.basename(path)              # 返回path中的文件名
# 创建目录：
os.mkdir(path)          # 创建path目录（只能创建一级目录，如'F:\XXX\WWW'）,在XXX目录下创建WWW目录
os.makedirs(path)       # 创建多级目录（如'F:\XXX\SSS'），在F盘下创建XXX目录，继续在XXX目录下创建SSS目录
# 删除文件或目录：
os.remove(path)     # 删除文件（必须是文件）
os.rmdir(path)       # 删除path目录(只能删除一级目录，如'F:\XXX\SSS'),只删除SSS目录
os.removedirs(path)  # 删除多级目录（如'F:\XXX\SSS'）,必须为空目录，删除SSS、FFF目录
# 更改路径：
os.chdir(path)  # 将当前工作目录更改为指定路径path
# 查看文件时间：
os.path.getmtime(path)  # 返回文件或目录的最后修改时间，结果为秒数
os.path.getatime(path)  # 返回文件或目录的最后访问时间，结果为秒数
os.path.getctime(path)  # 返回文件或目录得创建时间，结果为秒数
# 查看文件大小：
os.path.getsize(path)  # 返回文件的大小，若是目录则返回0
# 查看文件：
os.path.exists(path)  # 判断path是否存在，存在返回True,不存在返回False
os.path.isfile(path)  # 判断path是否为文件，是返回True,不是返回False
os.path.isdir(path)  # 判断path是否目录，是返回True，不是返回False
# 表现形式参数：
print(os.sep)  # 返回当前操作系统特定的路径分隔符
print(os.linesep)  # 返回当前平台使用的行终止符
print(os.extsep)  # 返回文件名与扩展名的分隔符
# 获取文件和目录：
os.walk(path)   # 递归返回path下的目录（包括path目录）、子目录、文件名的三元组
# 获得shell命令返回值：
fp = os.popen(cmd)   # 打开命令cmd或从命令cmd打开管道，返回值是连接到管道的文件对象
# 读取结果有2种方式
rlt1 = fp.read()
rlt2 = fp.readlines()
