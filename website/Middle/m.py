from django.utils.deprecation import MiddlewareMixin

class Row(MiddlewareMixin):
    def process_request(self,request):
        print '666666666'

    def process_response(self,request,response):
        print '222222222'
        return response
