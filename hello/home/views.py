from django.shortcuts import render, redirect

from .models import ContactSubmission, IceCream, Order


def sp(request):
    return render(request, 'sp.html')


def about(request):
    return render(request, 'about us.html')


def home(request):
    """Home shows the available menu so visitors land on something live."""
    return render(request, 'home.html', {"menu": IceCream.objects.filter(is_available=True)})


def services(request):
    return render(request, 'services.html')


def contact(request):
    """Render the contact page; persist a ContactSubmission on POST."""
    if request.method == "POST":
        ContactSubmission.objects.create(
            name=request.POST.get("name", "").strip()[:120],
            email=request.POST.get("email", "").strip()[:254],
            message=request.POST.get("message", "").strip()[:5000],
        )
        return redirect("contact")
    return render(request, 'contact.html')


def ourreasontostart(request):
    return render(request, 'ourreasontostart.html')


def trackorders(request):
    """Look up an order by tracking_id from the ?id=... query param."""
    tracking_id = request.GET.get("id", "").strip()
    order = None
    if tracking_id:
        order = Order.objects.filter(tracking_id=tracking_id).first()
    return render(request, 'trackorders.html', {"order": order, "tracking_id": tracking_id})


def orders(request):
    """List every order, newest first."""
    return render(request, 'orders.html', {"orders": Order.objects.select_related("ice_cream").all()})
