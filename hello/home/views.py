from django.shortcuts import render, HttpResponse

# Create your views here.
def sp (requests):
    #return HttpResponse("this is hompage")
  
    return render(requests, 'sp.html')

def about (requests):
    #return HttpResponse("well i promised you to start shekhu and pops in our early 20s so here i am le kar hi diya finally apna sapna poora i love you")
    return render(requests, 'about us.html')

def home (requests):
    #return HttpResponse("well i promised you to start shekhu and pops in our early 20s so here i am le kar hi diya finally apna sapna poora i love you")
    return render(requests, 'home.html')

def services (requests):
    #return HttpResponse("this is services page")
    return render(requests, 'services.html')

def contact (requests):
    #return HttpResponse("this is contact page")

    return render(requests, 'contact.html')

def ourreasontostart (requests):
    return render(requests, 'ourreasontostart.html')

def trackorders (requests):
   return render(requests, 'trackorders.html')

def orders (requests):
   return render(requests, 'orders.html')