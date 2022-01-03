import os
import numpy
import pandas as pd
from pathlib import Path


class RenameFile:
    def __init__(self):
        pass

    def give_file_rename(self, past_name, new_name, past_fold_path, new_fold_path):
        """
        给文件重命名
        :param past_name:
        :param new_name:
        :param past_fold_path:
        :param new_fold_path:
        :return:
        """
        past_file_path = Path(past_fold_path).joinpath(past_name)
        if not past_file_path.exists():
            raise Exception(f"{past_file_path}路径不存在")
        if not past_file_path.is_file():
            raise Exception(f"{past_file_path}不是文件")
        self.create_fold(new_fold_path)
        new_file_path = Path(new_fold_path).joinpath(new_name)
        if new_file_path.exists():
            raise Exception(f"{new_file_path}新路径已存在")
        os.rename(past_file_path, new_file_path)

    def create_fold(self, fold_path):
        """
        创建文件夹
        :return:
        """
        fold_path = Path(fold_path)
        fold_path.mkdir(parents=True, exist_ok=True)

    def goback_template_df(self, file_path):
        """
        返回模板的值
        :param file_path:
        :return:
        """
        pd_kwargs = {
            "names": ["原名", "新名"],
            "engine": "openpyxl"
        }
        file_path = Path(file_path)
        df = self.read_file_by_pd(file_path, pd_kwargs)
        with open("a.txt", "w") as f:
            f.write(str(11))
        if df['原名'].isnull().any():
            raise Exception("原名列存在空值")
        if df['新名'].isnull().any():
            raise Exception("新名列存在空值")
        past_name_list = df["原名"].values.tolist()
        new_name_list = df["新名"].values.tolist()
        return past_name_list, new_name_list

    def read_file_by_pd(self, file_path, kwargs):
        """
        通过pandas读取文件
        :param file_path:
        :param kwargs:
        :return:
        """
        file_path = Path(file_path)
        file_suffix = file_path.suffix
        if not (file_suffix == ".xls" or file_suffix == '.xlsx'):
            raise Exception("文件类型不是xls或者xlsx")
        df = pd.read_excel(file_path, **kwargs)
        return df

def start_exec(file_path, past_fold_path, new_fold_path):

    rename_file = RenameFile()
    past_name_list, new_name_list = rename_file.goback_template_df(file_path)

    for past_name in past_name_list:
        new_name = new_name_list[past_name_list.index(past_name)]
        rename_file.give_file_rename(past_name, new_name, past_fold_path, new_fold_path)


# if __name__ == "__main__":
#     file_path = r"C:\Users\Administrator\Desktop\a.xlsx"
#     past_fold_path = r"C:\Users\Administrator\Desktop"
#     new_fold_path = r"C:\Users\Administrator\Desktop"
#     rename_file = RenameFile()
#     past_name_list, new_name_list = rename_file.goback_template_df(file_path)
#     for past_name in past_name_list:
#         new_name = new_name_list[past_name_list.index(past_name)]
#         rename_file.give_file_rename(past_name, new_name, past_fold_path, new_fold_path)
