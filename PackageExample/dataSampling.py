import string
import random

def dataSampling(datatype,num,*args):
    try:
        print("等待生成数据，")
        result = []
        for index in range(0, num):
            if datatype is int:
                item = random.randint(args[0], args[1])
                result.append(item)
                continue
            elif datatype is float:
                item = random.uniform(args[0], args[1])
                result.append(item)
                continue
            elif datatype is str:
                item = ''.join(
                    random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(args[0]))
                result.append(item)
                continue
            elif datatype is tuple:
                item = tuple(''.join(
                    random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(args[0]) for _ in
                    range(args[1])))
                result.append(item)
                continue
            elif datatype is list:
                # list={'python':"1",'is':"2",'one':"3"}
                item = list(''.join(
                    random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(args[0]) for _ in
                    range(args[1])))
                result.append(item)
                continue
            else:
                raise ValueError("Invalid data type")
        return result
    except ValueError:
        print("输入数据格式错误")
    except TypeError:
        print("输入类型有误！")



if __name__ == '__main__':
    print(dataSampling(int,10,4,8))
    print(dataSampling(float,6,3,5))
    print(dataSampling(str,5,8))
    print(dataSampling(list,5,3,2))
    print(dataSampling(tuple, 5, 7, 2))
    print(dataSampling(str, 5, 5, 3))
