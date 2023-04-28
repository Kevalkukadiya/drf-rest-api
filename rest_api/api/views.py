from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Function Based CRUD
@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer =StudentSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complte Data Updated'})
        return Response(serializer.errors)
    

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Data Deleted'})



# CLass based CRUD
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer =StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, pk=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    def put(self,request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complte Data Updated'})
        return Response(serializer.errors)


    def patch(self,request, pk ,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    def delete(self,request, pk ,format=None):
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Data Deleted'})


#GenericAPIView and  Model Mixin CRUD

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwarges):
        return self.create(request, *args, **kwarges)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwarges):
        return self.retrieve(request, *args, **kwarges)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwarges):
        return self.update(request, *args, **kwarges)

class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwarges):
        return self.destroy (request, *args, **kwarges)


# Generic View and Model in One

# List and Create Model
class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwarges):
        return self.create(request, *args, **kwarges)


# Update , Retrive , Destroy Mixin 
class RUDStudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwarges):
        return self.retrieve(request, *args, **kwarges)

    def put(self, request, *args, **kwarges):
        return self.update(request, *args, **kwarges)

    def delete(self, request, *args, **kwarges):
        return self.destroy (request, *args, **kwarges)


# List API View

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# List API View in One

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# ViewSet - 12

from rest_framework import viewsets
from rest_framework import status
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    def retrieve (self,request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)


    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self,request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updatec'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'PArtial Data Updatec'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(Self,request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


# Model Viewset

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny , IsAdminUser, IsAuthenticatedOrReadOnly,DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from api.permission import MyPermission
from api.auth import CustomAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [MyPermission]

    

# Read only Model Viewset

class StudentReadonlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

