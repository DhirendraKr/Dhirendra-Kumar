from django.urls import re_path
from apps.users.views import city_list, city_create, city_update, city_delete, weather_forecast, \
    weather_forecast_api

app_name = 'user'
urlpatterns = [
    re_path('city/list/', city_list, name="city list"),
    re_path('city/create/', city_create, name="city create"),
    re_path('city/update/(?P<city_id>\d+)/', city_update, name="city update"),
    re_path('city/delete/(?P<city_id>\d+)/', city_delete, name="city delete"),
    re_path('weather/forecast/', weather_forecast, name="weather forecast"),
    re_path('weather/(?P<city_id>\d+)/', weather_forecast_api, name="weather forecast api"),
]