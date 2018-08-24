from django.shortcuts import render, HttpResponse
from django.views import View


# FBV (function-based view)
def test(request):
    return HttpResponse("FBV testing")


# CBV (class-based view)
class Login(View):
    """
    get     list
    post    add
    put     update
    delete  delete
    """

    def dispatch(self, request, *args, **kwargs):
        """
        acting like a decorator for our http request and response
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print("Before every request !!!")
        dispatcher = super().dispatch(request, *args, **kwargs)  # you can just write super here
        print("After every response !!! ")
        return dispatcher

    def get(self, request):
        print("? Running test CBV get function")
        return render(request, "login.html")

    def post(self, request):
        print("getting a post request value as: " + request.POST.get('user'))
        return HttpResponse("testing: CBV post request")
