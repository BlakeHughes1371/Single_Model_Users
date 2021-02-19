from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
# def root(request):
#     return HttpResponse("Hello World!")
# --------------------------------------------


def index(request):
    context = {
        'friends': User.objects.all()
    }
    return render(request, "index.html", context)


def info(request):
    print(request.POST['firstname'])
    print(request.POST['lastname'])
    print(request.POST['email'])
    print(request.POST['age'])
    User.objects.create(fname = request.POST['firstname'], lname=request.POST['lastname'], email = request.POST['email'],
                        age = request.POST['age'])
    return redirect('/')

# a function handling a post request must REDIRECT!
# request.POST represents the information collected from the form.
# -------------------------------------------
# def index(request):
#     context = {
#         "time": strftime("%B-%d-%Y %H:%M %p", gmtime())
#     }
#     return render(request, "index.html", context)
# -------------------------------------------

# def index(request):
#     if 'visitcount' in request.session:
#         request.session['visitcount'] += 1
#     else:
#         request.session['visitcount'] = 1
#     return render(request, "index.html")


# def reset(request):
#     del request.session['visitcount']
#     return redirect('/')

# -------------------------------------------
# def survey(request):
#     # THE INFORMATION COLLECTED FROM THE FORM IS AVAILABLE and represented by THE KEYWORD REQUEST.POST
#     print(request.POST)
#     context = {  # only used to pass info to html
#         'forminfo': request.POST
#     }
#     # return redirect()
#     return render(request, "survey_info.html", context)

# --------------------------------------------
# def root(request):
#     return HttpResponse("Hello World!")
