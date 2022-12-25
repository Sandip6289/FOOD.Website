from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.Index,name='index'),
    path("homepage/",views.Home,name='home'),
    path("signuppage/", views.SignUpPage, name='signuppage'),
    path("register/", views.RegisterUser, name='register'),
    path("loginpage/", views.LoginPage, name='loginpage'),
    path("login/",views.Login,name='login'),
    path("logout/",views.LogOut, name='logout'),
    # path("otppage/",views.OtpPage,name='otppage'),
    path("otpverify/<int:pk>",views.OtpVerify,name='otpverify'),
    path("dishes/",views.DishesPage,name='dishes'),
    path("menu/",views.MenuPage,name='menu'),
    path("orderpage/<int:pk>",views.OrderPage,name='orderpage'),
    path("comfirmorderpage/<int:pk>-<int:fpk>",views.ConfirmOrderPage,name='confirmorderpage'),
    path("orderplace/<int:pk>-<int:fpk>",views.OrderPlace,name='orderplace'),
    path("success/<int:pk>",views.Success,name='success'),
    path("addtocart/<int:pk>-<int:fpk>",views.AddToCart,name='addtocart'),
    path("cartpage/<int:pk>",views.CartPage,name='cartpage'),
    path("reviewpage/",views.ReviewPage,name='reviewpage'),
    path("submitreview/<int:pk>",views.SubmitReview,name='submitreview'),
    path("aboutpage/",views.AboutPage,name='aboutpage'),
    path("gallarypage/",views.GallaryPage,name='gallarypage'),
    path("myprofilepage/<int:pk>",views.MyProfilePage,name='myprofilepage'),
    path("myorderpage/<int:pk>",views.MyOrderPage,name='myorderpage'),


    ####################### ADMIN SIDE ########################

    path("adminloginpage/",views.AdminLoginPage,name='adminloginpage'),
    path("adminlogin/",views.AdminLogin,name='adminlogin'),
    path("admindashboard/",views.AdminDashboard,name='admindashboard'),
    path("addfoodpage/",views.AddFoodPage,name='addfoodpage'),
    path("addnewfood/",views.AddNewFood,name='addnewfood'),
    path("foodlist/",views.FoodList,name='foodlist'),
    path("deletefood/<int:pk>",views.DeleteFood,name='deletefood'),
    path("userlist/",views.UserList,name='userlist'),
    path("deleteuser/<int:pk>",views.DeleteUser,name='deleteuser'),
    path("adminlogout/",views.AdminLogout,name='adminlogout'),
    path("orderlist/",views.OrderList,name='orderlist'),
    path("deleteorder/<int:pk>",views.DeleteOrder,name='deleteorder'),
]