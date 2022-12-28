from rest_framework import serializers
from .models import Employees

class EmployeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employees
        # fields = {'firstName','lastName'}
        fields = '__all__'
