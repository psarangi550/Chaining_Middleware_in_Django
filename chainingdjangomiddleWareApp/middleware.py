class FirstExecutableMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("First Middleware  Preprocess Being Executed Successfully")
        response=self.get_response(request)
        print("First Middleware Post Response will be executed at the end")
        return response
class SecondExecutableMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Second Middleware  Preprocess Being Executed Successfully")
        response=self.get_response(request)
        print("Second Middleware Post Response will be executed at the middle")
        return response
class ThirdExecutableMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Third Middleware  Preprocess Being Executed Successfully")
        response=self.get_response(request)
        print("Third Middleware Post Response will be executed at the first after the view function being executed")
        return response


