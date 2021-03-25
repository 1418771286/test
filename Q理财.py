import traceback

class DealData(object):


    def __init__(self):
        self.small = [chr(i) for i in range(97, 123)]
        self.all = ''
        for i in self.small:
            self.all += i
        self.list1 = ['a：总负债', 'b：总资产', 'c：净资产', "d：当前应偿债本息", "e：当期收入", "f：流动性资产", "g：月均支出", "h：生息资产", "i：可变现资产", "j：保险理赔金", "k：10年生活费", "l：房屋重建装修成本", "n：家庭储蓄", "m：家庭税后收入", "o：投资资产", "p：理财收入"]
        # 装输入的数据
        self.dic = {}
        self.analyze = []
        print()
        print("欢迎使用Q分析")
        print("-" * 80)
        self.show_data()


    def write_data(self, key=False):
        # 如果传入True直接默认修改全部信息
        if key:
            word = self.all
        else:
            # 设置一个变量判断填写的序号合不合法
            is_right = True
            while True:
                word = input("请选择要修改的数据字母(输入all全修改)：").lower()
                if word == 'all':
                    word = self.all
                    break
                else:
                    # 遍历输入的每一个字符
                    for i in word:
                        # 如果有一个字符不在字母表即输入错误
                        if i not in self.small:
                            is_right = False
                            print("输入错误")
                            break
                        # 否则字符在字母表
                        else:
                            is_right = True
                # 如果输入的都正确，跳出while循环，否则继续循环
                if is_right:
                    break

        for i in self.list1:
            first_word = i[0]
            # 判断用户需要改的数据
            if first_word in word:
                num = input("{} = ".format(i))
                # 如果用户回车
                if num == '':
                   # 有这个键值对，这删除，返回False
                    if self.dic.pop(first_word, False):
                        pass
                        # print("删除了原来的键值对")
                    # 有或没有自接跳过，不再添加键值对
                    continue
                self.dic['{}'.format(first_word)] = num


    def show_data(self):
        n = 1
        for i in self.list1:
            n += 1
            first_word = i[0]
            # 判断是否有数据
            if n % 2 == 0:
                if first_word in self.dic:
                    print("{} = {}\t\t\t".format(i, self.dic["{}".format(first_word)]), end="")
                else:
                    print("{} = \t\t\t\t".format(i), end="")
            else:
                if first_word in self.dic:
                    print("{} = {}".format(i, self.dic["{}".format(first_word)]))
                else:
                    print("{} = ".format(i))


    def calculate(self):
        keys = self.dic.keys()

        try:
            if 'a' in keys and 'b' in keys:
                num1 = float(self.dic['a'])
                num2 = float(self.dic['b'])
                result = num1/num2
                print("总资产负债率 = 总负债/总资产 = {}/{} = {:.3f}".format(num1, num2, result))
                if result > 1:
                    advice = "家庭面临破产危险，应尽快降低负债。"
                elif result > 0.5:
                    advice = "家庭负债率高于标准值，应降低负债。"
                elif  result >= 0:
                    advice = "指标正常，负债合理。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "总资产负债率标准值：0.5以下。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'c' in keys and 'b' in keys:
                num1 = float(self.dic['c'])
                num2 = float(self.dic['b'])
                result = num1 / num2
                print("净资产比率 = 净资产/总资产 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result < 0.3:
                    advice = "家庭主要靠借债维持，应尽快降低负债。"
                elif result < 0.5:
                    advice = "家庭净资产过少，应降低负债。"
                elif result <= 1:
                    advice = "指标正常，净资产合理。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "净资产比率标准值：0.5以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'd' in keys and 'e' in keys:
                num1 = float(self.dic['d'])
                num2 = float(self.dic['e'])
                result = num1 / num2
                print("收入负债比率 = 当前应偿债本息/当期收入 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result < 0.4:
                    advice = "指标正常，家庭偿债能力强。"
                elif result < 0.8:
                    advice = "家庭偿债能力偏弱，应增加收入或降低负债。"
                elif result <= 1:
                    advice = "家庭收入基本用于抵债，急需增加收入或降低负债。"
                elif result > 1:
                    advice = "家庭收入不能抵债，面临破产。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "收入负债比标准值：0.4以下，0.36较合适。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'f' in keys and 'g' in keys:
                num1 = float(self.dic['f'])
                num2 = float(self.dic['g'])
                result = num1 / num2
                print("流动资产保障率 = 流动性资产/月均支出 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result <= 1 :
                    advice = "迅速变现能力太弱，应增加流动资产。"
                elif result < 2.5:
                    advice = "迅速变现能力较弱，应增加流动资产。"
                elif  result >= 2.5:
                    advice = "指标正常，即流动资产可以满足{:.1f}个月家庭支出。".format(result)
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "流动资产保障率标准值：3以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'h' in keys and 'g' in keys:
                num1 = float(self.dic['h'])
                num2 = float(self.dic['g'])
                result = num1 / num2
                print("生息资产保障率 = 生息资产/月均支出 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result <= 3 :
                    advice = "变现能力太弱，应增加生息资产。"
                elif result < 5:
                    advice = "变现能力较弱，应增加生息资产。"
                elif  result >= 5:
                    advice = "指标正常，即生息资产可以保障{:.1f}个月家庭支出。".format(result)
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "生息资产保障率标准值：6以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'c' in keys and 'g' in keys:
                num1 = float(self.dic['c'])
                num2 = float(self.dic['g'])
                result = num1 / num2
                print("净资产保障率 = 净资产/月均支出 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result <= 4:
                    advice = "生活保障能力太弱，应增加净资产。"
                elif result < 8:
                    advice = "生活保障能力较弱，应增加净资产。"
                elif result >= 8:
                    advice = "指标正常，即变卖净资产可以保障{:.1f}个月家庭支出。".format(result)
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "净资产保障率标准值：12以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'i' in keys and 'j' in keys and 'a' in keys and 'k' in keys and 'j' in keys:
                if 'l' in keys:
                    num5 = float(self.dic['l'])
                else:
                    num5 = 0
                num1 = float(self.dic['i'])
                num2 = float(self.dic['j'])
                num3 = float(self.dic['a'])
                num4 = float(self.dic['k'])
                result = (num1+num2-num3)/(num4+num5)
                print("灾变保障率 = (可变现资产+保险理赔金-现有负责)/(10年生活费+房屋重建装修成本) = ({}+{}-{})/({}+{}) = {:.3f}".format(num1, num2, num3, num4, num5, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result <= 1:
                    sentence = "合理保额 = 10年生活费 + 负债 - 可变现资产 = {} + {} -{} = {:.3f}".format(num4, num3, num1,  num4 + num3 - num1)
                    advice = "意外事故发生的承受力较低，可以增加保额。\n{}".format(sentence)
                elif result > 1:
                    advice = "指标正常，意外事故发生的承受力较高。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "灾变保障率标准值：1以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'n' in keys and 'm' in keys:
                num1 = float(self.dic['n'])
                num2 = float(self.dic['m'])
                result = num1 / num2
                print("储蓄比率 = 家庭储蓄/家庭税后收入 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result <= 0.1:
                    advice = "储蓄比率太少，应增加储蓄，减少不必要的支出。"
                elif result < 0.2:
                    advice = "应提高储蓄比率，减少不必要的支出。"
                elif result >= 0.2:
                    advice = "指标正常，有较好的储蓄能力。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "储蓄比率标准值：0.2以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'o' in keys and 'c' in keys:
                num1 = float(self.dic['o'])
                num2 = float(self.dic['c'])
                result = num1 / num2
                print("净资产投资比率 = 投资资产/净资产 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result < 0.2:
                    advice = "投资资产占比较少，应增加投资资产以实现理财目标。"
                elif result >= 0.2:
                    advice = "指标正常，投资资产占比合理。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "净资产投资比率标准值：0.5以上，年轻家庭0.2以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)


            if 'p' in keys and 'o' in keys:
                num1 = float(self.dic['p'])
                num2 = float(self.dic['o'])
                result = num1 / num2
                print("投资回报率 = 理财收入/投资资产 = {}/{} = {:.3f}".format(num1, num2, result))
                if result < 0:
                    advice = "指标异常，请检查输入的数据。"
                elif result < 0.3:
                    advice = "投资回报较低，应合理配置投资产品。"
                elif result >= 0.3:
                    advice = "指标正常，投资回报合理。"
                else:
                    advice = "指标异常，请检查输入的数据。"

                advise = "投资回报率标准值：0.3以上。您的为：{:.3f}，".format(result) + advice
                self.analyze.append(advise)



        except Exception as ex:
            print(ex)
            traceback.print_exc()

        print()
        print("指标分析：")
        for i in self.analyze:
            print(i)
        self.analyze.clear()

    def run(self):

        print("请填写相关数据，没有请回车跳过")
        self.write_data(True)
        print("-" * 80)
        print("当前数据如下：")
        self.show_data()

        while True:
            print()
            print("1:分析数据   2:修改数据   3:清除数据   0:退出")
            print("-" * 80)
            word = input("请输入操作：")
            if word == '0':
                break
            elif word == '1':
                print("各类指标如下：")
                self.calculate()
            elif word == '2':
                print("-" * 80)
                print("当前的数据如下：")
                self.show_data()
                self.write_data()
                print("-" * 80)
                print("修改后的数据如下：")
                self.show_data()
            elif word == '3':
                self.dic.clear()
                print("-" * 80)
                print("当前数据如下：")
                self.show_data()
            else:
                pass


if __name__ == '__main__':
    DealData().run()
