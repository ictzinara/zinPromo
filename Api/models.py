import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Province(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class PromotionApplicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='')
    reg_number = models.CharField(max_length=100)
    nat_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    application_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class PromotionWeeklyDraw(models.Model):
    weekly_winner = models.ForeignKey(PromotionApplicant, on_delete=models.CASCADE)
    draw_number = models.IntegerField(default=0, null=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)
    notified_on = models.DateField()
    price_claimed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.weekly_winner.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class GrandPriceDraw(models.Model):
    weekly_winner = models.ForeignKey(PromotionApplicant, on_delete=models.CASCADE)
    draw_number = models.IntegerField(default=0, null=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    notified = models.BooleanField(default=False)
    notified_on = models.DateField()
    price_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.weekly_winner.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class vlicDb(models.Model):
    Regno = models.CharField(max_length=100, null=False)
    Status = models.CharField(max_length=100,null=False)
    Penalties = models.IntegerField(default=0)
    Arrears = models.IntegerField(default=0)
    DateLicensed = models.DateField(null=False)
    ExpiryDate = models.DateField(null=False)
    dateCaptured = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Regno

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class LicenseDb(models.Model):
    EXPIRED = models.CharField(max_length=100, null=True)
    REGISTRATION_NO = models.CharField(max_length=100, null=False)
    LICENSE_STATUS = models.CharField(max_length=100,null=False)
    PENALTY_AMOUNT = models.IntegerField(default=0)
    ARREAR_AMOUNT = models.IntegerField(default=0)
    LAST_LICENSING_TRANSACTION = models.DateTimeField(null=False)
    BLACKLISTED = models.CharField(max_length=100)
    LICENCE_EXPIRY_DATE = models.DateTimeField(null=False)
    Date_Captured = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.REGISTRATION_NO

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

# Define the Vehicle class model with the fields class and mass
class VehicleClass(models.Model):
    CLASS_CHOICES = (
        ('0', 'Motorcyles'),
        ('1', 'Light vehicles'),
        ('2', 'Buses'),
        ('3', 'Heavy vehicles'),
        ('4', 'Haulage trucks'),
    )
    vehicle_class = models.CharField(max_length=1, choices=CLASS_CHOICES)
    vehicle_mass = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle_class} - {self.vehicle_mass} kg"

# Define the Tariff class model with the fields fee_type, amount and vehicle (foreign key)
class Tariff(models.Model):
    FEE_CHOICES = (
        ('Toll', 'Tolling fee'),
        ('Liv', 'Vehicle licensing fee'),
        ('Bridge', 'Bridge fee'),
        ('Transit', 'Transit fee'),
    )
    fee_type = models.CharField(max_length=10, choices=FEE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ForeignKey(VehicleClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fee_type} - {self.amount} USD"

# Vehicle model
class Vehicle(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    status = models.BooleanField(default=1)
    license_plate = models.CharField(max_length=10, unique=True)
    owner = models.ForeignKey('VehicleOwner', on_delete=models.CASCADE, related_name='vehicles')
    current_user = models.ForeignKey('VehicleCurrentUser', on_delete=models.SET_NULL, related_name='vehicles', null=True)

    # Meta
    def __str__(self):
        return self.name

# KYC model
class KYC(models.Model):
    # Fields
    code =models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='')
    document_type = models.CharField(max_length=20)
    document_number = models.CharField(max_length=20, unique=True)
    reg_book_document = models.ImageField(upload_to='kyc/',null=True)

    # Meta
    def __str__(self):
        return self.name

# Vehicle owner model
class VehicleOwner(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    national_identity = models.EmailField(max_length=100, unique=True)
    national_identity_document_image = models.ImageField(upload_to='kyc/{1}/identity/')
    kyc = models.OneToOneField('KYC', on_delete=models.CASCADE, related_name='vehicle_owner')

    # Meta
    def __str__(self):
        return self.name

# Vehicle current user model
class VehicleCurrentUser(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    kyc = models.OneToOneField('KYC', on_delete=models.CASCADE, related_name='vehicle_current_user')
    national_identity = models.EmailField(max_length=100, unique=True)
    national_identity_document_image = models.ImageField(upload_to='kyc/{1}/identity/',null=True)

    # Meta
    def __str__(self):
        return self.name

# Data collection model
class DataCollection(models.Model):
     # Fields 
     vehicle_id = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='data_collection')
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return f'{self.vehicle_id}'

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return f'{self.name}'
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    firstName = models.CharField(max_length=100, null=False)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100,null=False)
    emailId  = models.CharField(max_length=100,null=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return f'{self.firstName}'


# A model for a workplace entity, such as a department, team, site or project
class Workplace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='workplaces_manager')
    address = models.TextField()
    employees = models.ManyToManyField('Employee',related_name='workplaces_employees')

    def __str__(self):
        return self.name

# A model for a safety, health, environment and quality (SHEQ) standard, such as ISO 9001, ISO 14001 or OHSAS 18001
class Standard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# A model for a SHEQ requirement, such as a policy, procedure, guideline or regulation
class Requirement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='requirements')

    def __str__(self):
        return self.name

