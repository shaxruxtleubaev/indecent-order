from rest_framework.serializers import ModelSerializer

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

class AdvantagesSerializer(ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'

class About_usSerializer(ModelSerializer):
    class Meta:
        model = About_us
        fields = '__all__'

class ClientRequestSerializer(ModelSerializer):
    class Meta:
        model = ClientRequest
        fields = '__all__'

class LanguagesSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'

class VisaSerializer(ModelSerializer):
    class Meta:
        model = Visa
        fields = '__all__'

class OtherImagesSerializer(ModelSerializer):
    class Meta:
        model = OtherImages
        fields = '__all__'

class ModelsSerializer(ModelSerializer):
    class Meta:
        model = Models
        fields = '__all__'

class Model_requestSerializer(ModelSerializer):
    class Meta:
        model = Model_request
        fields = '__all__'