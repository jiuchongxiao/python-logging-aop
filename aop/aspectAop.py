
from aop import Aspect


class InvocationLoggerAspect(Aspect):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # def before(self, *args, **kwargs):
    #     self.execute(*args, **kwargs)
    #     print("before")
    #     self.logger.info(
    #          'before----Invocation: name=%s, args=%s, kwargs=%s' % (
    #              self.function,
    #              args,
    #              kwargs
    #          )
    #     )
    #
    # def after(self, *args, **kwargs):
    #     self.execute(*args, **kwargs)
    #     print("after")
    #     self.logger.info(
    #         'after----Invocation: name=%s, args=%s, kwargs=%s' % (
    #             self.function,
    #             args,
    #             kwargs
    #         )
    #     )
    def around(self, *args, **kwargs):
        self.logger.info(
            'aspect-around-before-Invocation: name=%s, args=%s, kwargs=%s' % (
                self.function,
                args,
                kwargs
            )
        )
        response = self.execute(*args, **kwargs)
        self.logger.info(
            'aspect-around-after-Invocation: name=%s, args=%s, kwargs=%s,response=%s' % (
                self.function,
                args,
                kwargs,
                response
            )
        )