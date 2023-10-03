#this file contains sensitive information like django secret key
#edit this according to your requirement

class Django_Secrets:
    def __init__(self):
        self.key = "django-insecure-k1kop%yct&in5o@h!#%#87snw!kq**rc#r573h(t&4r0yu@_!z"


class Oauth_Secrets:
    def __init__(self):
        self.consumer_key = "7tTbk2WXcY8b8EgL2bnklqcw8"
        self.consumer_secret = "Kni0WU7ehhimgQZXe03QoQ7m4YpkXVdsr5LnKtG4JBpTd3F07y"
        self.access_token = "396530756-n8tOeZdKj04chWVTSKOQcNF6XCqhFMnX6GSktCst"
        self.access_token_secret = "LcbG4zI4K7sUtDLJ6bqemqjQxZnjJn6z0wh7YQLTLAMhm"

class Server_Url:
    def __init__(self):
        self.dev_server = "192.168.20.151:8000"
        self.test_server = "192.168.20.151:81"
        self.live_server = "41.60.204.194:81"

class Email_configs:
    def __init__(self):
        self.sendgrid_api_api = "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"
        self.account_sid = 'AC550c36ad55f97c144c194b6c69c2df12'
        self.auth_token = '5f012c04563d7062207e061e7df90ca6'


class SMS_configs:
    def __init__(self):
        self.sendgrid_api_api = "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"
        self.account_sid = 'AC550c36ad55f97c144c194b6c69c2df12'
        self.auth_token = '7ad28c56b452cbfe5747c5a2dcf20ef0'

# DATABASESLiveTest = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'zebs_test',
#         'HOST': '192.168.100.246',
#         'PORT': '5432',
#         'USER': 'bitnami',
#         # 'PASSWORD': '42ad7aa197' Ishe Dev
#         'PASSWORD': '7f6812fb09'
#     }
# }
# DATABASESDEVSERVER = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'zebs_test',
#         'HOST': '',
#         'PORT': '5432',
#         'USER': 'ishe',
#         'PASSWORD': '@Dmin1234'
#     }
# }
# DATABASESOLDEVMYSL = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangostack',
#         'HOST': '',
#         'PORT': '3310',
#          'USER': 'root',
#         'PASSWORD': 'toor'
#         # 'USER': 'bitnami',
#         # 'PASSWORD': '2a45c03996'
#     }
# }

# EXAMPLE_DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangostack',
#         'HOST': '',
#         'PORT': '3307',
#         'USER': 'bitnami',
#         'PASSWORD': '6d4f00c5c7'
#     }
# }

# EXAMPLE_DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
