from django.urls import path
from . import views

urlpatterns = [
    # GET URLs
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('team/', views.TeamListView.as_view(), name='team-list'),
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    
    # POST URLs
    path('orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('followers/create/', views.FollowerCreateView.as_view(), name='follower-create'),
    path('contact/create/', views.ContactCreateView.as_view(), name='contact-create'),
]
