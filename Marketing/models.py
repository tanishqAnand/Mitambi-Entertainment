from django.db import models

class contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    queries = models.CharField(max_length=200)

    def __str__(self):
        return (self.email)


class influencer_detail(models.Model):
    fullname = models.CharField(max_length=50)
    male = models.BooleanField(default=False, blank=True)
    female = models.BooleanField(default=False, blank=True)
    email = models.EmailField()
    phone_no = models.CharField(max_length=13)
    date_of_birth = models.DateField()
    preferred_lang = models.CharField(max_length=20, blank=True)
    
    fb_url = models.URLField(blank=True)
    insta_url = models.CharField(max_length=30, blank=True)
    tiktok_url = models.CharField(max_length=30, blank=True)
    youtube_url = models.URLField(blank=True)

    technology = models.BooleanField(default=False, blank=True)
    sports = models.BooleanField(default=False, blank=True)
    gaming = models.BooleanField(default=False, blank=True)
    educational = models.BooleanField(default=False, blank=True)
    entertainment = models.BooleanField(default=False, blank=True)
    travel = models.BooleanField(default=False, blank=True)
    motivational = models.BooleanField(default=False, blank=True)
    beauty = models.BooleanField(default=False, blank=True)
    lifestyle = models.BooleanField(default=False, blank=True)
    health = models.BooleanField(default=False, blank=True)
    cooking = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return (self.fullname)


class brand_detail(models.Model):
    fullname = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    prod_desc = models.CharField(max_length=500)

    technology = models.BooleanField(default=False, blank=True)
    sports = models.BooleanField(default=False, blank=True)
    gaming = models.BooleanField(default=False, blank=True)
    educational = models.BooleanField(default=False, blank=True)
    entertainment = models.BooleanField(default=False, blank=True)
    travel = models.BooleanField(default=False, blank=True)
    motivational = models.BooleanField(default=False, blank=True)
    beauty = models.BooleanField(default=False, blank=True)
    lifestyle = models.BooleanField(default=False, blank=True)
    health = models.BooleanField(default=False, blank=True)
    cooking = models.BooleanField(default=False, blank=True)

    influencer_choice = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname

class application(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    skills = models.TextField(max_length=200)

    def __str__(self):
        return self.name