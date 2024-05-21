from Fruit import Fruit
import warnings
from Data import get_pages
import pandas as pd
from GeneralTable import create_general_df, general_df_to_excel
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)


general_df = pd.DataFrame()
i = 0
j = 0
while True:
    loc_fruit = Fruit(i, is_import=0)
    i += 1
    if loc_fruit.title.lower() == 'импорт':
        while True:
            imp_fruit = Fruit(j, is_import=1)
            j += 1
            get_pages(imp_fruit)
            data_dict = imp_fruit.get_general_data()
            general_df = create_general_df(data_dict, general_df, 1)
            general_df_to_excel(general_df, 'общая.xlsx')
            if imp_fruit.title.lower() == 'стоп':
                break
    else:
        get_pages(loc_fruit)
        data_dict = loc_fruit.get_general_data()
        general_df = create_general_df(data_dict, general_df, 0)
        general_df_to_excel(general_df, 'общая.xlsx')

#а-15-65.8,аа-15-64.2,8-5-20.4,о-3-12.4,ж-10-43.4
#а-10-186,э-7-125.7
#аа-10,в-40,ж-20
