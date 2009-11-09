from django.conf import settings

class PayPalSettingsError(Exception):
    """Raised when settings are incorrect."""
    
# Paypal Test
TEST = getattr(settings, "PAYPAL_TEST", True)

if not TEST:
    RECEIVER_EMAIL = settings.PAYPAL_RECEIVER_EMAIL
else:
    RECEIVER_EMAIL = settings.PAYPAL_TEST_RECEIVER_EMAIL

# API Endpoints.
POSTBACK_ENDPOINT = getattr(settings, "PAYPAL_ENDPOINT", 
            "https://www.paypal.com/cgi-bin/webscr")
SANDBOX_POSTBACK_ENDPOINT = getattr(settings, "PAYPAL_TEST_ENDPOINT", 
            "https://www.sandbox.paypal.com/cgi-bin/webscr"

# Images
IMAGE = getattr(settings, "PAYPAL_IMAGE", 
            "http://images.paypal.com/images/x-click-but01.gif")
SUBSCRIPTION_IMAGE = getattr(settings, "PAYPAL_SUBSCRIPTION_IMAGE",
            "https://www.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif")
SANDBOX_IMAGE = getattr(settings, "PAYPAL_TEST_IMAGE", 
            "https://www.sandbox.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif")
SUBSCRIPTION_SANDBOX_IMAGE = getattr(settings, "PAYPAL_SUBSCRIPTION_TEST_IMAGE", 
            "https://www.sandbox.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif")

            
if 'paypal.standard.pdt' in settings.INSTALLED_APPS
    try:
        if not TEST:
            IDENTITY_TOKEN = settings.PAYPAL_IDENTITY_TOKEN
        else:
            IDENTITY_TOKEN = settings.PAYPAL_TEST_IDENTITY_TOKEN
    except:
        raise PayPalSettingsError("You must set PAYPAL_IDENTITY_TOKEN in settings.py. Get this token by enabling PDT in your PayPal account.")


CERT = getattr(settings, "PAYPAL_PRIVATE_CERT", '')
PUB_CERT = getattr(settings, "PAYPAL_PUBLIC_CERT", '')
PAYPAL_CERT = getattr(settings, "PAYPAL_CERT", '')
CERT_ID = getattr(settings, "PAYPAL_CERT_ID", '')