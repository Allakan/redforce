from django.shortcuts import render
from rest_framework import generics
from .models import Advantages, AdvantagesImage, Feedback, Faq, Contacts, Rating, Subscription
from .serializers import AdvantagesSerializer, AdvantagesImageSerializer, FeedbackSerializer, FaqSerializer, ContactsSerializer, RatingSerializer, SubscribptionSerializer
# Create your views here.


class AdvantagesList(generics.ListCreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class AdvantagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class AdvantagesImageList(generics.ListCreateAPIView):
    queryset = AdvantagesImage.objects.all()
    serializer_class = AdvantagesImageSerializer

class AdvantagesImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvantagesImage.objects.all()
    serializer_class = AdvantagesImageSerializer

class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class ContactsList(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class ContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class SubscribptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscribptionSerializer

class SubscribptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscribptionSerializer