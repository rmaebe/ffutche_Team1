from rest_framework import generic
from backend.models import School
from backend.models import Scholarship
from backend.models import Tuition_Fee
from .serializers import ScholarshipSerializer
from .serializers import TuitionfeeSerializer
from .serializers import SchoolSerializer


class SchoolListView(generic.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetailView(generic.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDestroyView(generic.DestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolUpdateView(generic.UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ScholarshipListView(generic.ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class ScholarshipDetailView(generic.RetrieveAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class ScholarshipDestroyView(generic.DestroyAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class ScholarshipUpdateView(generic.UpdateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class TuitionFeeListView(generic.ListAPIView):
    queryset = Tuition_Fee.objects.all()
    serializer_class = TuitionfeeSerializer


class TuitionFeeDetailView(generic.RetrieveAPIView):
    queryset = Tuition_Fee.objects.all()
    serializer_class = TuitionfeeSerializer


class TuitionFeeDestroyView(generic.DestroyAPIView):
    queryset = Tuition_Fee.objects.all()
    serializer_class = TuitionfeeSerializer


class TuitionFeeUpdateView(generic.UpdateAPIView):
    queryset = Tuition_Fee.objects.all()
    serializer_class = TuitionfeeSerializer

