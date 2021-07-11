import urllib
import requests
import json

from datetime import datetime
from pytz import timezone

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.conf.urls import url
from django.utils import timezone
from .models import Account,Profile,Nickname,Name,Sns,Proof,Verify,Report,Test

admin.site.register([Account,Profile,Nickname,Name,Sns,Proof,Verify,Test])

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin) : 
    list_display = ('nickname','name')
    actions = ['accept','reject']

    def accept(self, request, queryset) : 
        report_object = queryset.get()

        with open('secrets.json', 'r') as f:
            json_data = json.load(f)
        
        RIOT_KEY = json_data['RIOT_KEY']
        headers = {"X-Riot-Token": RIOT_KEY,
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        encoded_name = urllib.parse.quote(report_object.nickname)
        puuid = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+encoded_name,headers=headers).json()['puuid']

        account = Account(puuid=puuid)
        account.create_time = timezone.localtime()
        account.modify_time = timezone.localtime()
        account.save()

        profile = Profile(puuid=account)
        profile.url = report_object.url
        profile.save()
        
        nickname = Nickname(puuid=account)
        nickname.nickname = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'+puuid, headers=headers).json()['name']
        nickname.nickname_search = nickname.nickname.replace(' ','').lower()
        nickname.save()

        name = Name(puuid=account)
        name.name = report_object.name
        name.save()

        sns = Sns(puuid=account)
        sns.youtube_url = report_object.youtube_url
        sns.twitch_url = report_object.twitch_url
        sns.afreeca_url = report_object.afreeca_url
        sns.namu_url = report_object.namu_url
        sns.instagram_url = report_object.instagram_url
        sns.dcinside_url = report_object.dcinside_url
        sns.save()

        proof = Proof(puuid=account)
        proof.proof_pic1 = report_object.proof_pic1
        proof.proof_pic1_link = report_object.proof_pic1_link
        proof.proof_pic2 = report_object.proof_pic2
        proof.proof_pic2_link = report_object.proof_pic2_link
        proof.proof_vod = report_object.proof_vod
        proof.proof_vod1_link = report_object.proof_vod1_link
        proof.save()

        report_object.delete()
    
    accept.short_description = "제보 승인하기"

    def reject(self, request, queryset) : 
        report_object = queryset.get()
        report_object.delete()
    
    reject.short_description = "제보 거부하기"
