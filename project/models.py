from django.db import models

class Gujang(models.Model):
    name = models.CharField(max_length=100,default='gujang')
    logo = models.ImageField(blank=True)
    content = models.TextField(help_text='구장 기본적인 정보 입력')
    basic = models.ImageField(blank=True)
    cheer = models.ImageField(blank=True)
    sight = models.ImageField(blank=True)
    etc = models.ImageField(blank=True)
    tip = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Block(models.Model):
    block = models.ForeignKey(Gujang, null=True)
    block_name = models.CharField(max_length=100)
    block_img = models.ImageField(blank=True)
    block_info = models.TextField(blank=True)
    block_tip = models.TextField(verbose_name='Tip!', help_text='블럭별 팁을 입력')

    def __str__(self):
        return self.block_name


class Blockview(models.Model):
    blocks = models.ForeignKey(Block, null=True)
    view_img = models.ImageField(blank=True)


# Create your models here.
