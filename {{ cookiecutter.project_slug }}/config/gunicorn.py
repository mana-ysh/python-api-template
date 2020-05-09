import os

bind = '0.0.0.0:{}'.format(str(os.getenv('GNICORN_APP_PORT', 9876)))
workers = 1
