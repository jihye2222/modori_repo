from django.db.models import F, ExpressionWrapper, IntegerField, Case, When, Value, Q,FloatField
from araapp.models import influencer_cate_region_bscore
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Sum
from araapp.api import main
import pandas as pd
local_list = ['제주도',
                '전라북도',
                '광주광역시',
                '전라남도',
                '대전광역시',
                '충청북도',
                '충청남도',
                '서울특별시',
                '인천광역시',
                '경기도',
                '대구광역시',
                '울산광역시',
                '부산광역시',
                '경상북도',
                '경상남도',
                '강원도'] 

def calculate_local_score(influencer_region, input_local):
    if influencer_region == input_local:
        return 100
    diff = abs(local_list.index(influencer_region) - local_list.index(input_local))
    if diff == 1:
        return 80
    if 2 <= diff <= 7:
        return 70
    return 50

def calculate_category_score(category, influencer):
    if influencer['cate3'] == category:
        return 50
    if influencer['cate2'] == category:
        return 75
    if influencer['cate1'] == category:
        return 100
    return 0

def search(request):
    if 'local' in request.GET and 'category' in request.GET:
        input_local = request.GET['local']
        category = request.GET['category']

        if input_local not in local_list:
            return JsonResponse({"message": "Invalid 'local' parameter."}, status=400)

        influencer_data = influencer_cate_region_bscore.objects.values(
            'insta_id', 'cate1', 'cate2', 'cate3', 'region', 'commer_power', 'influ_power'
        )

        results = []

        for influencer in influencer_data:
            region_score = calculate_local_score(influencer['region'], input_local)
            category_score = calculate_category_score(category, influencer)
            sum_score = (region_score + category_score + influencer['commer_power'] + influencer['influ_power']) / 4

            results.append({
                "insta_id": influencer['insta_id'],
                "commer_power": influencer['commer_power'],
                "influ_power": influencer['influ_power'],
                "cate_score": category_score,
                "region_score": region_score,
                "sum_score": sum_score
            })

        results.sort(key=lambda x: x['sum_score'], reverse=True)
        first_five_rows = results[:5]

        return JsonResponse(first_five_rows, status=201, safe=False)
    
    elif 'keyword' in request.GET:
        keyword = request.GET['keyword']  
        ad = main(keyword)
        return JsonResponse(ad, status=status.HTTP_201_CREATED,safe=False)
