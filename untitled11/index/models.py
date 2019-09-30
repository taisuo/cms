from django.db import models

# Create your models here.
class inadmin(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=8)
    email=models.CharField(max_length=50,null=True)
    lasttime=models.DateTimeField(null=True)
    registtime=models.DateTimeField(null=True)

    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "admin"


class inmenu(models.Model):
    menuname=models.CharField(max_length=32)
    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "menu"

class news(models.Model):
    catid=models.PositiveSmallIntegerField(max_length=5)
    title=models.CharField(max_length=8)
    title_font_colour=models.CharField(max_length=8,null=True)
    thumb=models.CharField(max_length=64,null=True)
    num=models.PositiveSmallIntegerField(max_length=5)

    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "news"

class innews_content(models.Model):
    newsid=models.PositiveSmallIntegerField(max_length=5)
    content=models.TextField(max_length=640)
    newstime = models.DateTimeField(null=True)
    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "news_content"

class inposition(models.Model):
    positionname=models.PositiveSmallIntegerField(max_length=5)

    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "inposition"

class inposition_content(models.Model):
    positionid=models.PositiveSmallIntegerField(max_length=5)
    newsid=models.PositiveSmallIntegerField(max_length=5)
    class Meta:  # 重命名
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "inposition_content"