from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.decorators import action
from .models import Flat, Bill, Item, Feedback, Survey, Resident, FaMember, SurveyResult
from .serializers import FlatSerializer, BillSerializer, ItemSerializer, FeedbackSerializer, SurveySerializer, ResidentSerializer, FaMemberSerializer, SurveyResultSerializer
from rest_framework.parsers import MultiPartParser

class ResidentViewSet(viewsets.ViewSet,generics.UpdateAPIView, generics.CreateAPIView):
    queryset = Resident.objects.filter(is_active=True)
    serializer_class = ResidentSerializer
    parser_classes = [MultiPartParser, ]



class FlatViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class BillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Bill.objects.filter(payment_status='Paid')
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): #tra cứu hóa đơn
        queryset = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(bill_type__icontains=q)

        return queryset

class ItemViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FeedbackViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class SurveyViewSet(viewsets.ViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class FaMemberViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = FaMember.objects.all()
    serializer_class = FaMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class SurveyResultViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = SurveyResult.objects.all()
    serializer_class = SurveyResultSerializer