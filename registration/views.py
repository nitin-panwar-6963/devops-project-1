from django.shortcuts import render, redirect
from .dynamodb import save_user
import uuid

def register(request):
    if request.method == "POST":
        data = {
            "id": str(uuid.uuid4()),
            "full_name": request.POST.get("full_name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "roll_number": request.POST.get("roll_number"),
            "course": request.POST.get("course"),
            "year": request.POST.get("year"),
            "address": request.POST.get("address"),
        }

        save_user(data)
        return redirect('success')

    return render(request, "register.html")


def success(request):
    return render(request, "success.html")
