from aop import AspectType
from aop.aspectTypeAop import InvocationLoggerAspect


class AuthenticationBackend(metaclass=AspectType):
    def auth(self, user, password):
        print("user+passowrd",user+" "+password)
        if user == 'aop' and password == '#$%3&23%#$(%':
            return True
        return False

    def hellof(self,str):
        print("hellowolrd"+str)
        return "hellowolrd"+str






backend = AuthenticationBackend()
AuthenticationBackend.pointcut('auth', InvocationLoggerAspect)
backend.auth('aop', '#$%3&23%#$(%')
AuthenticationBackend.pointcut('hellof', InvocationLoggerAspect)
backend.hellof("zhangsan")