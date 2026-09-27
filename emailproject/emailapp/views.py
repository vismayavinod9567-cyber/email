from django.shortcuts import render,redirect
from django.views import View
from django.core.mail import send_mail,settings
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
# ---------------- EMAIL VIEW CLASS ---------------------
class EmailView(View):
    def get(self,request,*args,**kwargs):
        sub="Django emal sending"
        msg="this is from django email sending project"
        from_addr=settings.EMAIL_HOST_USER
        to="aparna8848@gmail.com"
        res=send_mail(sub,msg,from_addr,[to])
        print(res)
        return HttpResponse("Mail send successfully")


class EmailSendView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"index.html")

    def post(self,request):
        print(request.POST)
        sub=request.POST.get("sub")
        msg=request.POST.get("msg")
        to=request.POST.get("email")
        from_addr=settings.EMAIL_HOST_USER
        send_mail(sub,msg,from_addr,[to])
        messages.success(request,"mail send successfully")
        return redirect("verify_view")


class EmailVerify(View):
    def get(self,request):
        return render(request,'success.html')
        