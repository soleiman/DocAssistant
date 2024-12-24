# Generated by Django 4.2.7 on 2023-12-04 04:03

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1041_alter_consumptiontemplate_sources"),
    ]

    operations = [
        migrations.AddField(
            model_name="consumptiontemplate",
            name="assign_custom_fields",
            field=models.ManyToManyField(
                blank=True,
                related_name="+",
                to="documents.customfield",
                verbose_name="assign these custom fields",
            ),
        ),
        migrations.AddField(
            model_name="customfieldinstance",
            name="value_document_ids",
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name="customfield",
            name="data_type",
            field=models.CharField(
                choices=[
                    ("string", "String"),
                    ("url", "URL"),
                    ("date", "Date"),
                    ("boolean", "Boolean"),
                    ("integer", "Integer"),
                    ("float", "Float"),
                    ("monetary", "Monetary"),
                    ("documentlink", "Document Link"),
                ],
                editable=False,
                max_length=50,
                verbose_name="data type",
            ),
        ),
    ]
