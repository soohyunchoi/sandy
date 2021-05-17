from django.shortcuts import render
from .models import SurfSpot
from .serializers import *
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import io
# from rest_framework.parsers import JSONParse
# import requests


class SurfSpotListCreate(generics.ListCreateAPIView):
    queryset = SurfSpot.objects.all()
    serializer_class = SurfSpotSerializer

@api_view(['GET', 'POST'])
def surfspot_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        surfspots = SurfSpot.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(surfspots, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        serializer = SurfSpotSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data, 
        'count': paginator.count, 
        'numpage' : paginator.num_pages,
        'nextlink': '/api/surfspots/?page=' + str(nextPage),
        'prevlink': '/api/surfspots/?page=' + str(previousPage)})
    elif request.method == 'POST':
        serializer = SurfSpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def surfspots_detail(request, pk):
    try:
        customer = SurfSpot.objects.get(pk=pk)
    except SurfSpot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SurfSpotSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SurfSpotSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # (46054 = 'SANTA BARBARA'),
# # (46269 = 'SANTA CRUZ')
# @api_view()
# def FetchBuoyDataList(request, buoyID='46054'):
#     GATEWAY = 'http://127.0.0.1:5000/'
#     buoyDataResponseJSON = requests.get(GATEWAY+ f"api/buoytalk/{buoyID}/spec").json()
#     serializer = BuoyDataSerializer(data=buoyDataResponseJSON["data_points"], many=True)
#     serializer.is_valid()
#     return Response(data=serializer.validated_data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def FetchBuoyData(request, pk):
#     try:
#         buoyData = BuoyData.objects.get(pk=pk)
#     except BuoyData.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = BuoyDataSerializer(BuoyData)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = BuoyDataSerializer(BuoyData, data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         BuoyData.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)