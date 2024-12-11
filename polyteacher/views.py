from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class AllTranslation(APIView):
    def get(self, request):

        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)

        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

class FrenchSpanishTranslationViewSet(APIView):


    def get(self, request):
        source_language = request.query_params.get('source_language', 'pas de language') 
        target_language = request.query_params.get('target_language', None)
        source_text = request.query_params.get('source_text', None)

        data = Translation.objects.filter(source_language=source_language, target_language=target_language, source_text=source_text)
        serialized_data = TranslationSerializer(data, many=True)

        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):

        source_language = 'FR'
        source_text = 'J\'ai un chat'
        target_language = 'ES'
        target_text = 'Tengo un gato'

        Translation.objects.create(source_language=source_language, source_text=source_text, target_language=target_language, target_text=target_text)

        return Response(data={
            "Result": "Translation added",
            "Translation": target_text
        },
          status=status.HTTP_201_CREATED
        )
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

def index(request):
    return render(request, 'index.html', context={})