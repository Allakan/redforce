from django.urls import path
from .views import AdvantagesList, AdvantagesDetail
from .views import AdvantagesImageList, AdvantagesImageDetail
from .views import FeedbackList, FeedbackDetail
from .views import FaqList, FaqDetail
from .views import ContactsList, ContactsDetail
from .views import RatingList, RatingDetail
from .views import SubscribptionList, SubscribptionDetail

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
]