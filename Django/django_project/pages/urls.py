from django.urls import path

from pages.views import home_view, log_view, base_view, team_view, mentors_view

urlpatterns = [
    path('', home_view, name='home'),
    path('log/', log_view, name='log'),
    path('base/', base_view, name='base'),
    path('team/', team_view, name='team'),
    path('mentors/', mentors_view, name='mentors'),

]
