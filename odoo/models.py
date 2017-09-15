# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class ResUsers(models.Model):
    active = models.NullBooleanField()
    login = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64, blank=True, null=True)
    company_id = models.IntegerField()
    partner_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField()
    share = models.NullBooleanField()
    write_uid = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    password_crypt = models.CharField(max_length=200, blank=True, null=True)
    alias_id = models.IntegerField()
    chatter_needaction_auto = models.NullBooleanField()
    sale_team_id = models.IntegerField(blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_invoiced = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    role_in_org = models.CharField(max_length=64, blank=True, null=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    is_deleted = models.NullBooleanField()
    is_prime = models.NullBooleanField()
    user_name = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'

    def __str__(self):
        return self.first_name