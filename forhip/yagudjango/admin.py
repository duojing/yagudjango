from django.contrib import admin
from yagudjango.models import Gujang, Block, Seat, Tag, Comment, Blockimg, Imgtext

class GujangAdmin(admin.ModelAdmin):
    list_display=['name','logo','content','tip']

class BlockAdmin(admin.ModelAdmin):
    list_display=['block_name','block_info', 'block_tip']

class SeatAdmin(admin.ModelAdmin):
    list_display = ['block','row','col','is_blind','photo']
    list_filter = ['block','is_blind']


admin.site.register(Block, BlockAdmin)
admin.site.register(Gujang, GujangAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Blockimg)
admin.site.register(Imgtext)