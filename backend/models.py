from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    address1 = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45)
    phone1 = models.CharField(max_length=45)
    dob_month = models.CharField(max_length=45)
    dob_day = models.CharField(max_length=45)
    dob_year = models.CharField(max_length=45)
    phone2 = models.CharField(max_length=45)
    cityofbirth = models.CharField(max_length=45)
    countryofbirth = models.CharField(max_length=45)
    martial_status = models.CharField(max_length=45)

    def __str__(self):
        return self.username


class Student_Hollow_Year(models.Model):
    username = models.ForeignKey(User)
    hollow_year = models.CharField(max_length=45, primary_key=True)
    activities = models.CharField(max_length=45)

    def __str__(self):
        return self.username


class School(models.Model):
    schoolID = models.CharField(max_length=45, primary_key=True)
    name = models.CharField(max_length=45)
    address1 = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    contact_name = models.CharField(max_length=45)
    contact_phone1 = models.CharField(max_length=45)
    contact_phone2 = models.CharField(max_length=45)

    def __str__(self):
        return self.schoolID


class Student_Education(models.Model):
    schoolID = models.ForeignKey(School)
    username = models.ForeignKey(User)
    years_attended = models.CharField(max_length=45, primary_key=True)
    SE_class = models.CharField(max_length=45)
    grade = models.CharField(max_length=45)
    degree = models.CharField(max_length=45)
    rank = models.CharField(max_length=45)
    dismissed = models.CharField(max_length=45)
    dismissal_reason = models.CharField(max_length=45)

    def __str__(self):
        return self.username


class Scholarship(models.Model):
    scholarshipID = models.CharField(max_length=45, primary_key=True)
    denomination = models.CharField(max_length=45)
    referred_studies = models.CharField(max_length=45)
    minimum_amount = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    criteria = models.CharField(max_length=45)

    def __str__(self):
        return self.scholarshipID


class Student_Scholarship(models.Model):
    scholarshipID = models.ForeignKey(Scholarship)
    username = models.ForeignKey(User)
    awarded_on = models.CharField(max_length=45)
    delivery_method = models.CharField(max_length=45)
    award_justification = models.CharField(max_length=45)
    awarded_amount = models.CharField(max_length=45)

    def __str__(self):
        return self.scholarshipID


class Scholarship_Donation(models.Model):
    scholarshipID = models.ForeignKey(Scholarship)
    donorID = models.ForeignKey(User)
    amount = models.CharField(max_length=45)
    academic_year = models.CharField(max_length=45)

    def __str__(self):
        return self.scholarshipID


class Tuition_Fee(models.Model):
    schoolID = models.ForeignKey(School)
    academic_level = models.CharField(max_length=45, primary_key=True)
    academic_year = models.CharField(max_length=45, primary_key=True)
    tuition = models.CharField(max_length=45)
    clothing = models.CharField(max_length=45)
    furniture = models.CharField(max_length=45)
    books = models.CharField(max_length=45)
    misc = models.CharField(max_length=45)

    def __str__(self):
        return self.schoolID
