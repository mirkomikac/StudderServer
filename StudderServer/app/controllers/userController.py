from rest_framework import serializers;

from rest_framework.decorators import api_view;
from rest_framework.response import Response;

from django.http import HttpResponse

from app.models.user import User;



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = ('id', 'name', 'surname');


@api_view(['GET'])
def getUser(request, pk):
    try:
        user = User.objects.get(pk=pk);
    except:
        return HttpResponse(status = 404);

    if(request.method == "GET"):
        serializer = UserSerializer(user);
        return Response(serializer.data)   


