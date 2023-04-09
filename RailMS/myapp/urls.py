from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path("",views.index,name="home"),
    path("pnr_status",views.pnr_status,name="pnr_status"),
    path("view_pnr",views.view_pnr,name="view_pnr"),
    path("contact",views.contact,name="contact"),
    path("bookTicket",views.bookTicket,name="bookTicket"),
    path("login_user",views.login_user,name="login_user"),
    path("view_train",views.view_train,name="view_train"),
    path("view_schedule",views.view_schedule,name="view_schedule"),
    path("register",views.register,name="register"),
    path("logout_user",views.logout_user,name="logout_user"),
    path("admin",views.admin,name="admin"),
    path("view_ticket",views.view_ticket,name="view_ticket"),
    path("confirmBooking",views.confirmBooking,name="confirmBooking"),
    path("cancelTicket",views.cancelTicket,name="cancelTicket"),
    path("avlTrain",views.avlTrain,name="avlTrain"),
    # path("list_cancel.html",views.list_cancel,name=list_cancel),
]
admin.site.site_header = "SYN Admin"
admin.site.site_title = "SYN Admin Portal"
admin.site.index_title = "Welcome to SYN Researcher Portal"
