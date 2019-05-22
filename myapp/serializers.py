from rest_framework import serializers

from myapp.models import Users, Investment, Relation, Pledge


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Investment
        fields="__all__"

class  RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Relation
        fields="__all__"

class  PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pledge
        fields='__all__'