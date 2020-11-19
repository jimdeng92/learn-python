## 整个文件读取
## 文件路径：Python 是在项目目录运行的，因此文件路径也要以项目目录开头
# with open('10_文件和异常/pi_digits.txt') as file_object:
#   contents = file_object.read()
#   print(contents.rstrip())


## 逐行读取文件
filename = '10_文件和异常/pi_digits.txt' 
with open(filename) as file_object:
  for line in file_object:
    print(line)
