from django.contrib import admin
from .models import BotUsers, Users, Matnlar


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "passport_number", "visa_aplication_centre"]

@admin.register(Matnlar)
class MatnlarAdmin(admin.ModelAdmin):
    list_display = ["location", "title", "text"]

@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ["username", "user_id", "lang"]