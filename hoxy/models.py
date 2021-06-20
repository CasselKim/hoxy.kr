from django.db import models

class Account(models.Model) : 
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    
class Profile(models.Model) : 
    account_id = models.ForeignKey("Account", related_name="account_on_profile",on_delete=models.CASCADE)
    url = models.ImageField(help_text="Profile Picture URL", upload_to="")

class Nickname(models.Model) : 
    account_id = models.ForeignKey("Account", related_name="account_on_Nickname",on_delete=models.CASCADE, db_column="account_id")
    nickname = models.CharField(help_text="Account Nickname", max_length=40, blank=False, null=False)

class Name(models.Model) : 
    account_id = models.ForeignKey("Account", related_name="account_on_Name",on_delete=models.CASCADE, db_column="account_id")
    name = models.CharField(help_text="Account Name", max_length=80, blank=True, null=False)

class Sns(models.Model) : 
    account_id = models.ForeignKey("Account", related_name="account_on_Sns",on_delete=models.CASCADE, db_column="account_id")
    youtube_url = models.URLField(help_text="Account Youtube URL",blank=False, null=True)
    twitch_url = models.URLField(help_text="Account Twitch URL",blank=False, null=True)
    afreeca_url = models.URLField(help_text="Account AfreecaTV URL",blank=False, null=True)
    namu_url = models.URLField(help_text="Account Namuwiki URL",blank=False, null=True)
    instagram_url = models.URLField(help_text="Account Instagram URL",blank=False, null=True)
    dcinside_url = models.URLField(help_text="Account DC Inside URL",blank=False, null=True)

class Proof(models.Model) : 
    account_id = models.ForeignKey("Account", related_name="account_on_Proof",on_delete=models.CASCADE, db_column="account_id")
    proof_pic1 = models.ImageField(help_text="Account approving proof picture 1",upload_to="", null=False)
    proof_pic2 = models.ImageField(help_text="Account approving proof picture 2",upload_to="", null=True)
    proof_vod = models.FileField(help_text="Account approving proof video",upload_to="", null=True)
    proof_pic1_link = models.URLField(help_text="Account approving proof picture 1 link to original",blank=False, null=False)
    proof_pic2_link = models.URLField(help_text="Account approving proof picture 2 link to original",blank=False, null=True)
    proof_vod1_link = models.URLField(help_text="Account approving proof video 1 link to original",blank=False, null=True)