from django.test import TestCase

# Create your tests here.
from .utils import *
from .models import *
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile

expected_diff = 'DataFrame.iloc[:, 1] are different\n\nDataFrame.iloc[:, 1] values are different (33.33333 %)\n[left]:  [5, 6, 7]\n[right]: [5, 666, 7]'

class UtilsTests(TestCase):
  files = [
    BASE_DIR+'/example_file_1.csv',
    BASE_DIR+'/example_file_2.csv',
  ]

  def test_pd_read(self):
    fm = []
    fn = self.files[0]
    with open(fn,'rb') as fh:
      fu = UploadedFile(fh)
      fm = FileModel(imported_file=fu)
      df = pd_read(fm.imported_file)

  def test_pd_compare(self):
    df = []
    for fn in self.files:
      with open(fn,'rb') as fh:
        fu = UploadedFile(fh)
        fm = FileModel(imported_file=fu)
        df.append(pd_read(fm.imported_file))

    res_a = pd_compare(df[0], df[0])
    self.assertEquals(res_a, 'ok')

    res_b = pd_compare(df[0], df[1])
    self.assertEquals(res_b, expected_diff)


class ReconciliationModelTests(TestCase):
  files = [
    BASE_DIR+'/example_file_1.csv',
    BASE_DIR+'/example_file_2.csv',
  ]

  def test_pd_compare(self):
    fa = []
    for fn in self.files:
      with open(fn,'rb') as fh:
        fu = UploadedFile(fh)
        fm = FileModel(imported_file=fu)
        fm.full_clean()
        fm.save()
        fa.append(fm)

    rm_00 = ReconciliationModel(file_1=fa[0], file_2=fa[0])
    rm_00.save()
    self.assertEquals(rm_00.recon_msg, 'ok')

    rm_01 = ReconciliationModel(file_1=fa[0], file_2=fa[1])
    rm_01.save()
    self.assertEquals(rm_01.recon_msg, expected_diff)
