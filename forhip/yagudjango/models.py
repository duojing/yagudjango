from django.db import models

class Gujang(models.Model):
    name = models.CharField(max_length=100,default='gujang')
    logo = models.ImageField(blank=True)
    content = models.TextField(help_text='구장 기본적인 정보 입력')
    basic = models.ImageField(blank=True)
    cheer = models.ImageField(blank=True)
    sight = models.ImageField(blank=True)
    sight_real = models.ImageField(blank=True)
    sight_overall = models.ImageField(blank=True)
    etc = models.ImageField(blank=True)
    tag_at = models.ManyToManyField('Tag', blank=True)
    tip = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Block(models.Model):
    stadium = models.ForeignKey(Gujang, null=True, verbose_name='구장')
    block_name = models.CharField(max_length=100)
    block_point = models.CharField(max_length=200, blank=True,
    help_text='해당 블럭의 좌표를 입력해주세요')
    block_info = models.TextField(blank=True)
    block_tip = models.TextField(verbose_name='Tip!', help_text='블럭별 팁을 입력')

    def __str__(self):
        return self.block_name

    def get_seat_list(self):
        seat_dict = { (seat.row, seat.col):seat for seat in self.seat_set.all() }
        max_row = max(row for (row, col) in seat_dict.keys())
        max_col = max(col for (row, col) in seat_dict.keys())
        seat_list = []
        for row_idx in range(max_row):
            row_list = []
            for col_idx in range(max_col):
                key = (row_idx, col_idx)
                seat = seat_dict.get(key, None)
                row_list.append((row_idx, col_idx, seat))
            seat_list.append(row_list)
        return seat_list

class Blockimg(models.Model):
    blocks = models.ForeignKey(Block)
    block_img = models.ImageField()

class Imgtext(models.Model):
    text = models.OneToOneField(Blockimg)
    img_text = models.TextField(blank=True)

class Seat(models.Model):
    block = models.ForeignKey(Block)
    row = models.PositiveIntegerField()
    col = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return '{}행 {}열'.format(self.row, self.col)

    class Meta:
        unique_together = [
            ('block','row','col'),
        ]

class Tag(models.Model):
    tag_tip = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_tip

class Comment(models.Model):
    post = models.ForeignKey(Block)
    message = models.TextField()