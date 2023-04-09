from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NewUser(AbstractUser):

    ADMIN = 'Admin'
    STUDENT = 'Student'
    TEACHER = 'Teacher'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default=ADMIN)
    user_id = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self) -> str:
        return self.role  

    # sorting users by role
    class Meta:
        ordering = ['role']

class Computer(models.Model):
    OS_MAC = 'MacOS'
    OS_WINDOWS = 'Windows'
    OS_CHOICES = [
        (OS_MAC, 'MacOS'),
        (OS_WINDOWS, 'Windows'),
    ]

    RAM_STANDARD = '16GB'
    RAM_HIGH_PERFORMANCE = '64GB'
    RAM_CHOICES = [
        (RAM_STANDARD, '16GB'),
        (RAM_HIGH_PERFORMANCE, '64GB'),
    ]

    SSD_STANDARD = '512GB'
    SSD_HIGH_PERFORMANCE = '4TB'
    SSD_CHOICES = [
        (SSD_STANDARD, '512GB'),
        (SSD_HIGH_PERFORMANCE, '4TB'),
    ]

    GRAPHIC_CARD_STANDARD = '4GB'
    GRAPHIC_CARD_HIGH_PERFORMANCE = '12GB'
    GRAPHIC_CARD_CHOICES = [
        (GRAPHIC_CARD_STANDARD, '4GB'),
        (GRAPHIC_CARD_HIGH_PERFORMANCE, '12GB'),
    ]

    STATUS_AVAILABLE = 'Available'
    STATUS_UNAVAILABLE = 'Unavailable'
    STATUS_NON_OPERATIONAL = 'Non Operational'
    STATUS_RETIRED = 'Retired'

    STATUS_CHOICES = [
       (STATUS_AVAILABLE,'Available'),
        (STATUS_UNAVAILABLE,'Unavailable'),
        (STATUS_NON_OPERATIONAL,'Non Operational'),
        (STATUS_RETIRED, 'Retired'),
    ]

    COMPUTER_STANDARD = 'Standard'
    COMPUTER_HIGH_PERFORMANCE = 'Performance'

    COMPUTER_CLASSSIFICATION = [
        (COMPUTER_STANDARD, 'Standard'),
        (COMPUTER_HIGH_PERFORMANCE, 'Performance'),
    ]

    serial_number = models.CharField(max_length=7)
    os = models.CharField(max_length=17, choices=OS_CHOICES, default=OS_WINDOWS)
    ram = models.CharField(max_length=17, choices=RAM_CHOICES, default=RAM_STANDARD)
    ssd = models.CharField(max_length=17, choices=SSD_CHOICES, default=SSD_STANDARD)
    graphic_card = models.CharField(max_length=17, choices=GRAPHIC_CARD_CHOICES, default=GRAPHIC_CARD_STANDARD)
    status = models.CharField(max_length=17, choices=STATUS_CHOICES, default=STATUS_AVAILABLE)
    computer_classification = models.CharField(max_length=17, choices=COMPUTER_CLASSSIFICATION, default=COMPUTER_STANDARD)
    last_update = models.DateTimeField(auto_now=True)
    # overriding the method (converting to string)
    def __str__(self) -> str:
        return self.serial_number 

    # sorting computers by serial number
    class Meta:
        ordering = ['serial_number']

class Request (models.Model):
    REQUEST_CREATED = 'Created'
    REQUEST_PENDING = 'Pending'
    REQUEST_PROCESSING = 'Processing'
    REQUEST_DENIED = 'Denied'
    REQUEST_READY = 'Ready'
    REQUEST_CHECKOUT = 'Checked Out'
    REQUEST_CHECKIN = 'Returned'

    REQUEST_CHOICES = [
        (REQUEST_CREATED, 'Created'),
        (REQUEST_PENDING, 'Pending'),
        (REQUEST_PROCESSING, 'Processing'),
        (REQUEST_DENIED, 'Denied'),
        (REQUEST_READY, 'Ready'),
        (REQUEST_CHECKOUT, 'Checked Out'),
        (REQUEST_CHECKIN, 'Returned'),
    ]
    OS_MAC = 'MacOS'
    OS_WINDOWS = 'Windows'
    OS_CHOICES = [
        (OS_MAC, 'MacOS'),
        (OS_WINDOWS, 'Windows'),
    ]
    COMPUTER_STANDARD = 'Standard'
    COMPUTER_HIGH_PERFORMANCE = 'Performance'

    COMPUTER_CLASSSIFICATION = [
        (COMPUTER_STANDARD, 'Standard'),
        (COMPUTER_HIGH_PERFORMANCE, 'Performance'),
    ]
    order_date = models.DateTimeField(auto_now_add=True)
    # check_out_date = models.DateTimeField(auto_now=True)
    # check_in_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=15, choices=REQUEST_CHOICES, default=REQUEST_CREATED)
    student_first_name = models.CharField(max_length=50, null=True, blank=True)
    student_last_name = models.CharField(max_length=50, null=True, blank=True)
    student_email = models.EmailField()
    teacher_first_name = models.CharField(max_length=50, null=True, blank=True)
    teacher_last_name = models.CharField(max_length=50, null=True, blank=True)
    teacher_email = models.EmailField()
    computer_sn = models.ForeignKey(Computer, on_delete=models.PROTECT)
    os = models.CharField(max_length=17, choices=OS_CHOICES, default=OS_WINDOWS)
    computer_classification = models.CharField(max_length=17, choices=COMPUTER_CLASSSIFICATION, default=COMPUTER_STANDARD)
    approved = models.BooleanField('Approved', default=False)
    approved_date = models.DateTimeField(auto_now=True, null=True)
    returned = models.BooleanField('Returned', default=False)
    returned_date = models.DateTimeField(auto_now=True, null=True)
    comment = models.TextField(null=True, blank=True)
        
    