from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local models
from contact.models import Contact
from followers.models import Follower
from orders.models import Orders
from projects.models import Project
from team.models import Team
from services.models import Service

# Serializers
from .serializers import (
    ProjectSerializer, TeamSerializer, ServiceSerializer,
    OrdersSerializer, FollowerSerializer, ContactSerializer
)

# GET API Views
class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        data = serializer.data
        for project in data:
            if project.get('image'):
                project['image'] = request.build_absolute_uri(project['image'])
        return Response(data)

class TeamListView(APIView):
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        data = serializer.data
        for member in data:
            if member.get('image'):
                member['image'] = request.build_absolute_uri(member['image'])
        return Response(data)

class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

# POST API Views
class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowerCreateView(APIView):
    def post(self, request):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse("{Response: 200 OK}")