from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('deletebook/<int:pk>', views.DeleteBook.as_view(), name='bookdelete'),
    path('updatebook/<int:pk>', views.UpdateBook.as_view(), name= 'bookupdate'),
]
