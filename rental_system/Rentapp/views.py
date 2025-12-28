from django.shortcuts import render
from rest_framework import viewsets
from .models import House, Tenant, Room, TenantDocument, RentLedger, Payment, SMSLog, Expense, ReportExport
from .serializers import HouseSerializer,TenantSerializer,RoomSerializer,TenantDocumentSerializer,RentLedgerSerializer,PaymentSerializer,SMSLogSerializer,ExpenseSerializer,ReportExportSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.



class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    
    @action(detail=False,methods=['get'])
    def list_available_house(self,request):
        queryset = House.objects.filter(is_available=True)
        serializer = HouseSerializer(queryset,many=True)
        
        return Response(serializer.data)
    
    
    @action(detail=False,methods=['get'])
    
    def list_total_rooms(self,request):
        total_room_dict ={}
        houses = House.objects.all()
        for house in houses:
            total_room_dict[house.name] = house.total_rooms
        # houses = House.objects.values('name','total_rooms')
        # for house in houses:
        #      total_room_dict = {house['name']:house['total_rooms']}
            
        return Response(total_room_dict)
    
    @action(detail=False,methods=['get'])
    def house_available(self,request):
        q1 = House.objects.filter(is_available=True).count()
        q2 = House.objects.filter(is_available=False).count()
        
        return Response({
            "available_count":q1,
            "unavailable_count":q2
        })
        
    @action(detail=True,methods=['post'])
    def add_house(self,request,pk=None):
        house_data = request.data
        serializer = HouseSerializer(data=house_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':"New house Successfully added."
            })
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True,methods=['get'])
    def total_rent(self,request,pk=None):
        house = self.get_object()
        total_rooms = house.rooms.all()
        total_rent = 0
        for room in total_rooms:
            total_rent += room.monthly_rent
           
        return Response({
            "house_name": house.name,
            "total_rent":total_rent
        })    
        
                 
                
        
        
            
            
        
        
        
        
    
    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class TenantDocumentViewSet(viewsets.ModelViewSet):
    queryset = TenantDocument.objects.all()
    serializer_class = TenantDocumentSerializer
    
class RentLedgerViewset(viewsets.ModelViewSet):
    queryset = RentLedger.objects.all()
    serializer_class = RentLedgerSerializer
    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class SMSLogViewSet(viewsets.ModelViewSet):
    queryset = SMSLog.objects.all()
    serializer_class = SMSLogSerializer
    
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
class ReportExportViewset(viewsets.ModelViewSet):
    queryset = ReportExport.objects.all()
    serializer_class = ReportExportSerializer
    
                            
            