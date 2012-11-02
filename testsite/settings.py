import os, sys
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('..'))

SITE_ID = 1

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
CURRENT_PATH = os.getcwd()

DEBUG = True
LOCAL = DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Test User', 'test@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CURRENT_PATH, 'database.sqlite')
    }
}

if DEBUG:
    EMAIL_HOST_USER = 'test@gmail.com'
    EMAIL_HOST = '127.0.0.1'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = "%s/%s/" % (ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

STATIC_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7j6o^y6#w@#067^-dr)h_)*^^@b&mgmd@1_y309w+)rk!4p^0!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'testsite.urls'

TEMPLATE_DIRS = (
    "%s/%s/" % (ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'tinymce',
    'emailer',
    'south',
    'testapp',
)

#TINYMCE_SPELLCHECKER = False
TINYMCE_JS_URL = "%sjs/tiny_mce/tiny_mce_src.js" % MEDIA_URL
TINYMCE_COMPRESSOR = False
USE_COMPRESSOR = False
TINYMCE_USE_TEMPLATES = False

TINYMCE_DEFAULT_CONFIG = {
    'theme' : "advanced",
    'plugins' : "autolink,lists,spellchecker,pagebreak,style,layer,table,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    
    'document_base_url' : "/",
    'relative_urls' : False,
    'convert_urls': False,
    'strict_loading_mode': 1,
    
    #Theme options
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2' : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    'theme_advanced_buttons4' : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : False,

    #Skin options
    'skin' : "o2k7",
    'skin_variant' : "silver",
    
    'template_external_list_url' : "emailer/templates/",

}

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '''%(levelname)s %(asctime)s %(module)s %(process)d
                %(thread)d %(message)s'''
                },
            'simple': {
                'format': '%(levelname)s %(message)s'
                }
            },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
                }
            },
        'loggers': {
            'emailer': {
                'handlers': ['console'],
                'level': 'DEBUG'
                }
            }
        }

