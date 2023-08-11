from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from stc.models import depot, document, master_data, movement, region, region_auth, user_details, user_level, users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

class userSuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('__all__')
        
class user_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_level
        fields = ('__all__')
        
class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = ('__all__')
        
class depotSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = depot
        fields = ('__all__')
        expandable_fields = {'reg': (regionSerializer, {'source': 'region_id', 'fields': ['region_id', 'region_txt','region_code','priority']})}

class region_authSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = region_auth
        fields = ('__all__')
        expandable_fields = {'users': (usersSerializer, {'source': 'user_id', 'fields': ['user_id', 'username','status','password']})}

class user_detailsSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = user_details
        fields = ('__all__')
        expandable_fields = {'users': (usersSerializer, {'source': 'user_id', 'fields': ['user_id', 'username','status','password']})}

class master_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = master_data
        fields = ('__all__')  

class documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = document
        fields = ('__all__')  

class movementSerializer(serializers.ModelSerializer):
    class Meta:
        model = movement
        fields = ('__all__')  

class qrSerializer(serializers.ModelSerializer):
    class Meta:
        model = master_data
# this will show only below mentioned fields
        fields = ("material_no", "visible_material_no", "qr_id")  

""" 
Extend user and autohnticatons

"""        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token