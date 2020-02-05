from django.contrib import admin
from Marketing.models import contact, influencer_detail, brand_detail,application

# Register your models here.
admin.site.register(contact)
admin.site.register(influencer_detail)
admin.site.register(brand_detail)
admin.site.register(application)