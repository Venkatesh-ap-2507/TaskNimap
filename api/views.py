from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client,Project,User
from .serializers import ClientSerializer,ProjectSerializer,UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ClientDetail(APIView):
    def get(self,request,pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        client = Client.objects.get(pk=pk)
        client.delete()
        return Response(status=204)


class ProjectList(APIView):
    def get(self, request, client_id=None, *args, **kwargs):
        if client_id:
            projects = Project.objects.filter(client__id=client_id)
        else:
            projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, client_id, *args, **kwargs):
        client = Client.objects.get(pk=client_id)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(client=client, created_by=request.user)
            project.users.set(request.data.get('users'))
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class UserProjectListView(APIView):
    def get(self, request):
        user = request.user
        # Access the projects using the related name defined in the ManyToManyField
        projects = user.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
