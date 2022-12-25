from asyncio.windows_events import NULL
from locale import currency
from urllib.robotparser import RequestRate
from django.shortcuts import render,redirect
from random import randint
from django.http import Http404
from app.models import Customer, Food, Order, ReviewTab, UserMaster, Cart
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import razorpay



# Create your views here.
global OTP
global P_METHOD
OTP=0
def Index(request):
    return render(request, "app/index.html")

def Home(request):
    food = Food.objects.all().order_by('?')[:10]
    return render(request, "app/home.html",{'food':food})

def SignUpPage(request):
    return render(request, "app/Sign-up.html")

def RegisterUser(request):
    global OTP
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        gender=request.POST['gender']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "User Already Exists"
            return render(request, "app/Login.html",{'msg':message})
        else:
            if password==cpassword:
                otp=randint(10000,99999)
                OTP=otp
                Hpass = make_password(password)
                newuser = UserMaster.objects.create(email=email, password=Hpass,otp=otp)
                newcust = Customer.objects.create(user_id=newuser, firstname=firstname, lastname=lastname,
                contact=contact,gender=gender)
                
                subject = 'welcome to Food world'
                message = f'Hi {newcust.firstname} {newcust.lastname}, thank you for registering in Food. . Your otp is: {newuser.otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [newuser.email, ]
                send_mail( subject, message, email_from, recipient_list, fail_silently=True )
                return render(request, "app/otpverify.html",{'user':newuser})
            else:
                message = "Password Doesnot Match"
                return render(request, "app/Sign-up.html",{'msg':message})            
    return render(request, "app/Sign-up.html")

# def OtpPage(request):
#     return render(request, "app/otpverify.html")

def OtpVerify(request,pk):
    user = UserMaster.objects.get(pk=pk)
    otp=int(request.POST['otp'])
    if OTP==otp:
        user.Is_verified=True
        user.save()
        message="OTP Verified Successfully"
        return render(request, "app/Login.html",{'msg':message})
    else:
        message="OTP incorrect"
        return render(request, "app/otpverify.html",{'msg':message})

def LoginPage(request):
    return render(request, "app/Login.html")

def Login(request):
    if request.method=="POST":
        email=request.POST['logemail']
        password=request.POST['logpassword']
        user = UserMaster.objects.get(email=email)
        if user:
            if check_password(password, user.password):
                cust = Customer.objects.get(user_id=user)
                food = Food.objects.all().order_by('?')[:50]
                cust_cart=Cart.objects.filter(cust_id=cust)
                request.session['cartqnt']=Cart.objects.filter(cust_id=cust).count()
                request.session['id']=user.id
                request.session['email']=user.email
                request.session['password']=user.password
                request.session['firstname']=cust.firstname
                request.session['lastname']=cust.lastname
                request.session['address']=cust.address
                request.session['state']=cust.state
                request.session['city']=cust.city
                request.session['pincode']=cust.pincode
                request.session['contact']=cust.contact
                request.session['gender']=cust.gender
                request.session['near']=cust.near
                message="You are Logged in Successfully"
                return render(request, "app/home.html", {'msg':message, 'food':food})
            else:
                message="Password Doesnot Match"
                return render(request,"app/Login.html",{'msg':message})
        else:
            message="User Doesnot Exists"
            return render(request, "app/Login.html", {'msg':message})

def LogOut(request):
    if request.session['id']:
        del request.session['id']
        del request.session['password']
        message="Logged Out Successfully"
        food = Food.objects.all().order_by('?')[:50]
        return render(request, "app/index.html", {'msg':message,'food':food})
    else:
        return redirect('home')

def DishesPage(request):
    food = Food.objects.all()
    return render(request, "app/Dishes.html", {'food':food})

def MenuPage(request):
    food = Food.objects.all()
    return render(request, "app/menu.html", {'food':food})

def OrderPage(request,pk):
    food=Food.objects.get(pk=pk)
    return render(request, "app/Table.html",{'food':food})

