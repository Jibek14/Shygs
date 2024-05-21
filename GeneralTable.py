import warnings
import pandas as pd
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)


def create_general_df(data, df,is_import):
    rows = []
    for fruit_name, fruit_data in data.items():
        rows.append(list(fruit_data.keys()))
        main_values = [value[0] if isinstance(value, list) else value for value in fruit_data.values()]
        rows.append(main_values)
        for i in range(len(fruit_data['наименование'][1])):
            if is_import==0:
                rows.append([fruit_data['наименование'][1][i], fruit_data['кол-во'][1][i], fruit_data['ВЕС'][1][i]])
            else:
                rows.append([fruit_data['наименование'][1][i], fruit_data['кол-во'][1][i]])
    new_df = pd.DataFrame(rows)
    df = pd.concat([df, new_df], ignore_index=True)
    return df


def general_df_to_excel(df, output_file):
    try:
        df.to_excel(output_file, index=False)
        print(f"DataFrame successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
