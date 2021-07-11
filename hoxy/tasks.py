# Create your tasks here
from __future__ import absolute_import, unicode_literals

import urllib
import requests
import json
import time
from datetime import datetime
#from pytz import timezone

from celery import shared_task
from django.utils import timezone
from .models import Account, Nickname, Test

@shared_task
def db_update():
    with open('secrets.json', 'r') as f:
            json_data = json.load(f)
            
    RIOT_KEY = json_data['RIOT_KEY']
    headers = {"X-Riot-Token": RIOT_KEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    for _ in range(20) : 
        account_list = Account.objects.all()
        for account in account_list : 
            recent_name = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'+account.puuid,headers=headers).json()['name']
            nickname_object = Nickname.objects.get(puuid=account)
            if recent_name.replace(' ','').lower() != nickname_object.nickname_search : 
                continue
            else : 
                nickname_object.nickname = recent_name
                nickname_object.nickname_search = recent_name.replace(' ','').lower()
                nickname_object.save()
                account.modify_time = timezone.localtime()
                account.save()

        time.sleep(10)