def ConfirmOrderPage(request,pk,fpk):
    global P_METHOD
    user = UserMaster.objects.get(pk=pk)
    if user:
        cust = Customer.objects.get(user_id=user)
        food = Food.objects.get(pk=fpk)
        cust.state=request.POST['state']
        cust.city=request.POST['city']
        cust.address=request.POST['address']
        cust.pincode=request.POST['pincode']
        cust.near=request.POST['near']
        paymentmethod=request.POST['paymentmethod']
        if paymentmethod=="-Select Payment Method-":
            message="Please Select Any one Payment Method"
            return render(request, "app/Table.html", {'food':food,'msg':message})
        P_METHOD=paymentmethod
        cust.save()
        if food.offerprice>=500:
            delcharge=0
        elif food.offerprice>=300:
            delcharge=40
        else:
            delcharge=70
        price = food.offerprice+delcharge
        return render(request,"app/confirmorder.html",{'cust':cust,'food':food,'paymentmethod':paymentmethod,'delcharge':delcharge,'price':price})

def OrderPlace(request,pk,fpk):
    cust = Customer.objects.get(user_id=pk)
    
    if cust:
        food = Food.objects.get(id=fpk)
        offerprice=food.offerprice
        address=cust.address
        pincode=cust.pincode
        contact=cust.contact
        near=cust.near
        quantity=int(request.POST['quantity'])
        if offerprice>=500:
            delcharge=0
        elif offerprice>=300:
            delcharge=40*quantity
        else:
            delcharge=70*quantity
        offerprice=offerprice*quantity
        totalAmount = offerprice+delcharge
        paymentmethod=P_METHOD
        neworder = Order.objects.create(orderid=cust,foodid=food,offerprice=offerprice,
        totalAmount=totalAmount, deladdress=address,delpincode=pincode,delcontact=contact,delnear=near,
        quantity=quantity,delcharge=delcharge,paymentmethod=paymentmethod)

        if paymentmethod == "UPI" or paymentmethod == "Net Banking":
            # auth = ("PUBLIC_KEY", "SECRET_KEY")
            client = razorpay.Client(auth=("rzp_test_7PlwfpJ4UJOaZt", "0DhKowoXW6xBdljofyamTO2r"))
            payment = client.order.create({'amount':(totalAmount*100), 'currency':'INR', 'payment_capture':'1'})
            return render(request,"app/confirmorder.html",{'cust':cust,'food':food,'paymentmethod':paymentmethod,'delcharge':delcharge,'price':totalAmount, 'payment':payment})


        message="Thank You! Your Order will deliver soon"
        subject = f'{neworder.foodid.foodname} Ordered Successfully'
        emessage = f'Hi {neworder.orderid.firstname} {neworder.orderid.lastname}, thank you Choosing Food. . Your Order will deliver soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [neworder.orderid.user_id.email, ]
        send_mail( subject, emessage, email_from, recipient_list )
        food = Food.objects.all()        
        

        return render(request,"app/home.html",{'msg':message,'food':food})

@csrf_exempt
def Success(request,pk):
    if request.method=="POST":
        a=request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        neworder = Order.objects.filter(orderid=pk).latest('id')
        neworder.payment_id = order_id
        neworder.paid = True
        neworder.save()

        subject = f'{neworder.foodid.foodname} Ordered Successfully'
        emessage = f'Hi {neworder.orderid.firstname} {neworder.orderid.lastname}, thank you Choosing Food. . Your Order will deliver soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [neworder.orderid.user_id.email, ]
        send_mail( subject, emessage, email_from, recipient_list )
        request.session['id'] = neworder.orderid.user_id.id
        request.session['firstname'] = neworder.orderid.firstname
        request.session['lastname'] = neworder.orderid.lastname
    return render(request, "app/paymentstatus.html")


def CartPage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user:
        cust=Customer.objects.get(user_id=user)
        cust_cart=Cart.objects.filter(cust_id=cust)
        return render(request,"app/cart.html",{'custcart':cust_cart})

def AddToCart(request,pk,fpk):
    user=UserMaster.objects.get(pk=pk)
    if user:
        cust=Customer.objects.get(user_id=user)
        food=Food.objects.get(id=fpk)
        chk=Cart.objects.filter(cust_id=cust,food_id=food)
        if not chk:
            newcart=Cart.objects.create(cust_id=cust,food_id=food)
            cust_cart=Cart.objects.filter(cust_id=cust)
            request.session['cartqnt']=Cart.objects.filter(cust_id=cust).count()
        return redirect('home')

