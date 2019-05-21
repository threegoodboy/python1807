from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=''
        fields="__all__"
