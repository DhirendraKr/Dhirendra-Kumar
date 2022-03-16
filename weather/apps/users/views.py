from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import  City
from apps.users.serializers import CitySerializer
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import json

@api_view(['GET'])
def city_list(request):
    try:
        queryset =  City.objects.all()
        serialized = CitySerializer(queryset, many = True, context={'request':request})
        return  Response({"msg": "Success", "city": serialized.data}, 200)
    except Exception as e:
        return Response({"msg": str(e), "city":[]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def city_create(request):
    city_name = request.data.get('city_name')
    if(not city_name):
        return Response({"msg": "Can't be empty city name"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = City()
        user.city_name = city_name
        user.save()
        return Response({"msg":'Success'}, 201)
    except Exception as e:
        return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def city_update(request, city_id):
    city_name = request.data.get('city_name')
    if(not city_name):
        return Response({"msg": "Can't be empty city name"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = City.objects.get(city_id=city_id)
        user.city_name = city_name
        user.save()
        return Response({"msg":'Success'}, 200)
    except Exception as e:
        return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def city_delete(request, city_id):
    try:
        City.objects.get(city_id=city_id).delete()
        return Response({"msg":'Success'}, 200)
    except Exception as e:
        return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def weather_forecast_api(request, city_id):
    try:
        user = City.objects.get(city_id=city_id)
    except Exception as e:
        return Response({"cod": "200"}, 400)
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={user.city_name}&limit=4&appid=2261ba0108886628e6e7704689d024ec"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(json.loads(response.text), 200)
    except Exception as e:
        return Response({"cod": "200"}, 400)


def weather_forecast(request):
    resp = {}
    resp['city_list'] = City.objects.all()
    return render(request, 'weather_forecast.html', resp)


def balance_parenthesis_string():
    p_string = "([{}])"
    result = []
    for p in p_string:
        if p in ["(", "{", "["]:
            result.append(p)
        else:
            if not result:
                return False
            p_string_list = result.pop()
            if p_string_list == '(':
                if p != ")":
                    return False
            if p_string_list == '{':
                if p != "}":
                    return False
            if p_string_list == '[':
                if p != "]":
                    return False
    if result:
        return False
    return True
