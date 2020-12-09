from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        """Returnes a list of API view features"""
        an_apiView = [
            'User HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to Django Traditional View',
            'Gives you more control over app logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!', 'an_apiView':an_apiView})