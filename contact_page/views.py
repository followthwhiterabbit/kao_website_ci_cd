from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404

from django.core.mail import send_mail
from django.conf import settings
import re, random
from validate_email import validate_email

from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


def contact_func(request, ):
    template = loader.get_template("contact_page/contact_page.html")
    context = {
        "contact":"contact_us",
        }

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        first_name = request.POST['first_name']
        second_name = request.POST['surname']
        captcha_response = request.POST.get('g-recaptcha-response', '')


        #captcha_secret_key = settings.RECAPTCHA_PRIVATE_KEY
        #recaptcha = ReCaptchaField(captcha_secret_key)
        #is_captcha_valid = recaptcha.clean(captcha_response)



        return_message = f"Thank you for reaching out to us {first_name} {second_name} ! We appreciate your interest in Kao Metrology. Our team has received your enquiry, and we are working diligently to provide you with the information you need.\n\n" \
            f"In the meantime, you may find answers to some common questions on our Frequently Asked Questions (FAQ) page: [Insert Link].\n\n" \
            f"We understand that your time is valuable, and we aim to respond to your inquiry as quickly as possible. If you have any urgent matters, please don't hesitate to contact us directly at +48 451033668.\n\n" \
            f"We appreciate your patience and look forward to assisting you. If there's anything else you'd like to add or specify, feel free to respond to this email.\n\n" \
            "Wishing you the best,\n\n" \
            "Kaan Karaalioglu\n" \
            "Software Engineer & Customer Service Representative\n" \
            "Kao Metrology\n" \
            "kaan.karaalioglu@kaometrology.com"


        send_mail(
        'FORM INQUIRY', #title, 
        return_message,
        'kaan.karaalioglu@kaometrology.com',
        [request.POST['email']], #receiver email
        fail_silently=False, 
    )

    #else:
        #context['captcha_error'] = "Captcha validation failed. Please try again."
        


    return HttpResponse(template.render(context, request))


    

