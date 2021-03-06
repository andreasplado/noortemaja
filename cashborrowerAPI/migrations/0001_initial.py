# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-04 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=255)),
                ('borrower', models.CharField(max_length=255)),
                ('amount', models.FloatField(default=0.0)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('loanAdded', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('isLoanPrivate', models.BooleanField(default=False)),
                ('interest', models.FloatField(default=0.0)),
                ('interestInterval', models.CharField(max_length=5)),
                ('imageProof', models.ImageField(default='Imageproof/None/No-img.jpg', max_length=254, upload_to='Imageproof')),
            ],
        ),
        migrations.CreateModel(
            name='LoanComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('commenter', models.CharField(max_length=100)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='LoanCommentDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliker', models.CharField(max_length=255)),
                ('loancomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.LoanComment')),
            ],
        ),
        migrations.CreateModel(
            name='LoanCommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.CharField(max_length=255)),
                ('loancomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.LoanComment')),
            ],
        ),
        migrations.CreateModel(
            name='LoanDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliker', models.CharField(max_length=255)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='LoanLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.CharField(max_length=255)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=255)),
                ('borrower', models.CharField(max_length=255)),
                ('isLoanReturned', models.BooleanField(default=False)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashborrowerAPI.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.CharField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('imagePath', models.CharField(max_length=300)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
