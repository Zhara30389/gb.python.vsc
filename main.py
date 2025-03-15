from file_utils import get_directory_info, save_to_json, save_to_csv, save_to_pickle

directory = 'path/to/your/directory'
data = get_directory_info(directory)

save_to_json(data, 'output.json')
save_to_csv(data, 'output.csv')
save_to_pickle(data, 'output.pkl')