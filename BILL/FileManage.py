"""
备份bill.txt为bill.txt.bak.
文件内标记为测试的数据丢掉
"""

# 读取文件
f1 = open("bill.txt", "r", encoding="UTF-8")

# 备份
f2 = open("bill.txt.bak", "w", encoding="UTF-8")


for line in f1:
    # 把首尾空格以及换行符去掉
    line = line.strip()
    #分割并取出最后一列
    remarks = line.split(",")[-1]
    # 判断是不是测试
    if remarks =="测试":
        # 进入下一次循环
        continue
    f2.write(line)
    # 手动加入换行符
    f2.write("\n")

#关闭文件
f1.close()
f2.close()