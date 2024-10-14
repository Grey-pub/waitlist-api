from django.contrib import admin
from django.urls import path
from .views import waitlist_collection, waitlist_view, waitlist_respond

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/create-waitlist", waitlist_collection, name="create waitlist"),
    path("api/view-waitlist", waitlist_view, name="view waitlist"),
    path("api/respond-waitlist", waitlist_respond, name="respond waitlist"),
]
