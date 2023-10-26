from django.db import models

class influencer_info(models.Model):
    idx = models.AutoField(primary_key=True)
    file_id = models.IntegerField(blank=True, null=True)
    insta_id = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()
    hashtags = models.TextField()
    tag_id = models.TextField()
    post_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    insight = models.IntegerField(default=0)
    like_cnt = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    class Meta:
        managed = False  # 이 모델은 데이터베이스 테이블을 관리하지 않음
        db_table = 'influencer_info'  # 외부 테이블의 이름을 지정
        
class influencer_cate_region_bscore(models.Model):
    idx = models.AutoField(primary_key=True)
    insta_id = models.CharField(max_length=50, blank=True, null=True)
    cate1 = models.CharField(max_length=100, blank=True, null=True)
    cate2 = models.CharField(max_length=100, blank=True, null=True)
    cate3 = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    commer_power = models.IntegerField(blank=True, null=True)
    influ_power = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False  # 이 모델은 데이터베이스 테이블을 관리하지 않음
        db_table = 'influencer_cate_region_bscore'  # 외부 테이블의 이름을 지정