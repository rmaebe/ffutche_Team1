from rest_framework import serializers
from backend.models import User
from backend.models import School
from backend.models import Scholarship
from backend.models import Tuition_Fee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'firstname',
            'lastname',
            'type',
            'address1',
            'address2',
            'phone1',
            'dob_month',
            'dob_day',
            'dob_year',
            'phone2',
            'cityofbirth',
            'countryofbirth',
            'martial_status']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'schoolID',
            'name',
            'address1',
            'address2',
            'city',
            'country',
            'type',
            'contact_name',
            'contact_phone1',
            'contact_phone2',
        ]


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = [
            'scholarshipID',
            'denomination',
            'referred_studies'
            'minimum_amount',
            'description',
            'criteria'
        ]


class TuitionfeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition_Fee
        fields = [
            'schoolID'
            'academic_level',
            'academic_year',
            'tuition',
            'clothing',
            'furniture',
            'books',
            'misc',
        ]
