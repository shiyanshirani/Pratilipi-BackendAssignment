# Django imports
from django.contrib.auth.models import User

# Project imports
from api.models import Profile
from api.serializers import ProfileSerializer

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
class UserAPI(APIView):
    def post(self, request):
        try:
            """
            Username mandatory in this case because
            I am not configuring AbstractUser class
            which will make the code even complex.
            """

            user = User(
                username=request.data["username"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                email=request.data["email_id"],
                password=request.data["password"],
            )
            user.save()

            profile = Profile(
                user=user,
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                email_id=request.data["email_id"],
                phone_number=request.data["phone_number"],
            )
            profile.save()

            return Response({"Success": "Profile saved."})

        except Exception as e:
            return Response(str(e))

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
