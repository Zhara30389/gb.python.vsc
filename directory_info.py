import os

def get_directory_info(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        dir_size = 0
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            result.append({
                'name': name,
                'type': 'file',
                'size': file_size,
                'parent': root
            })
        
        for name in dirs:
            dir_path = os.path.join(root, name)
            dir_info = {
                'name': name,
                'type': 'directory',
                'size': 0,  # Размер будет обновлен после обхода всех файлов
                'parent': root
            }
            result.append(dir_info)
        
        # Обновляем размер директории
        for item in result:
            if item['type'] == 'directory' and item['parent'] == root:
                item['size'] = dir_size
    return result