from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from apps.user.tokens import create_jwt_pair_for_user


def login_user(serializer):
    user = authenticate(
        email=serializer.validated_data['email'],
        password=serializer.validated_data['password']
    )

    if user is not None:
        token = create_jwt_pair_for_user(user)
        response = {'message': 'Login Successful', 'token': token}
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
