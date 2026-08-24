from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("consent", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="consentrecord",
            name="expires_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="consentrecord",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="consentrecord",
            constraint=models.UniqueConstraint(fields=("user", "consent_type"), name="unique_user_consent_type"),
        ),
    ]
