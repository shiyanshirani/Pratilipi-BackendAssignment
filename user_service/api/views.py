# Project imports
from api.models import Profile
from api.serializers import ProfileSerializer

# DRF imports
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

# Create your views here.
class UserAPI(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Detail": "Profile saved."})

        return Response({"Error": "Profile not saved."})

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
