import pandas as pd
import os
from datetime import datetime
from django.utils import timezone
import csv
from tqdm import tqdm
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project.settings")
#2번 실행파일에 Django 환경을 불러오는 작업.
import django
django.setup()
from araapp.models import influencer_info, influencer_cate_region_bscore
df = pd.read_csv('./influencer_data.csv', encoding='utf-8')
df.drop('Unnamed: 0', axis=1, inplace=True)
print(df.columns)

# encoding 설정 필요
with open('./cate.csv', newline='', encoding='utf-8-sig') as csvfile:	
    data_reader = csv.DictReader(csvfile)

    for row in tqdm(data_reader):
        # print(row)
        influencer_cate_region_bscore.objects.create(	
            insta_id=row['insta_id'], 
            cate1=row['cate1'],
            cate2=row['cate2'], 
            cate3=row['cate3'], 
            region=row['region'], 
            commer_power=row['commer_power'],
            influ_power=row['influ_power']
         )
 
# encoding 설정 필요
with open('./influencer_data.csv', newline='', encoding='utf-8-sig') as csvfile:	
    data_reader = csv.DictReader(csvfile)

    for row in tqdm(data_reader):
        # print(row)
        influencer_info.objects.create(	
            file_id=row['file_id'], 
            insta_id=row['ID'], 
            content=row['content'],
            hashtags=row['hashtags'], 
            tag_id=row['tag_id'], 
            post_id=row['post_id'], 
            created_at=row['created_at'],
            insight=row['insight'],
            like_cnt=row['like_cnt'],
            comments=row['comments'],
            followers=row['followers'],
         )
    

 
    