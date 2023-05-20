from django import forms
from django.forms import ModelForm
from  .models import Venue,Event


# admin EventForm
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ("name","event_date","venue","manager","participats","description")
        widgets = {
            "name": forms.TextInput(attrs={'class':"form-control", 'placeholder':'enter name'}),
            "event_date": forms.TextInput(attrs={'class':'form-control', 'placeholder':'event date YYYY-MM-DD HH:MM:SS '}),
            "venue": forms.Select(attrs={'class':'form-select','placeholder':' venue' }),
            
            "manager": forms.Select(attrs={'class':'form-select', 'placeholder':''}),
            "participats": forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':''}),
            "description": forms.Textarea(attrs={'class':'form-control', 'placeholder':''})
        }
        labels = {
            "name": ' ',
            "event_date": '',
            "participats": '',
            "venue":'venue',
            "description":'',
        }

# user event form

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name","event_date","venue","participats","description")
        widgets = {
            "name": forms.TextInput(attrs={'class':"form-control", 'placeholder':'enter name'}),
            "event_date": forms.TextInput(attrs={'class':'form-control', 'placeholder':'event date YYYY-MM-DD HH:MM:SS '}),
            "venue": forms.Select(attrs={'class':'form-select', }),
            
            
            "participats": forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':''}),
            "description": forms.Textarea(attrs={'class':'form-control', 'placeholder':''})
        }
        labels = {
            "name": ' ',
            "event_date":'',
            "venue": 'venue',
            "participats": '',
            "description":'',

        }




class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("name","address","zipcode","phone","web","email")
        widgets = {
            "name": forms.TextInput(attrs={'class':"form-control", 'placeholder':'enter name'}),
            "address": forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),
            "zipcode": forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcodee'}),
            "phone": forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone no'}),
            "web": forms.TextInput(attrs={'class':'form-control', 'placeholder':' link'}),
            "email": forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter email'})
        }
        labels = {
            "name": ' ',
            "address":'',
            "zipcode":'',
            "phone":'',
            "web":'',
            "email":'',


            
        }

        