# A model for a SHEQ indicator, such as a metric, target, score or rating
class Indicator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='indicators')
    unit = models.CharField(max_length=20) # e.g. percentage, number, rating
    formula = models.TextField(blank=True) # e.g. (a + b) / c * 100

    def __str__(self):
        return self.name

# A model for a SHEQ record, such as an audit, inspection, assessment or survey
class Record(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name='records_workplace')
    date = models.DateField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='records_employee')
    indicators = models.ManyToManyField(Indicator, through='RecordIndicator')

    def __str__(self):
        return self.name

# A model for a record-indicator relationship, which stores the value of an indicator for a record
class RecordIndicator(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f'{self.record} - {self.indicator}'

class Risk(models.Model):
    RISK_LEVELS = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('E', 'Extreme'),
    )
    workplace = models.ForeignKey('Workplace', on_delete=models.CASCADE, related_name='workplace_risks')
    description = models.TextField()
    level = models.CharField(max_length=1, choices=RISK_LEVELS)
    mitigation = models.TextField()
    responsible = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='responsible_risks')

    def __str__(self):
        return f'{self.workplace} - {self.description}'

class Incident(models.Model):
    INCIDENT_TYPES = (
        ('A', 'Accident'),
        ('I', 'Injury'),
        ('D', 'Damage'),
        ('N', 'Near miss'),
    )
    SEVERITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    )
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )
    workplace = models.ForeignKey('Workplace', on_delete=models.CASCADE, related_name='workplace_incidents')
    date = models.DateField()
    type = models.CharField(max_length=1, choices=INCIDENT_TYPES)
    action_taken = models.TextField()
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='employee_incidents')
    reported_by = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='incidents_reporter')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    corrective_action = models.TextField(blank=True)

    def __str__(self):
        return f'{self.workplace} - {self.date} - {self.type} - {self.date} - {self.employee} - {self.severity}'
    


class Compliance(models.Model):
    COMPLIANCE_TYPES = (
        ('L', 'Legal'),
        ('R', 'Regulatory'),
        ('S', 'Standard'),
        ('C', 'Contractual'),
    )
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name='compliances')
    type = models.CharField(max_length=1, choices=COMPLIANCE_TYPES)
    requirement = models.TextField()
    evidence = models.FileField(upload_to='compliance/')
    status = models.BooleanField(default=False)
    verified_by = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='compliances')

    def __str__(self):
        return f'{self.workplace} - {self.type} - {self.requirement}'

class ChecklistItem(models.Model):
    question = models.CharField(max_length=200)
    answer = models.BooleanField()

    def __str__(self):
        return self.question
class Audit(models.Model):
    AUDIT_TYPES = (
        ('I', 'Internal'),
        ('E', 'External'),
    )
    workplace = models.ForeignKey('Workplace', on_delete=models.CASCADE, related_name='audits')
    date = models.DateField()
    type = models.CharField(max_length=1, choices=AUDIT_TYPES)
    findings = models.TextField()
    recommendations = models.TextField()
    auditor = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='auditor_employee')
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL,null=True,related_name='audited_employee')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    checklist = models.ManyToManyField(ChecklistItem)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    feedback = models.TextField(blank=True)
    def __str__(self):
        return f'{self.workplace} - {self.date} - {self.type}-{self.date} - {self.employee} - {self.score}%'


