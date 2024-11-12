from django.http import HttpResponse, JsonResponse

# html render
from django.shortcuts import render

"""
1) HttpResponse - Bu bizga HTTP status code va String (HTML) contentni qaytaradi.
2) JsonResponse - Bu bizga JSON contentni qaytaradi. (dict)
3) render(request, file_name.html) - Bu bizga HTML faylni qaytaradi. (html)

"""


def hello_func(request):
    # return JsonResponse(data={"message": "Hello world"})
    # return HttpResponse(content="<h1>Hello world</h1>")
    return render(request, "hello_page.html")


def home_page(request):
    return render(request, "index.html")
