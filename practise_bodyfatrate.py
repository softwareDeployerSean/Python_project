# 1.首先得到输入的数据,身高，体重，年龄，性别
personHeight = float(input('请输入身高(m)'))
personWeight = int(input('请输入体重(kg)'))
personSex = int(input('请输入性别(1是男，0是女)'))
personAge = int(input('请输入年龄'))
# 2.进行计算
BMI = personWeight / (personHeight ** 2)
bodyfat = (1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex) / 100
minrate = 0.25 - 0.1 * personSex
maxrate = 0.28 - 0.1 * personSex
result = minrate < bodyfat < maxrate
# 3.输出
print('您的体脂率%.2f' % bodyfat, result)
#测试本地commit   测试本地commit1

