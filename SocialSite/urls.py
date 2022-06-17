from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('registration.urls')),
	path('', include('account.urls')),
	path('', include('dialogs.urls')),
	path('', include('posts.urls')),
]
