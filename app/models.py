from django.db import models


class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name
    
class Technical(models.Model):
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')
    work = models.TextField('内容', max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name