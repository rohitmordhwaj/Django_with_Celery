class MyCustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Code that is executed in each request before the view is called
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        print("Request is coming from : ", request.META["HTTP_USER_AGENT"])
        return response

    # def process_view(request, view_func, view_args, **view_kwargs):
    #     pass
        # This code is executed just before the view is called

    # def process_exception(request, exception):
    #     pass
        # This code is executed if an exception is raised

    # def process_template_response(request, response):
    #     # This code is executed if the response contains a render() method
    #     return response