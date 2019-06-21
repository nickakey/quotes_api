from django.shortcuts import render
from rest_framework import viewsets
from .models import QuoteModel
from .serializers import QuoteSerializer

# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = QuoteModel.objects.all()
    serializer_class = QuoteSerializer
