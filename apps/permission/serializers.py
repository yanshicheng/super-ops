from rest_framework import serializers
from .models import Role, Rule, Menu


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'





class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(MenuSerializer, self).to_representation(instance)
        role_list = instance.role.all()
        representation['roles'] = [] if not role_list else [role.name for role in
                                                            role_list]
        return representation
