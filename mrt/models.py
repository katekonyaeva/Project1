from django.db import models

def upload_path_handler(instance, filename):
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
    tr = {ord(a):ord(b) for a, b in zip(*symbols)}
    return "mrt/{id}/{file}".format(id=instance.id, file=filename.translate(tr))

class Mrt (models.Model):
    FILTER_ONE = 1
    FILTER_TWO = 2
    FILTER_THREE = 3
    FILTER_FOUR = 4

    status_id = models.IntegerField(db_index=True)
    image = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)

