#!/usr/bin/env python3
# coding=utf-8

import os


def find_files_with_string(directory, target_string):
    for root, _, files in os.walk(directory):
        for file in files:
            if target_string in file:
                relative_path = os.path.relpath(
                    os.path.join(root, file), directory)
                print(f"Found: {relative_path}")


if __name__ == "__main__":
    # 指定要查找的目录和目标字符串
    search_directory = '.'  # 当前目录
    target_string = 'o'  # 替换为你要查找的字符串

    find_files_with_string(search_directory, target_string)
