import time
import hashlib
import hmac
import base64
import pandas as pd
import requests
import openai
import re
from ast import literal_eval
class Signature:
    @staticmethod
    def generate(timestamp, method, uri, secret_key):
        message = "{}.{}.{}".format(timestamp, method, uri)
        hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
        
        hash.hexdigest()
        return base64.b64encode(hash.digest())
    

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = Signature.generate(timestamp, method, uri, secret_key)
    
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 
            'X-API-KEY': api_key, 'X-Customer': str(customer_id), 'X-Signature': signature}


def getresults(hintKeywords):

    BASE_URL = 'https://api.naver.com'
    API_KEY = '01000000003bfa1a83641bf52ae21cb7f04fbc7291f717c1a9a4d3c7e0c1647439c18e4ec2'
    SECRET_KEY = 'AQAAAAA7+hqDZBv1KuIct/BPvHKRPYQPw/ThInLs9ZWh4akRiw=='
    CUSTOMER_ID = '3022039'

    uri = '/keywordstool'
    method = 'GET'

    params={}

    params['hintKeywords']=hintKeywords
    params['showDetail']='1'

    r=requests.get(BASE_URL + uri, params=params, 
                 headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
    df = pd.DataFrame(r.json()['keywordList'])
    df = df.sort_values(by=['plAvgDepth'], ascending=[False])
    df = df[~df['relKeyword'].str.contains('남성|여성|남자|여자', case=False, na=False)]
    keyword_list = df['relKeyword'].tolist()[:5]
    return keyword_list

def main(keyword) : 
    openai.api_key ="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"
    hintKeywords=[keyword]
    resultdf = getresults(hintKeywords)
    
    keyword= keyword.replace("(", "").replace(")", "").replace(" ", "")
    system_message = f"너는 {resultdf} 이 키워드 중에 브랜드명을 제외하고, 광고에 관련된 키워드들만 선택해서 {keyword}을 광고하는데 효과적인 가이드라인을 생성하는 인공지능 모델이야"
    user_message = f"다음과 같은 딕셔너리 구조로 제공해줘. {{'제목': '제목 내용', '목차': '목차 내용', '키워드': '키워드 내용'}}"
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": system_message},  
        {"role": "user", "content": user_message}
        ]
    )
    text = completion.choices[0].message.content
    print(text)
    if text.lstrip().replace('\n', '').startswith("{"):
        try :
            text = literal_eval(text)
            return text
        except Exception as e:
            text = re.sub(r"'", "'''", text)
            text = literal_eval(text)
            return text
    else:
        if '{' in text:
            try :
                pattern = r'{(.*?)}'
                match = re.search(pattern, text, re.DOTALL)
                text = literal_eval(match.group(0))
                return text
            except Exception as e:
                text = re.sub(r"'", "'''", text)
                text = literal_eval(text)
                return text          

        