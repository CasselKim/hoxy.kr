# Generated by Django 3.1.3 on 2021-07-01 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoxy', '0006_auto_20210626_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(help_text='Profile Picture URL', upload_to='img/')),
                ('nickname', models.CharField(help_text='Account Nickname', max_length=40)),
                ('name', models.CharField(blank=True, help_text='Account Name', max_length=80)),
                ('youtube_url', models.URLField(help_text='Account Youtube URL', null=True)),
                ('twitch_url', models.URLField(help_text='Account Twitch URL', null=True)),
                ('afreeca_url', models.URLField(help_text='Account AfreecaTV URL', null=True)),
                ('namu_url', models.URLField(help_text='Account Namuwiki URL', null=True)),
                ('instagram_url', models.URLField(help_text='Account Instagram URL', null=True)),
                ('dcinside_url', models.URLField(help_text='Account DC Inside URL', null=True)),
                ('proof_pic1', models.ImageField(help_text='Account approving proof picture 1', upload_to='static/img/')),
                ('proof_pic2', models.ImageField(help_text='Account approving proof picture 2', null=True, upload_to='static/img/')),
                ('proof_vod', models.FileField(help_text='Account approving proof video', null=True, upload_to='static/vod/')),
                ('proof_pic1_link', models.URLField(help_text='Account approving proof picture 1 link to original')),
                ('proof_pic2_link', models.URLField(help_text='Account approving proof picture 2 link to original', null=True)),
                ('proof_vod1_link', models.URLField(help_text='Account approving proof video 1 link to original', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_play_with', models.DateTimeField()),
                ('champion_user', models.CharField(help_text='User Play Champion', max_length=40)),
                ('dealing_user', models.IntegerField(help_text='User Amount of dealing')),
                ('nickname_play_with', models.CharField(blank=True, help_text='Nickname Play with User', max_length=40)),
                ('account_id', models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, related_name='account_on_Verify', to='hoxy.account')),
            ],
        ),
    ]
