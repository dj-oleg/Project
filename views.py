from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from tests.models import Tests 
from django.shortcuts import redirect


def dovidka(request):
    return render(request,'blog/dovidka.html')

def starter(request):
    print(request.GET.get("error"))
    request.session["answers"] = []
    mainerror = "display:none" 
    if request.GET.get("error") =="true":
        mainerror = "display:block; color:red"
    return render(request, "blog/starter.html",{"mainerror": mainerror})


def general(request):
    # return HttpResponse('<div>Hello</div>'
    lst_tests = Tests.objects.values_list("tests_name")
    tmptest = Tests()
    # testinterface =  Tests.Mytest(tmptest) #запускаем тестово интерфейс из класса Тестс, должен вызваться метод май тест который запускает интерфейс zope
    # # print(Tests.objects.values_list("tests_name"))
    # print(testinterface)

    return render(request,'blog/general.html',context={'mytests':lst_tests})

def testscard(request):
    k_test = request.GET.get("test")#k_test это мы ловим имя теста который надо показать подробно 
    datetest = Tests.objects.filter(tests_name__startswith=k_test).values_list('tests_question','answer_list')#вытаскиваем подробную инфу о конкретном тесте
    print(datetest)
    return render(request,'blog/card.html',context={"datetest":datetest})

def saveanswers(request):
    # xhr.open('GET', '/saveanswers?test='+testnumber+'&answ='+answer_user, false);
    testnumber = request.GET.get("test")
    answer_user = request.GET.get("answ")
    tmp_session = request.session["answers"]
    tmp_session.append([testnumber,answer_user])
    request.session["answers"]=tmp_session
    return HttpResponse("1")

def finalresult(request):
    print(request.session["answers"])
    count_answers = len(request.session["answers"])
    print(count_answers)
    my_session = request.session["answers"]
    write_answers = 0
    for elem in my_session:
        print(elem[1])
        if elem[1] == "y":
            write_answers+=1
    print(write_answers)    
    return render(request,'blog/finalresult.html',context={'count_answers':count_answers,'write_answers':write_answers})





class Myclass(Exception):
    pass
    print("myClass1")

    def func(login,password):
        print("Myclass2")
        if login == "user" and password== "user":
            print("Okay")
        else:
            raise  Myclass()



def checkouts(request):
    print(request.POST)
    login = request.POST.get("login")
    
    password = request.POST.get("password")

    try:
        Myclass.func(login,password)
        return render(request,"blog/checkouts.html")
    except Exception:
        print("No password or login")
        return redirect("/starter?error=true")

            # print(login,password)
    
    # if request.POST.get("login") != "":
    #     login = request.POST.get("login")

    # try:
    #     if MycheckUser(login,password):
    #         return render(request,"blog/checkouts.html")
    #     else:
    #         return redirect("/starter?error=true")
    # except Exception as e:
    #     print({e})
    #     return redirect("/starter?error=true")

def MycheckUser(login,password):
    if login == "user" and password== "user":
        return True
    else:
        return False





