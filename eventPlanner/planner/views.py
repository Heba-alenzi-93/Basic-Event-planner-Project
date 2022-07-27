from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import EvenPlanner
from .serializer import EvenPlannerListSerializer,DetailSerializer,UpdateSerializer,CreateSerializer

# Create your views here.


class EvenPlannerListView(ListAPIView):
    queryset = EvenPlanner.objects.all()
    serializer_class = EvenPlannerListSerializer


class EventPlannerObjAPIView(RetrieveAPIView):
    queryset = EvenPlanner.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "event_id"
    serializer_class = DetailSerializer



class EventPlannerObjUpdateView(UpdateAPIView):
    queryset = EvenPlanner.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "event_id"
    serializer_class = UpdateSerializer

class EventPlannerDeleteApiView(DestroyAPIView):
    queryset = EvenPlanner.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "event_id"



class EventPlannerObjAddView(CreateAPIView):
    serializer_class = CreateSerializer
    def perform_create(self,obj):
        return None

