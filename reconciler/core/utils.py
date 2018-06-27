import pandas as pd
def pd_read(file_field):
  """
  file_field - FileField entry
  """
  extension = file_field.name.split('.')[-1]
  file_field.seek(0)
  if extension=='csv':
    df = pd.read_csv(file_field)
    return df
  if extension=='xlsx':
    df = pd.read_excel(file_field)
    return df
  raise ValueError("File extension '%s' not supported yet. Only done for csv, xlsx."%extension)


from pandas.util.testing import assert_frame_equal
def pd_compare(df_1, df_2):
    try:
      assert_frame_equal(df_1, df_2)
    except Exception as error:
      return str(error)
    return 'ok'



