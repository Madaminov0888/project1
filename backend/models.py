from django.db import models


class BotUsers(models.Model):
    class Meta:
        verbose_name = "Bot user"
        verbose_name_plural = "Bot users"
    
    class Language(models.TextChoices):
        RU = "Ru"
        UZ = "Uz"

    lang = models.CharField(verbose_name="Tili", max_length=33, choices=Language.choices,null = True, default="Uz")    
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=55, null = True, default="-")


class Users(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        

    class Textchoice(models.TextChoices):
        TYPE_D = "National Visa (Type D)"
        TYPE_C = "National Visa (Type C)"
        RECONSIDERATION = "Reconsideration"

    class SubCategory(models.TextChoices):
        HIGHER_EDUCATION = "Higher education"
        TURKISH_citizens = "Turkish citizens - work permit"
        FOREIGNERS = "Foreigners - work permit"
        LONG_STAY = "Long-Stay others"
    
    name = models.CharField(verbose_name="Ismi", max_length=30, null = True, default="-")
    surname = models.CharField(verbose_name="Familiyasi", max_length=30, null = True, default="-")
    nationality = models.CharField(verbose_name="Irqi", max_length = 30, null = True, default = "-")
    passport_number = models.CharField(verbose_name="Passport raqami", max_length=55, null = True, default = "-")
    contact_number = models.CharField(verbose_name = "Telefon raqami", max_length=60, null = True, default="-")
    email = models.EmailField(null = True, default="-")
    appointment_category = models.CharField(verbose_name="Tayinlash toifasi", max_length=70, choices=Textchoice.choices, null = True, default="National Visa (Type D)")
    sub_category = models.CharField(verbose_name="Pastki kategoriya", max_length=100, choices=SubCategory.choices, null = True, default="Foreigners - work permit")
    visa_aplication_centre = models.CharField(verbose_name="Application", max_length=100, null = True, default="-")



class Matnlar(models.Model):
    class Meta:
        verbose_name = "Matn"
        verbose_name_plural = "Matnlar"

    location = models.CharField(max_length=40, null = True, default="-")
    title = models.CharField(max_length=50, null = True, default="-")
    text = models.TextField(verbose_name="Text", max_length=500, null = True, default="-")
    text_ru = models.TextField(verbose_name="Text Ru", max_length=500, null = True, default="-")

