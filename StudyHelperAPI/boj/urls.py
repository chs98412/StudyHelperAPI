from django.urls import path,include
from .views import createMember,getMember,deleteMember,getAll

urlpatterns = [
    path('createMember/', createMember),
    path('getMember/', getMember),
    path('deleteMember/', deleteMember),
    path('getAll/', getAll),

]
