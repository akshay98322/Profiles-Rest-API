from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from profile_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):
        """Returnes a list of API view features"""
        an_apiView = [
            'User HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to Django Traditional View',
            'Gives you more control over app logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!', 'an_apiView':an_apiView})
    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request,pk=None):
        """ Handles updateing an object"""
        return Response({'method': 'PUT'})

    def patch(self,request, pk=None):
        """ Handles partical update an object"""
        return Response({'method': 'PATCH'})
    def delete(self,request, pk=None):
        """ Delete an object"""
        return Response({'method': 'DELETE'})


