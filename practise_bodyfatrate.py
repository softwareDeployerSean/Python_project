# 1.首先得到输入的数据,身高，体重，年龄，性别
personHeight = float(input('请输入身高(m)'))
personWeight = int(input('请输入体重(kg)'))
personSex = int(input('请输入性别(1是男，0是女)'))
personAge = int(input('请输入年龄'))

if not (0 < personHeight < 1.7 and 0 < personWeight < 200 and 0 < personAge < 150 and (
        personSex == 0 or personSex == 1)):
    exit()
# 2.进行计算
BMI = personWeight / (personHeight ** 2)
bodyfat = (1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex) / 100
if personSex:
    result = 0.15 < bodyfat < 0.18
else:
    result = 0.25 < bodyfat < 0.28
# minrate = 0.25 - 0.1 * personSex
# maxrate = 0.28 - 0.1 * personSex
# result = minrate < bodyfat < maxrate
# 3.输出1.7
if personSex == 1 and result:
    print("先生身体健康")
elif personSex == 1 and not result:
    if bodyfat < 0.15:
        print("先生身体瘦")
    else:
        print("先生身体胖")

elif personSex == 0 and result:
    print("女士健康")
elif personSex == 0 and not result:
    if bodyfat < 0.25:
        print("女士身体瘦")
    else:
        print("女士身体胖")

print('您的体脂率%.2f' % bodyfat, result)
# 测试本地commit   测试本地commit1   测试本地commit3   测试本地commit4
