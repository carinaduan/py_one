#coding=utf-8
class User:
    '用户信息类'
    __secretCount = 0  # 私有变量
    def __init__(self,id,user_name):   #这是构造方法，self是类的实例
        self.id = id;
        self.user_name = user_name;


    def displayUserInfo(self):
        print self.id,"-----",self.user_name,"----",self.__secretCount;   #python中用逗号连接字符串


print "123"
u = User(1,"duan");
u.displayUserInfo();


print "User.__doc__:", User.__doc__            #User.__doc__: 用户信息类
print "User.__name__:", User.__name__          #User.__name__: User
print "User.__module__:", User.__module__      #User.__module__: __main__   ----类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
print "User.__bases__:", User.__bases__        #User.__bases__: ()       --------类的所有父类构成元素（包含了一个由所有父类组成的元组）
#__dict__ 类的属性（包含一个字典，由类的数据属性组成）
print "User.__dict__:", User.__dict__          #User.__dict__: {'__module__': '__main__', 'displayUserInfo': <function displayUserInfo at 0x028038F0>, '__doc__': '\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe7\xb1\xbb', '__init__': <function __init__ at 0x02803930>}