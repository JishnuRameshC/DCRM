import csv,io
from django.shortcuts import render,redirect
import calendar
from django.contrib import messages
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event,Venue
from .form import VenueForm,EventForm,EventFormAdmin
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# imort user model in django
from django.contrib.auth.models import User
def venue_pdf_file(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica',15)

    lines = []
    venues = Venue.objects.all()
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zipcode)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email)
        lines.append('')
        lines.append('_____________________________________________________________')
        lines.append('')


    for line in lines:
        textob.textLine(line)
    

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True, filename='venue.pdf')

def venue_csv_file(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachement;filename= venue.csv'
    venues = Venue.objects.all()
    writer = csv.writer(response)
    writer.writerow(['venue name', 'address','zipcode','phone','web','email',])
    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zipcode, venue.phone, venue.web,venue.email])
    
    return response 


def venue_txt_file(request):
    response = HttpResponse(content_type = 'text/plain')
    response['Content-Disposition'] = 'attachement;filename= venue.txt'
    # line =['hello world\n', 'mf']
    venues = Venue.objects.all()
    line = [ ]
    for venue in venues:
        line.append(f'{venue.name}\n{venue.address}\n{venue.zipcode}\n{venue.phone}\n{venue.web}\n{venue.email}\n\n\n\n')
    
    response.writelines(line)
    return response

def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request('event deleted'))
        return redirect('event')
    else:
        messages.succes(request('you are not auterized to delete this event'))
        return redirect('event')

def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venue')

def update_event(request, event_id):
    venue = Event.objects.get(pk = event_id )
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=venue)

    else:
        form = EventForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('event')
    return render(request,'website/update_event.html',{'event':venue, 'form':form})


def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(request.POST) 
            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm 
        if 'submitted' in request.GET:
            submitted = True

    return render (request,'website/add_event.html',{'form':form,'submitted':submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id )
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venue')
    return render(request,'website/update_venue.html',{'venue':venue, 'form':form})


def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venue = Venue.objects.filter(name__contains = searched)
        return render(request,'website/search_venue.html',{'searched':searched,'venue':venue})
    else:
        return render(request,'website/search_venue.html')

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id )
    venue_owner = User.objects.get(pk = venue.owner)
    return render(request,'website/show_venue.html',
                  {'venue':venue, 'venue_owner':venue_owner})


def list_venue(request):
    venue = Venue.objects.all().order_by('name')
    return render(request,'website/venue.html',{'venue':venue})


def my_event(request):
    return render(request,'website/my_event.html',{})
def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            venu = form.save(commit=False)
            venu.owner = request.user.id
            venu.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:

            submitted = True

    return render (request,'website/add_venue.html',{'form':form,'submitted':submitted})

def event(request):
    events = Event.objects.all()
    return render(request,'website/even_list.html',
                  { "event":events})

def home(request,year=datetime.now().year,month= datetime.now().strftime('%B')):
    name = 'jishnu '
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int (month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')

    return render(request,'website/home.html',
                  {
                        "name":name,
                        'month':month,
                        'month_number':month_number,
                        'cal' : cal,
                        'current_year' : current_year,
                        'time' : time
                  })