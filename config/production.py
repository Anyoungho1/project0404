from config.default import *

SQLALCHEMY_DATABASE_URI="sqlite:///{}".format(
    os.path.join(BASE_DIR,'pybo.db')
)


SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY=b'\xe1\xd52\xf8\xe9\xa9\xfb\x82\x95\x16\\>!\xa0\xc8\x8f'

