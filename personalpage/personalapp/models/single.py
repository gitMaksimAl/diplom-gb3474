from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.__class__.objects.exclude(pk=self.pk).delete()
        super(SingletonModel, self).save(
            force_insert, force_update, using, update_fields
        )

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
