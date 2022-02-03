# # Project imports
# from api.models import User

# # DRF imports
# from rest_framework.response import Response

# # Django imports
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend


# # class MyAuthBackend(object):
# #     def authenticate(self, email, password, **kwargs):
# #         try:
# #             user = User.objects.get(email=email)
# #             if user.check_password(password):
# #                 return user
# #             else:
# #                 return Response({"Error": "Invalid credentials"})

# #         except User.DoesNotExist:
# #             # logging.getLogger("error_logger").error(
# #             #     "user with login %s does not exists " % login
# #             # )
# #             # return None
# #             return Response({"Error": "User does not exists"})

# #         except Exception as e:
# #             # logging.getLogger("error_logger").error(repr(e))
# #             # return None
# #             return Response({"Error": str(e)})

# #     def get_user(self, user_id):
# #         try:
# #             user = User.objects.get(sys_id=user_id)
# #             if user.is_active:
# #                 return user
# #             return None
# #         except User.DoesNotExist:
# #             # logging.getLogger("error_logger").error("user with %(user_id)d not found")
# #             # return None

# #             return Response({"Error": "User does not exists"})


# class MyAuthBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)

#         try:
#             case_insensitive_username_field = "{}__iexact".format(
#                 UserModel.USERNAME_FIELD
#             )
#             user = UserModel._default_manager.get(
#                 **{case_insensitive_username_field: username}
#             )
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
