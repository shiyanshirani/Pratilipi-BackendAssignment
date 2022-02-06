# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.http import Http404
# from django.contrib.auth.hashers import check_password


# class CustomBackend(ModelBackend):
#     def authenticate(self, request, **kwargs):
#         User = get_user_model()
#         email = kwargs["email"]
#         password = kwargs["password"]
#         try:
#             user = User.objects.get(email=email)
#             if user.check_password(password) is True:
#                 return user
#         except User.DoesNotExist:
#             return Http404
