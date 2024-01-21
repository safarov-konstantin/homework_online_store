from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = [
        'казино', 
        'криптовалюта', 
        'крипта', 
        'биржа', 
        'дешево', 
        'бесплатно', 
        'обман', 
        'полиция',
        'радар',
    ]

    def check_attribute(self, attribute):
        contains_forbidden_word = [word for word in self.forbidden_words if word in attribute.lower()] 
        if len(contains_forbidden_word) > 0:
            raise forms.ValidationError(f'В поле ввода запрещены слова: {", ".join(contains_forbidden_word)}')
        return attribute

    def clean_name(self):
        data = self.cleaned_data.get('name')
        return self.check_attribute(attribute=data)
    
    def clean_description(self):
        data = self.cleaned_data.get('description')
        return self.check_attribute(attribute=data)

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'image',
            'category',
            'price',
        )


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
