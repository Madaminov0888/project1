import config
from backend.models import Users, Matnlar


def parse_find(location, lang):
    matn_obj = Matnlar.objects.filter(location = location)[0]
    if lang == "Uz":
        text = matn_obj.text
    else:
        text = matn_obj.text_ru
    return text

