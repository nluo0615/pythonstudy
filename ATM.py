"""
函数综合案例
定义一个全局变量：money，用来记录银行卡余额（默认5000000）
定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
定义如下的函数：
查询余额函数
存款函数
取款函数
主菜单函数
要求：
程序启动后要求输入客户姓名
查询余额、存款、取款后都会返回主菜单
存款、取款后，都应显示一下当前余额
客户选择退出或输入错误，程序会退出，否则一直运行
"""

# 定义全局变量money name
money = 5000000
name = None

# 要求客户输入姓名
name = input("请输入您的姓名:")

# 查询函数
def query(show_header):
    if show_header:
        print("--------查询余额--------")
    print(f"{name}，您好，您的余额为{money}元")

# 定义存款函数
def saving(num):
    global money # 在函数内部变为全局变量，修改作用域外的数据
    money += num
    print("--------存款--------")
    print(f"{name}，您好，您存款{num}元成功")

    # 调用query查询余额，不想要标题通过参数实现
    query(False)

# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------取款--------")
    print(f"{name}，您好，您取款{num}元成功")

    # 调用query查询余额
    query(False)
    menu()

# 定义主菜单函数
def menu():
    print("--------主菜单--------")
    print(f"{name},您好，欢迎来到洛洛ATM。请选择您要办理的业务",name)
    # print("1.查询余额\n2.存款\n3.取款\n4.退出")
    # 字符串对齐
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
# 设置无限循环，确保程序不退出
while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        query(True)
        continue # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("请输入存款金额："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入取款金额："))
        get_money(num)
        continue
    elif keyboard_input == "4":
        print("已成功退出登录")
        break
    else:
        print("请输入正确的业务")
        continue

