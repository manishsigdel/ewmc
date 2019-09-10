from django import forms

from nattest.models import Nattest
from usermessage.models import Usermessage


class UsermessageForm(forms.ModelForm):
    name = forms.CharField(min_length=4, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Name', 'data-rule': 'required',
               }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Your Email',
                                                           }))
    subject = forms.CharField(min_length=8,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Subject',
                                                            'data-rule': 'required',
                                                            }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'data-rule': 'required',
                                     'placeholder': 'Message'}))

    def __init__(self, *args, **kwargs):
        super(UsermessageForm, self).__init__(*args, **kwargs)

        # Focus on form field whenever error occurred
        errorList = list(self.errors)
        for item in errorList:
            self.fields[item].widget.attrs.update({'autofocus': ''})
            break

    class Meta:
        model = Usermessage
        fields = ['name', 'email', 'subject', 'message']


class NattestForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocapitalize': 'word'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocapitalize': 'word'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    testdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    GRADE_CHOICES = (
        ('N5', 'N5'),
        ('N4', 'N4'),
        ('N3', 'N3'),
        ('N2', 'N2'),
        ('N1', 'N1'),
    )
    grade = forms.ChoiceField(choices=GRADE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    testplace = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bankvoucher = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(NattestForm, self).__init__(*args, **kwargs)

        # Focus on form field whenever error occurred
        errorList = list(self.errors)
        for item in errorList:
            self.fields[item].widget.attrs.update({'autofocus': ''})
            break

    class Meta:
        model = Nattest
        fields = ['firstname', 'lastname', 'photo', 'testdate', 'grade', 'testplace', 'gender', 'dob', 'nationality', 'address', 'phonenumber', 'email', 'document', 'bankvoucher']
