def read_hex_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def get_matrix_data(hex_data, unicode_code):
    for line in hex_data:
        if line.startswith(unicode_code):
            return line.split(':')[1].strip()
    return None

def replace_matrix(hex_data, unicode_codes, new_unicode_code):
    new_matrix = get_matrix_data(hex_data, new_unicode_code)
    if new_matrix is not None:
        for unicode_code in unicode_codes:
            for i, line in enumerate(hex_data):
                if line.startswith(unicode_code):
                    hex_data[i] = unicode_code + ':' + new_matrix + '\n'
                    break
    else:
        print(f"未找到Unicode码 {new_unicode_code}")

def write_hex_file(file_path, hex_data):
    with open(file_path, 'w') as file:
        file.writelines(hex_data)

def main():
    file_path = 'unifont.hex'  # 请替换为你的文件路径
    hex_data = read_hex_file(file_path)

    to_replace_list = []
    while True:
        unicode_code = input("请输入要替换的Unicode码（输入exit结束输入）：")
        if unicode_code.lower() == 'exit':
            break
        to_replace_list.append(unicode_code)

    new_unicode_codes = []
    print("请输入新的Unicode码（输入exit开始替换）：")
    while True:
        new_unicode_code = input("输入新的Unicode码（输入exit结束输入）：")
        if new_unicode_code.lower() == 'exit':
            break
        new_unicode_codes.append(new_unicode_code)

    if new_unicode_codes:
        for new_unicode_code in new_unicode_codes:
            replace_matrix(hex_data, to_replace_list, new_unicode_code)

        write_hex_file(file_path, hex_data)
        print("替换完成！")
    else:
        print("未输入新的Unicode码，无法开始替换。")

if __name__ == "__main__":
    main()
