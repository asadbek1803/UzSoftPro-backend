### Local models
from contact.models import Contact
from followers.models import Follower
from orders.models import Orders
from projects.models import Project, Category
from team.models import Team
from services.models import Service

# Global library
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Project
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = fields

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = fields

# POST Serializers
class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class FollowerSerializer(ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'