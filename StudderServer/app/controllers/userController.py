from rest_framework import serializers;

from rest_framework.decorators import api_view;
from rest_framework.response import Response;

from django.http import HttpResponse

from rest_framework.parsers import JSONParser;
from django.utils.six import BytesIO;


from app.models.user import User;

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = ('id', 'name', 'surname', 
                  'description', 'birthday', 'onlineStatus', 
                  'lastOnline', 'radius', 'latitude',
                  'longtitude', 'profileCreated', 
                  'shareLocation', 'sex', 'interestedIn');
    
    def create(validated_data):
        user = User(**validated_data);
        user.save();


@api_view(['GET'])
def userOne(request, pk):
    try:
        user = User.objects.get(pk=pk);
    except:
        return HttpResponse(status = 404);

    if(request.method == 'GET'):    
        serializer = UserSerializer(user);
        return Response(serializer.data); 
      
@api_view(['GET'])    
def userAll(request): 
    try:
        users = User.objects.all();
    except:
        return HttpResponse(status = 404);

    if(request.method == 'GET'):
        serializer = UserSerializer(users, many = True);
        return Response(serializer.data);


@api_view(['POST'])
def userAdd(request):
    try:
        data = JSONParser.parse(request.body);
        serializer = UserSerializer(data = data);
        serializer.validated_data;

        if(request.method == "POST"):
            serializer.save();
    except:
        return HttpResponse(status = 404);

    

    
    