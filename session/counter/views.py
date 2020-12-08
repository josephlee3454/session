from django.shortcuts import render

# Create your views here.
def session_counter(request):
    
    request.session['counter'] = request.session['counter']  + 1
    return render(request,"index.html")

def session_counter_2(request):

    request.session['counter'] = request.session['counter']  + 2
    return render(request,"count_two.html")

def session_delete(request):

    request.session['counter'] = 0 
    return render(request,"delete.html")



