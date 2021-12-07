from django.shortcuts import render
from rest_framework.decorators import api_view

from api.models import User
from api.serializers import api_serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse


@api_view(['GET'])
def get_active_users(request):
    if request.method == 'GET':
        user_data_object = User.objects.filter(active_status="Yes")
        print(user_data_object)
        user_data_object_serializer = api_serializer(user_data_object, many=True)
        return JsonResponse(user_data_object_serializer.data, safe=False)


@api_view(['PUT', 'GET'])
def user_update_and_fetch(request, email_id):
    if request.method == 'GET':
        user_data_object = User.objects.get(email_id=email_id)
        user_data_object_serializer = api_serializer(user_data_object)
        return JsonResponse(user_data_object_serializer.data)

    elif request.method == 'PUT':

        user = User.objects.get(email_id=email_id)
        user_data_object = JSONParser().parse(request)
        user_data_object_serializer = api_serializer(user, data=user_data_object)
        if user_data_object_serializer.is_valid():
            user_data_object_serializer.save()
            return JsonResponse(user_data_object_serializer.data)
        return JsonResponse(user_data_object_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_create_and_retreive(request):
    if request.method == 'GET':
        user_data_object = User.objects.all().order_by('education_qualification')
        user_data_object_serializer = api_serializer(user_data_object, many=True)
        return JsonResponse(user_data_object_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data_object = JSONParser().parse(request)
        user_data_object_serializer = api_serializer(data=user_data_object)
        if user_data_object_serializer.is_valid():
            user_data_object_serializer.save()
            return JsonResponse(user_data_object_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_data_object_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
