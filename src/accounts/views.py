from django.shortcuts import redirect
from django.views import View


class Login_Check(View):
    def get(self, request, *args, **kwargs):
        if str(request.tenant) == "public":
            return redirect("/admin")
        return redirect("/admin")


class Logout_Check(View):
    def get(self, request, *args, **kwargs):
        if str(request.tenant) == "public":
            return redirect("/")
        return redirect("account_login")
