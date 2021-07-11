from django.db import models

class Account(models.Model) : 
    puuid = models.CharField(primary_key=True, max_length=80)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    
class Profile(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_Profile",on_delete=models.CASCADE, db_column="puuid")
    url = models.ImageField(help_text="Profile Picture URL", upload_to="img/")

class Nickname(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_Nickname",on_delete=models.CASCADE, db_column="puuid")
    nickname = models.CharField(help_text="Account Nickname", max_length=40, blank=False, null=False)
    nickname_search = models.CharField(help_text="Account Nickname For Search", max_length=40, blank=False, null=False)

class Name(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_Name",on_delete=models.CASCADE, db_column="puuid")
    name = models.CharField(help_text="Account Name", max_length=80, blank=True, null=False)

class Sns(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_SNS",on_delete=models.CASCADE, db_column="puuid")
    youtube_url = models.URLField(help_text="Account Youtube URL",blank=False, null=True)
    twitch_url = models.URLField(help_text="Account Twitch URL",blank=False, null=True)
    afreeca_url = models.URLField(help_text="Account AfreecaTV URL",blank=False, null=True)
    namu_url = models.URLField(help_text="Account Namuwiki URL",blank=False, null=True)
    instagram_url = models.URLField(help_text="Account Instagram URL",blank=False, null=True)
    dcinside_url = models.URLField(help_text="Account DC Inside URL",blank=False, null=True)

class Proof(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_Proof",on_delete=models.CASCADE, db_column="puuid")
    proof_pic1 = models.ImageField(help_text="Account approving proof picture 1",upload_to="static/img/", null=False)
    proof_pic2 = models.ImageField(help_text="Account approving proof picture 2",upload_to="static/img/", null=True)
    proof_vod = models.FileField(help_text="Account approving proof video",upload_to="static/vod/", null=True)
    proof_pic1_link = models.URLField(help_text="Account approving proof picture 1 link to original",blank=False, null=False)
    proof_pic2_link = models.URLField(help_text="Account approving proof picture 2 link to original",blank=False, null=True)
    proof_vod1_link = models.URLField(help_text="Account approving proof video 1 link to original",blank=False, null=True)

class Verify(models.Model) : 
    puuid = models.ForeignKey("Account", related_name="account_on_Verify",on_delete=models.CASCADE, db_column="puuid")
    time_play_with = models.DateTimeField()
    champion_user = models.CharField(help_text="User Play Champion", max_length=40, blank=False, null=False)
    dealing_user = models.IntegerField(help_text="User Amount of dealing", blank=False, null=False)
    nickname_play_with = models.CharField(help_text="Nickname Play with User", max_length=40, blank=True, null=False)

class Report(models.Model) : 
    url = models.ImageField(help_text="Profile Picture URL", upload_to="temp/")
    nickname = models.CharField(help_text="Account Nickname", max_length=40, blank=False, null=False)
    name = models.CharField(help_text="Account Name", max_length=80, blank=True, null=False)

    youtube_url = models.URLField(help_text="Account Youtube URL",blank=False, null=True)
    twitch_url = models.URLField(help_text="Account Twitch URL",blank=False, null=True)
    afreeca_url = models.URLField(help_text="Account AfreecaTV URL",blank=False, null=True)
    namu_url = models.URLField(help_text="Account Namuwiki URL",blank=False, null=True)
    instagram_url = models.URLField(help_text="Account Instagram URL",blank=False, null=True)
    dcinside_url = models.URLField(help_text="Account DC Inside URL",blank=False, null=True)

    proof_pic1 = models.ImageField(help_text="Account approving proof picture 1",upload_to="temp/", null=False)
    proof_pic2 = models.ImageField(help_text="Account approving proof picture 2",upload_to="temp/", null=True)
    proof_vod = models.FileField(help_text="Account approving proof video",upload_to="temp/", null=True)
    proof_pic1_link = models.URLField(help_text="Account approving proof picture 1 link to original",blank=False, null=False)
    proof_pic2_link = models.URLField(help_text="Account approving proof picture 2 link to original",blank=False, null=True)
    proof_vod1_link = models.URLField(help_text="Account approving proof video 1 link to original",blank=False, null=True)

class Test(models.Model) : 
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    def __str__(self) : 
        return 'Test model'