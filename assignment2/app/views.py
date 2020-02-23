from django.shortcuts import render


# Create your views here.
def showmain(request):
    return render(request,"index.html")

def showindex(request):
    f1=int(request.POST.get("t1"))
    f2=int(request.POST.get("t2"))
    result=request.POST.get("t3")
    print(f1)
    print(f2)
    print(result)
    if result == "+":
        result=f1+f2
    elif result =="-":
        result=f1-f2
    elif result =="*":
        result=f1*f2

    else:
        try:
            result = f1/f2
        except ZeroDivisionError:
            result="invalid input"

    return render(request,"index.html",{"message":result})

