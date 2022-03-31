from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [

        {'GET' : 'api/Users'},# available only for admin
        {'GET': 'api/Users/userId'},

        #for supplier
        {'GET' : 'api/Users/Suppliers'},
        {'GET' : 'api/Users/Suppliers/supplierId'},
        {'GET' : 'api/Users/Suppliers/supplierId/Tasks'},
        {'GET' : 'api/Users/Suppliers/supplierId/Tasks/taskId'},
        {'GET' : 'api/Users/Suppliers/supplierId/Bills'},
        {'GET' : 'api/Users/Suppliers/supplierId/Bills/billId'},

        #for agency
        {'GET' : 'api/Users/Agencies'},
        {'GET' : 'api/Users/Agencies/agencyId'},
        {'GET' : 'api/Users/Agencies/agencyId/Tasks'},
        {'GET' : 'api/Users/Agencies/agencyId/Tasks/taskId'},
        {'GET' : 'api/Users/Agencies/agencyId/Bills'},
        {'GET' : 'api/Users/Agencies/agencyId/Bills/billId'},

        #for customers
        {'GET' : 'api/Users/Customers'},
        {'GET' : 'api/Users/Customers/cutomerId'},
        {'GET' : 'api/Users/Customers/cutomerId/Tasks'},
        {'GET' : 'api/Users/Customers/cutomerId/Tasks/taskId'},
        {'GET' : 'api/Users/Customers/cutomerId/Bills'},
        {'GET' : 'api/Users/Customers/cutomerId/Bills/billId'},

        #for workers
        {'GET' : 'api/Users/Workers'},
        {'GET' : 'api/Users/Workers/workerId'},
        {'GET' : 'api/Users/Workers/workerId/Tasks'},
        {'GET' : 'api/Users/Workers/workerId/Tasks/taskId'},
        {'GET' : 'api/Users/Workers/workerId/Bills'},
        {'GET' : 'api/Users/Workers/workerId/Bills/billId'},
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getUser(request, pk):
    user = User.objects.all(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSuppliers(request):
    user = request.user
    if user.roll != 'Supplier':
        suppliers = Supplier.objects.all()
        serializer = SupplierProfileSerializer(suppliers, many=True)
        return Response(serializer.data)
    else:
        return Response({'message' : 'Sorry, You can\'t view Suppliers List because you are not owner nor permitted user'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAgencies(request):
    user = request.user
    if user.roll != 'Agency':
        suppliers = Agency.objects.all()
        serializer = AgencyProfileSerializer(suppliers, many=True)
        return Response(serializer.data)
    else:
        return Response({'message' : 'Sorry, You can\'t view Agencies List because you are not owner nor permitted user'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCustomers(request):
    user = request.user
    if user.roll != 'Customer':
        suppliers = Customer.objects.all()
        serializer = CustomerProfileSerializer(suppliers, many=True)
        return Response(serializer.data)
    else:
        return Response({'message' : 'Sorry, You can\'t view Customers List because you are not owner nor permitted user'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWorkers(request):
    user = request.user
    if user.roll != 'Worker':
        suppliers = Worker.objects.all()
        serializer = WorkerProfileSerializer(suppliers, many=True)
        return Response(serializer.data)
    else:
        return Response({'message' : 'Sorry, You can\'t view Workers List because you are not owner nor permitted user'})



@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getTasks(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getBills(request):
    user = request.user
    bills = Billing.objects.all()
    serializer = BillingSerializer(bills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getSupplier(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getAgency(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getCustomer(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getWorker(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getTask(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getBill(request):
    user = request.user
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def getTasks(request):
#     user = request.user
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def getTasks(request):
#     user = request.user
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
   