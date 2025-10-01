from django.shortcuts import render

# Create your views here.

def task_list(request):
    if not request.tenant:
        return render(request, "error.html", {"message": "Tenant not found"})