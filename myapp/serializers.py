from rest_framework import serializers
from .models import Advantages, AdvantagesImage, Feedback, Faq, Contacts, Rating, Subscription

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'

class AdvantagesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesImage
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class SubscribptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
