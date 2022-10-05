import config
from backend.models import Users, Matnlar


def parse_find(location, lang):
    matn_obj = Matnlar.objects.filter(location = location)[0]
    if lang == "Uz":
        text = matn_obj.text
    else:
        text = matn_obj.text_ru
    return text


def parse_data(location, lang):
    objs = Matnlar.objects.filter(location = location)
    for obj in objs:
        buttons = []
        for button in obj.buttons.all():
            buttons.append(button)
        if lang == 'Uz':
            text = obj.text
        else:
            text = obj.text_ru
        dct_data = {"text": text,"row_num" : obj.row_num, "buttons" : buttons}
    return dct_data
    

