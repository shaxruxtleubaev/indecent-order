from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from apps.about_us.models import (
    Advantages,
    About_us
)
from apps.client_requests.models import ClientRequest
from apps.models.models import (
    Languages,
    Visa,
    OtherImages,
    Models
)
from apps.models_requests.models import Model_request

from .serializers import (
    AdvantagesSerializer,
    About_usSerializer,
    ClientRequestSerializer,
    LanguagesSerializer,
    VisaSerializer,
    OtherImagesSerializer,
    ModelsSerializer,
    Model_requestSerializer
)

class About_usAPIView(APIView):

    def get(self, request):
        queryset = About_us.objects.all()
        serializer = About_usSerializer(queryset, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

class ModelsAPIView(APIView):

    def get(self, request):
        queryset = Models.objects.all()
        serializer = ModelsSerializer(
            queryset, 
            many=True,
            context={'request': request}
        )
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )

class ClientRequestAPIView(APIView):

    def post(self, request):
        serializer = ClientRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class Model_requestAPIView(APIView):
    
    def post(self, request):
        serializer = Model_requestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )