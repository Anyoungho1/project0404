from config.default import *
from logging.config import dictConfig
SQLALCHEMY_DATABASE_URI="sqlite:///{}".format(
    os.path.join(BASE_DIR,'pybo.db')
)


SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY=b'\xe1\xd52\xf8\xe9\xa9\xfb\x82\x95\x16\\>!\xa0\xc8\x8f'

dictConfig({
        "version":1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s", 
            }
        },
        "handlers":{
            "file":{
                "level":"info",
                "class":"logging.handlers.RotatingFileHandler",
                "filename": os.path.join(BASE_DIR, 'logs/project0404.log'),
                "maxBytes": 1*1024*1024*5,
                "backupCount": 5,
                "formatter": "default"
            }
        },
        "root":{
            "level": "INFO", # debug-> warning->error->critical
            "handlers": ["file"]
        }
        
    })