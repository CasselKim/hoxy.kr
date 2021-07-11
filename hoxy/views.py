#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Account,Profile,Nickname,Name,Sns,Proof,Verify,Report,Test
from .form import UploadProfile
from datetime import datetime, timedelta
from pytz import timezone

def main(request) : 
    latest_question_list = Account.objects.all()
    template = loader.get_template('hoxy/main.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'hoxy/main.html', context)

def report_button(request) : 
    return redirect('hoxy:report')

def search_button(request) :
    kw = request.POST.get('kw', '')  # 검색어
    nickname_object = Nickname.objects.filter(nickname_search=kw.replace(' ','').lower())
    if len(nickname_object) > 1 : 
        is_overflow = True
        is_empty = False
    elif len(nickname_object) == 0 : 
        is_overflow = False
        is_empty = True
    else : 
        is_overflow = False
        is_empty = False

    if len(nickname_object) : 
        puuid = nickname_object.get().puuid
        profile_object = Profile.objects.filter(puuid=puuid)
        name_objects = Name.objects.filter(puuid=puuid)
        sns_objects = Sns.objects.filter(puuid=puuid)
        proof_objects = Proof.objects.filter(puuid=puuid)
        nickname_objects = Nickname.objects.filter(puuid=puuid)
        modify_time = (puuid.modify_time + timedelta(hours=9)).strftime("(%Y-%m-%d) %H:%M:%S") #To KST
        context = {
            'kw' : kw,
            'nickname_object' : nickname_objects.all,
            'profile_object' : profile_object.get,
            'name_object' : name_objects.get,
            'sns_objects' : sns_objects.get,
            'proof_objects' : proof_objects.get,
            'is_overflow' : is_overflow,
            'is_empty' : is_empty,
            'modify_time' : modify_time,
        }
        return render(request, 'hoxy/result.html',context)
    else : 
        context = {
            'kw':kw,
            'nickname_object' : None,
            'is_overflow' : is_overflow,
            'is_empty' : is_empty,
        }
        return render(request, 'hoxy/result.html',context)

def upload_profile(request) : 
    if request.method=='POST' : 
        post = Profile()
        post.url = request.POST['image']
        post.puuid = Account(id=4)
        post.save()
        return render(request, 'hoxy/report.html', {'profile':post.url})
    else : 
        return render(request, 'hoxy/test.html')

def report(request) : 
    return render(request, 'hoxy/report.html')  
    
def test(request) : 
    account_num = len(Account.objects.all())
    print(account_num)
    return HttpResponse("이건 테스트임")

def submit(request) : 
    if request.method=='POST' : 
        kw_nickname = request.POST.get('kw-nickname', '')
        kw_name = request.POST.get('kw-name', '')
        kw_profile = request.FILES.get('profile','')
        kw_youtube = request.POST.get('kw-youtube', '')
        kw_twitch = request.POST.get('kw-twitch', '')
        kw_afreecatv = request.POST.get('kw-afreecatv', '')
        kw_namu = request.POST.get('kw-namu', '')
        kw_instagram = request.POST.get('kw-instagram', '')
        kw_dcinside = request.POST.get('kw-dcinside', '')
        kw_proof_pic_url1 = request.FILES.get('proof_pic1','')
        kw_proof_pic_link1 = request.POST.get('kw-proof_pic_link1', '')
        kw_proof_pic_url2 = request.FILES.get('proof_pic2','')
        kw_proof_pic_link2 = request.POST.get('kw-proof_pic_link2', '')
        kw_proof_vod_url1 = request.FILES.get('proof_vod','')
        kw_proof_vod_link1 = request.POST.get('kw-proof_vod_link1', '')

        report = Report()
        report.url = kw_profile
        report.nickname = kw_nickname
        report.name = kw_name

        report.youtube_url = kw_youtube
        report.twitch_url = kw_twitch
        report.afreeca_url = kw_afreecatv
        report.namu_url = kw_namu
        report.instagram_url = kw_instagram
        report.dcinside_url = kw_dcinside

        report.proof_pic1 = kw_proof_pic_url1
        report.proof_pic1_link = kw_proof_pic_link1
        report.proof_pic2 = kw_proof_pic_url2
        report.proof_pic2_link = kw_proof_pic_link2
        report.proof_vod = kw_proof_vod_url1
        report.proof_vod1_link = kw_proof_vod_link1

        report.save()

        account_num = len(Account.objects.all())

        context = {
            'kw_nickname' : kw_nickname,
            'kw_name' : kw_name,
            'kw_profile' : kw_profile,
            'kw_youtube' : kw_youtube,
            'kw_twitch' : kw_twitch,
            'kw_afreecatv' : kw_afreecatv,
            'kw_namu' : kw_namu,
            'kw_instagram' : kw_instagram,
            'kw_dcinside' : kw_dcinside,
            'kw_proof_pic_url1' : kw_proof_pic_url1,
            'kw_proof_pic_link1' : kw_proof_pic_link1,
            'kw_proof_pic_url2' : kw_proof_pic_url2,
            'kw_proof_pic_link2' : kw_proof_pic_link2,
            'kw_proof_vod_url1' : kw_proof_vod_url1,
            'kw_proof_vod_link1' : kw_proof_vod_link1,
            'account_num' : account_num,
            'error_occur' : False,
        }
        
        return render(request, 'hoxy/success.html', context)
    else : 
        return render(request, 'hoxy/success.html', {'error_occur' : True})