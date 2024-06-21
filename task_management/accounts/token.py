from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['user_id'] = str(user.id)
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email
        }

        return data


def get_user_token(user):
    serializer = CustomTokenObtainPairSerializer()
    refresh = serializer.get_token(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token