def ReviewPage(request):
    try:
        review=ReviewTab.objects.all()
    except:
        review = False
        return render(request,"app/Review.html",{'review':review})
    
    return render(request,"app/Review.html",{'review':review})


def SubmitReview(request, pk):
    user=UserMaster.objects.get(pk=pk)
    if user:
        cust=Customer.objects.get(user_id=user)
        chk=ReviewTab.objects.filter(cust_id=cust)
        if chk:
            review=ReviewTab.objects.get(cust_id=cust)
            review.rating = request.POST.get('rating')
            review.description = request.POST['desc']
            review.save()
        else:
            val = request.POST['rating']
            desc = request.POST['desc']
            newreview=ReviewTab.objects.create(cust_id=cust,rating=val,description=desc)

        message="Review Added"
        all = ReviewTab.objects.all()
        return render(request,"app/Review.html", {'review':all})


def AboutPage(request):
    return render(request,"app/About.html")

def GallaryPage(request):
    return render(request,"app/Gallery.html")

def MyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get(user_id=user)
    if Order.orderid==cust:
        order = Order.objects.get(orderid=cust)
        return render(request, "app/My-profile.html", {'user':user, 'cust':cust, 'order':order})
    else:
        return render(request, "app/My-profile.html", {'user':user, 'cust':cust})


def MyOrderPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get(user_id=user)
    order = Order.objects.filter(orderid=cust)
    return render(request, "app/My order.html", {'order':order})



############################ ADMIN SIDE ################################

def AdminLoginPage(request):
    return render(request, "app/admin/adminloginpage.html")

def AdminDashboard(request):
    return render(request, "app/admin/index.html")

def AddFoodPage(request):
    return render(request, "app/admin/addfood.html")

def AddNewFood(request):
    if request.method=="POST":
        if request.POST['foodtype']=="-Select Food Type-":
            message="Please Select Food Type"
        else:
            foodname = request.POST['foodname']
            foodprice = int(request.POST['foodprice'])
            foodtype = request.POST['foodtype']
            offer = int(request.POST['offer'])
            offerprice=foodprice-foodprice*(offer/100)
            foodpic = request.FILES['foodimage']
            newfood = Food.objects.create(foodname=foodname,foodprice=foodprice,
            foodtype=foodtype,offerprice=offerprice,offer=offer,foodpic=foodpic)
            message="New Food Added"
            return render(request,"app/admin/addfood.html", {'msg':message})

def FoodList(request):
    food = Food.objects.all()
    return render(request, "app/admin/tables.html",{'food':food})

def DeleteFood(request,pk):
    food = Food.objects.filter(pk=pk)
    food.delete()
    message = "1 Food Deleted"
    food = Food.objects.all()
    return render(request, "app/admin/tables.html",{'msg':message, 'food':food})

def UserList(request):
    cust=Customer.objects.all()
    return render(request,"app/admin/userlist.html",{'cust':cust})

def DeleteUser(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get(user_id=user)
    message =  "User"+ cust.firstname+" "+cust.lastname+"is Removed"
    user.delete()
    cust.delete()
    user=UserMaster.objects.all()
    cust=Customer.objects.all()
    return render(request, "app/admin/userlist.html",{'msg':message,'cust':cust})

def AdminLogin(request):
    if request.method=="POST":
        if request.POST['username']=="sandip@gmail.com" and request.POST['adminpass']=="s123":
            request.session['name']="Sandip Majhi"
            return render(request,"app/admin/index.html")
        else:
            message="Username or Password Doesnot Match"
            return render(request,"app/admin/adminloginpage.html",{'msg':message})

def AdminLogout(request):
    del request.session['name']
    return render(request,"app/admin/adminloginpage.html")

def OrderList(request):
    order=Order.objects.all()
    return render(request,"app/admin/orderlist.html",{'order':order})

def DeleteOrder(request,pk):
    order=Order.objects.get(pk=pk)
    order.delete()
    message="Order Has Been Deleted"
    order= Order.objects.all()
    return render(request,"app/admin/orderlist.html",{'order':order})
