from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:year>/<str:month>/',views.home,name="home"),
    path('event',views.event, name = "event"),
    path('add_venue', views.add_venue, name= 'add-venue'),
    path('list_venue', views.list_venue, name= 'list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name= 'show-venue'),
    path('search_venue', views.search_venue, name= 'search-venue'),
    path('update_venue/<venue_id>', views.update_venue, name= 'update-venue'),
    path('add_event', views.add_event, name= 'add-event'),
    path('update_event/<event_id>', views.update_event, name= 'update-event'),
    path('delete_event/<event_id>', views.delete_event, name= 'delete-event'),
    path('delete_venue/<venue_id>', views.delete_venue, name= 'delete-venue'),
    path('venue_txt_file', views.venue_txt_file, name= 'venue-txt-file'),
    path('venue_csv_file', views.venue_csv_file, name= 'venue-csv-file'),
    path('ven11ue_pdf_file', views.venue_pdf_file, name= 'venue-pdf-file'),
    path('my_events',views.my_events, name = "my_events"),

]
