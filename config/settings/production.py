from .deployment import *  # noqa

# REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = (  # noqa F405
#     "config.authentication.CustomJWTAuthentication",
# )
DEBUG = True
ALLOWED_HOSTS = ["*"]


IS_PRODUCTION = True
USE_SMS = env.bool("USE_SMS", default=True)  # noqa F405
SEND_SMS_NOTIFICATION = False
