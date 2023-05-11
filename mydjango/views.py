from django.shortcuts import HttpResponse,render

def page(request):
    return render(request,"index.html")

def index_main(request,num_one,num_two,operator):
    if operator == 'add':
        result = num_one + num_two
    else:
        result = num_one * num_two

    return HttpResponse("OK you have provided num_one {} , num_two {} , operator is {} and the result is {}".format(num_one,num_two,operator,result))

def index(request):
    return HttpResponse("This is HttpResponse")

def your_name(request,name):
    return HttpResponse("MY NAME IS {}".format(name))