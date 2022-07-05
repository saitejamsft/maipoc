import pandas as pd


cache_files = {}
removable_files = ["Feature_Contribution", "model_features", "Oppty_Amendment", "Resource_Resource_Tier_Mapping", "soft_exception"]

def get_data(file_name, file_type, file_encoding=None):
    if file_name in cache_files:
        return cache_files[file_name]
    else:
        # print(f"read again {file_name}")
        if len(cache_files) > 15:
            for name in removable_files:
                cache_files.pop(f"local_files/opty/{name}.csv", None)
        file_path = (file_name)
        if file_type == 'csv':
            if file_encoding:
                data = pd.read_csv(file_path, encoding=file_encoding)
            else:
                data = pd.read_csv(file_path)
        elif file_type == 'json':
            data = pd.read_json(file_path)
        elif file_type == 'pkl':
            return file_path
        cache_files[file_name] = data
        return data


def update_data(key, value):
    cache_files[key] = value
