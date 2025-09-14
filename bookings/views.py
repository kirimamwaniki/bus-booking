from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import base64


def main(request):
    if request.method == 'POST':
        customer_obj = customer(
            id_number = request.POST['ID'],
            name = request.POST['name'],
            destination = request.POST['destination'],
            No_of_tickets = request.POST['seat_no']
        )

        customer_obj.save()

        return redirect('pay', id=customer_obj.id_number)

    return render(request, 'main.html')

def pay(request, id):
    #getting customer details from the main.html
    x = customer.objects.get(id_number=id)

    # initiating a payment
    if x.paid == "not paid":
        if request.method == "POST":
            x.paid = "paid"
            x.save()

            #redirecting to success page
            return redirect('success', id=x.id_number) 

    return render(request, 'payment.html')

def success(request, id):
    #getting customer number
    data = customer.objects.get(id_number=id)
    qr_data = f"Name: {data.name}, ID: {data.id_number}, destination: {data.destination} status: {data.paid}"

    #generating qrcode
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')


    return render(request, 'success.html', {'qr_code': img_str})

# Create your views here.
