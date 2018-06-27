from django.db import models
from django.utils import timezone

class FileModel(models.Model):
  imported_file = models.FileField(unique=True)
  as_of = models.DateField(default=timezone.now)
  description = models.CharField(max_length=100, default="n/a")

  def __str__(self, *args, **kwargs):
    prefix = self.description if self.description!='n/a' else self.imported_file.name
    return "%s (%s)"%(prefix, self.as_of)


from .utils import pd_read, pd_compare
class ReconciliationModel(models.Model):
  file_1 = models.ForeignKey('FileModel', related_name='recon_file_1', on_delete=models.DO_NOTHING)
  file_2 = models.ForeignKey('FileModel', related_name='recon_file_2', on_delete=models.DO_NOTHING)
  #percent_ok = models.PositiveIntegerField(default=0)
  recon_msg = models.CharField(max_length=100, default='n/a')

  def save(self, *args, **kwargs):
    df_1 = pd_read(self.file_1.imported_file)
    df_2 = pd_read(self.file_2.imported_file)
    self.recon_msg = pd_compare(df_1, df_2)
    return super().save(*args, **kwargs)

  def __str__(self, *args, **kwargs):
    return "%s vs %s: %s"%(self.file_1, self.file_2, self.recon_msg)
