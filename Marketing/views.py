from django.shortcuts import render, redirect
from Marketing.models import contact, influencer_detail, brand_detail

# Create your views here.

def home(request):
    return render(request, 'marketing/home.html')

def about_us(request):
    return render(request, 'marketing/about_us.html')

def influencer(request):
    if request.method == "POST":
        fullname = request.POST.get('namefield', '')

        male = request.POST.get('Male')
        if male:
            male = True
        else:
            male = False

        female = request.POST.get('Female')
        if female:
            female = True
        else:
            female = False

        email = request.POST.get('emailfield', '')
        phone_no = request.POST.get('phone', '')
        date_of_birth = request.POST.get('dob', '')
        preferred_lang = request.POST.get('language', '')

        fb_url = request.POST.get('fb', '')
        insta_url = request.POST.get('instagram', '')
        tiktok_url = request.POST.get('tiktok', '')
        youtube_url = request.POST.get('youtube', '')

        technology = request.POST.get('Technology')
        sports = request.POST.get('Sports')
        gaming = request.POST.get('Gaming')
        educational = request.POST.get('Educational')
        entertainment = request.POST.get('Entertainment')
        travel = request.POST.get('Travel')
        motivational = request.POST.get('Motivational')
        beauty = request.POST.get('Beauty')
        lifestyle = request.POST.get('Lifestyle')
        health = request.POST.get('Health')
        cooking = request.POST.get('Cooking')

        if technology:
            technology = True
        else:
            technology = False
        
        if sports:
            sports = True
        else:
            sports = False
        
        if gaming:
            gaming = True
        else:
            gaming = False
        
        if educational:
            educational = True
        else:
            educational = False

        if entertainment:
            entertainment = True
        else:
            entertainment = False

        if travel:
            travel = True
        else:
            travel = False

        if motivational:
            motivational = True
        else:
            motivational = False

        if beauty:
            beauty = True
        else:
            beauty = False

        if lifestyle:
            lifestyle = True
        else:
            lifestyle = False

        if health:
            health = True
        else:
            health = False

        if cooking:
            cooking = True
        else:
            cooking = False

        details = influencer_detail(fullname=fullname, male=male, female=female, phone_no=phone_no, date_of_birth=date_of_birth, preferred_lang=preferred_lang, fb_url=fb_url, insta_url=insta_url, tiktok_url=tiktok_url, youtube_url=youtube_url, email=email, technology=technology, sports=sports, gaming=gaming, educational=educational, entertainment=entertainment, travel=travel, motivational=motivational, beauty=beauty, lifestyle=lifestyle, health=health, cooking=cooking)
        details.save()
    return render(request, 'marketing/influencer.html')

def brand(request):
    if request.method == "POST":
        fullname = request.POST.get('namefield', '')
        company = request.POST.get('companyfield', '')
        email = request.POST.get('emailfield', '')
        prod_desc = request.POST.get('productdesc', '')

        technology = request.POST.get('Technology')
        sports = request.POST.get('Sports')
        gaming = request.POST.get('Gaming')
        educational = request.POST.get('Educational')
        entertainment = request.POST.get('Entertainment')
        travel = request.POST.get('Travel')
        motivational = request.POST.get('Motivational')
        beauty = request.POST.get('Beauty')
        lifestyle = request.POST.get('Lifestyle')
        health = request.POST.get('Health')
        cooking = request.POST.get('Cooking')

        if technology:
            technology = True
        else:
            technology = False
        
        if sports:
            sports = True
        else:
            sports = False
        
        if gaming:
            gaming = True
        else:
            gaming = False
        
        if educational:
            educational = True
        else:
            educational = False

        if entertainment:
            entertainment = True
        else:
            entertainment = False

        if travel:
            travel = True
        else:
            travel = False

        if motivational:
            motivational = True
        else:
            motivational = False

        if beauty:
            beauty = True
        else:
            beauty = False

        if lifestyle:
            lifestyle = True
        else:
            lifestyle = False

        if health:
            health = True
        else:
            health = False

        if cooking:
            cooking = True
        else:
            cooking = False

        details = brand_detail(fullname=fullname,  company=company, email=email, prod_desc=prod_desc, technology=technology, sports=sports, gaming=gaming, educational=educational, entertainment=entertainment, travel=travel, motivational=motivational, beauty=beauty, lifestyle=lifestyle, health=health, cooking=cooking)
        details.save()
    return render(request, 'marketing/brand.html')

def contact_us(request):
    if request.method == "POST":
        fullname = request.POST.get('namefield', '')
        email = request.POST.get('emailfield', '')
        subject = request.POST.get('subjectfield', '')
        queries = request.POST.get('queries', '')
        details = contact(fullname=fullname,  email=email, subject=subject, queries=queries)
        details.save()
    return render(request, 'marketing/contact_us.html')