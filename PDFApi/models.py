from django.db import models



class PFDInvoice(models.Model):
    """Model that represent the invoice data"""
    invoice_number = models.CharField(max_length=225)
    Account = models.CharField(max_length=225)
    descripition = models.CharField(max_length=500)
    date = models.DateField()
    phone_no = models.IntegerField()
    address = models.TextField()
    subtoatal = models.IntegerField()
    shipping = models.IntegerField()
    total    = models.IntegerField()
