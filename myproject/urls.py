"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp.views import AdvantagesList, AdvantagesDetail
from myapp.views import AdvantagesImageList, AdvantagesImageDetail
from myapp.views import FeedbackList, FeedbackDetail
from myapp.views import FaqList, FaqDetail
from myapp.views import ContactsList, ContactsDetail
from myapp.views import RatingList, RatingDetail
from myapp.views import SubscribptionList, SubscribptionDetail
from myapp.views import SubscribeGreenList, SubscribeGreenDetail

urlpatterns = [
    path('advantages/', AdvantagesList.as_view(), name='advantages_list'),
    path('advantages/<int:pk>/', AdvantagesDetail.as_view(), name='advantages_detail'),
    path('advantagesimage/', AdvantagesImageList.as_view(), name='advantagesimage_list'),
    path('advantagesimage/<int:pk>/', AdvantagesImageDetail.as_view(), name='advantagesimage_detail'),
    path('feedback/', FeedbackList.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetail.as_view(), name='feedback_detail'),
    path('faq/', FaqList.as_view(), name='faq_list'),
    path('faq/<int:pk>/', FaqDetail.as_view(), name='faq_detail'),
    path('contacts/', ContactsList.as_view(), name='contacts_list'),
    path('contacts/<int:pk>/', ContactsDetail.as_view(), name='contacts_detail'),
    path('rating/', RatingList.as_view(), name='rating_list'),
    path('rating/<int:pk>/', RatingDetail.as_view(), name='rating_detail'),
    path('subscribption/', SubscribptionList.as_view(), name='subscribption_list'),
    path('subscribption/<int:pk>/', SubscribptionDetail.as_view(), name='subscribption_detail'),
    path('subscribegreen/', SubscribeGreenList.as_view(), name='subscribegreen_list'),
    path('subscribegreen/<int:pk>/', SubscribeGreenDetail.as_view(), name='subscribegreen_detail'),
]