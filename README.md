# Getting Started

### Description
Admin custom filter package is a package will let you customize the view for the data in admin panel for each model dynamically.

### Why this package has been developed ?

Basically when you want to add custom filters, custom searches, and custom list displays, You need to add the values you want in hard coded. But if someone uses the admin panel and he has no technical knowledge to update the code. He will ask the developer each time to update the codes and wait the development process to finish.

### How this package will benefit ?
1. The admin custom filter package will help to play around with all models' fields dynamically. So, any update in the filter will be reflected directly and immediately in the platform.
2. Let say there are more than one admin in the platform, each one of them will have its unique filter. So, no overlap between them.

### What you need to do ?
1. Install the package
```
pip install admin-custom-filter
```
2. Add the app name in installed apps in settings.py and configure the templates <br> Make sure to have APP_DIRS to True and add BASE_DIR / "admin_custom_filter" / "templates" to DIRS list
```
INSTALLED_APPS = [
    'admin_custom_filter',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "admin_custom_filter" / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
3. After installing the package, make sure to have AUTH_USER_MODEL from the settings file.
```
EX:
inside settings.py
AUTH_USER_MODEL = "authentication.user"
```
4. Run migration
```
python manage.py migrate
OR
python3 manage.py migrate
```
5. Add the custom filter class to the models you want as the parent class.
```
Ex:
class Countries(AdminCustomFilter):
    pass
```
6. Save and go to the admin panel. Then select the model that has the admin custom filter.
7. You will see button Custom filter.