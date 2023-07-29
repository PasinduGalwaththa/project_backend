from django import forms
from django.contrib import admin
from .models import estate

# class EstateForm(forms.ModelForm):
#     new_teatype = forms.CharField(max_length=20, required=False)

#     class Meta:
#         model = estate
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['teatype'].widget = forms.Select(choices=self.get_teatype_choices())

#     def get_teatype_choices(self):
#         existing_choices = estate.objects.values_list('teatype', flat=True).distinct()
#         choices = [(choice, choice) for choice in existing_choices]
#         return choices

#     def clean_new_teatype(self):
#         new_teatype = self.cleaned_data.get('new_teatype')
#         if new_teatype and new_teatype not in dict(self.fields['teatype'].widget.choices):
#             return new_teatype
#         return None

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         new_teatype = self.cleaned_data.get('new_teatype')
#         if new_teatype:
#             instance.teatype = new_teatype
#             choices = list(self.fields['teatype'].widget.choices)
#             choices.append((new_teatype, new_teatype))
#             self.fields['teatype'].widget.choices = choices
#         if commit:
#             instance.save()
#         return instance

# class EstateAdmin(admin.ModelAdmin):
#     list_display = ('estatename', 'teatype')
#     list_editable = ('teatype',)

#     def get_form(self, request, obj=None, **kwargs):
#         kwargs['form'] = EstateForm
#         return super().get_form(request, obj, **kwargs)

# admin.site.register(estate, EstateAdmin)

admin.site.register(estate)
