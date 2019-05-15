from .models import Mrt
from django import forms

class CreateForm(forms.Form):
    CHOICES = ((Mrt.FILTER_ONE, 'усредняющий фильтр'),
    (Mrt.FILTER_TWO, 'фильтр Гаусса'),
    (Mrt.FILTER_THREE, 'фильтр Винера'),
    (Mrt.FILTER_FOUR, 'медианный фильтр'))

    filter_id = forms.ChoiceField(label='Фильтры', choices=CHOICES)
    image = forms.FileField(label='Картинка')

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['filter_id'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Mrt
        fields = '__all__'
