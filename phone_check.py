# 定义一个手机号变量
phone = input("请输入手机号：")

# 判断长度是否为11位
if len(phone) == 11:
    print("✅ 手机号长度符合要求")
else:
    print("❌ 错误：手机号必须是11位数字！")