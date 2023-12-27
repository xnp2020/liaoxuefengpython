#!/usr/bin/env python3
# coding = utf-8

import os


def merge_files(input_files, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            for input_file in input_files:
                with open(input_file, 'r', encoding='utf-8') as input:
                    output.write(input.read())
                    output.write('\n')  # 可以根据需要插入换行符
        print(
            f'Merged content from {len(input_files)} files into {output_file} successfully.')
    except Exception as e:
        print(f'Error: {e}')


# 示例用法

os.chdir('C:\\Users\\xnp2010\\Desktop\\xwsz\\printhub\\安装包\\printhub\\V5.2023.0209增量补丁\\updatetools\\SQL更新脚本')
input_files = sorted(os.listdir())
print(input_files)

output_file = r'C:\Users\xnp2010\Desktop\xwsz\printhub\安装包\printhub\V5.2023.0209增量补丁\updatetools\20220321-20230209.sql'
merge_files(input_files, output_file)
