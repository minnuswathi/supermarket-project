from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import*
#def supermarket(request):
    #customer_name=None
    #if request.method=='POST':
        #customer_name=request.POST.get("customer_name")
        #print(customer_name)
    #name=CustomerBill.objects.get(customer_name=customer_name)
    #return render(request,"supermarket.html")
def supermarket_save(request):
    if request.method!='POST':
        return render(request,"supermarket.html")
    else:
        customer_name=request.POST.get("customer_name")
        print(customer_name)
        customer_mobile=request.POST.get("customer_mobile")
        print(customer_mobile)
        customer_address=request.POST.get("customer_address")
        print(customer_address)
        quantity=int(request.POST.get("quantity"))
        print(quantity)
        date=request.POST.get("date")
        print(date)
        item_name=request.POST.get("item_name")
        print(item_name)
        price=int(request.POST.get("price"))
        print(price)
        total_price=quantity*price
        try:
            item=Items.objects.create(item_name=item_name,price=price)
            item.save()
            super_market=SupermarketModel.objects.create(customer_name=customer_name,quantity=quantity,customer_mobile=customer_mobile,customer_address=customer_address,date=date)
            super_market.save()

            customer_bill=CustomerBill.objects.create(customer_name=customer_name,quantity=quantity,customer_mobile=customer_mobile,customer_address=customer_address,date=date,item_name=item_name,unit_price=price,total_price=total_price)
            customer_bill.save()
            messages.success(request,"successfully billed")
            return redirect(showBill,name=customer_name)
        except:
            messages.error(request,"billing failed")
            return redirect('supermarket')

def showBill(request,name):
    bill=CustomerBill.objects.filter(customer_name=name)
    return render(request,"bill.html",{"bill":bill})
