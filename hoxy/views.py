from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Account,Profile,Nickname,Name,Sns,Proof

def main(request) : 
    latest_question_list = Account.objects.order_by('-id')
    template = loader.get_template('hoxy/main.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'hoxy/main.html', context)

def report_button(request) : 
    return redirect('hoxy:report')

def result(request, account_id) : 
    result = get_object_or_404(Account,pk=account_id)
    return render(request, 'hoxy/result.html', {'result': result})
    #return HttpResponse("여기는  계정(%s)의 결과창 화면입니다." %account_id)

def report(request) : 
    return HttpResponse("여기는 제보창 화면입니다.")

def submit(request) : 
    return HttpResponse("여기는 제출 화면입니다.")

