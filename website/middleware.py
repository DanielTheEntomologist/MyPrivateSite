# def add_global_context_middleware(get_response):
#     # One-time configuration and initialization.


#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
        
#         response = get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     return middleware

class GlobalContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.global_context = {
    "name": "Daniel",
    "surname": "Borowiecki",
    "title": "Daniel's Blog",
    "author": "Daniel",
    "description": "This is a blog about Python and Django",
    "keywords": "Python, Django, Web Development",
    "page": "home",
}

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response, "context_data"):
            for key, value in self.global_context.items():
                if key not in response.context_data:
                    response.context_data[key] = value
        else:
            response.context_data = self.global_context
            
        return response