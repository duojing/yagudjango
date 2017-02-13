from django.contrib import admin
from project.models import Gujang, Block, Blockview

class GujangAdmin(admin.ModelAdmin):
    list_display=['name','logo','content','tip']

class BlockAdmin(admin.ModelAdmin):
    list_display=['block_name','block_img', 'block_info', 'block_tip']


admin.site.register(Block, BlockAdmin)
admin.site.register(Gujang, GujangAdmin)
admin.site.register(Blockview)
# Register your models here.
