from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from fc_user.models import FilingCabinetUser


class FilingCabinet(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_by = models.ForeignKey(FilingCabinetUser, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name



