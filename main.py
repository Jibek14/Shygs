from Fruit import Fruit
import warnings
from Data import get_pages
import pandas as pd
from GeneralTable import create_general_df, general_df_to_excel

warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

general_df = pd.DataFrame()
i = 0
j = 0
stop_program = False

while not stop_program:
    title =input("Введите наименование товара\t")
    if title.lower() == 'стоп':
        break
    elif title.lower() == 'импорт':
        while True:
            imp_title = input("Введите наименование товара\t")
            if imp_title.lower()=='стоп':
                stop_program = True
                break
            else:
                imp_fruit = Fruit(j, is_import=1, title=imp_title)
                j += 1
                get_pages(imp_fruit)
                data_dict = imp_fruit.get_general_data()
                general_df = create_general_df(data_dict, general_df, 1)
                general_df_to_excel(general_df, 'общая.xlsx')
    else:
        loc_fruit = Fruit(i, is_import=0, title=title)
        i += 1
        get_pages(loc_fruit)
        data_dict = loc_fruit.get_general_data()
        general_df = create_general_df(data_dict, general_df, 0)
        general_df_to_excel(general_df, 'общая.xlsx')
    if stop_program:
        break
# а-40-284.3,аа-25-175.4,8-10-59.3,в-10-62,о-5-32
# а-40-271.1,аа-25-172.8,в-10-67.9,б-10-65.4,р-15-103.9,э-10-68.5,$-3-20.3,о-7-48,г-5-32.6