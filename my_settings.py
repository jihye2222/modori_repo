#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        # 'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'modori_design', #2
        'USER': 'admin', #3                      
        'PASSWORD': 'indj2020#',  #4              
        'HOST': 'dev-indj.cw7ggpqhhqne.ap-northeast-2.rds.amazonaws.com',   #5                
        'PORT': '3306', #6
    }
}

SECRET_KEY = 'django-insecure-x+&#nn&qy)*=@zzy$vaq8o1k0t84z!h1qixro3uoi22@4!91i)'
