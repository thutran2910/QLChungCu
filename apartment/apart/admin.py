from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import Resident, Flat, Bill, Item, Feedback, Survey, FaMember
from django import forms
from django.urls import path

class MyApartAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG QUẢN LÝ CHUNG CƯ'


admin_site = MyApartAdminSite(name='myAdmin')


admin_site.register(Flat)
admin_site.register(Bill)
admin_site.register(Item)
admin_site.register(Feedback)
admin_site.register(Survey)
admin_site.register(FaMember)