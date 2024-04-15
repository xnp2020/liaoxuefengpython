#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :test9100.py
@说明        :
@时间        :2024/03/15 10:54:20
@作者        :xnp2010
@版本        :1.0
'''


import socket
import tkinter as tk
from tkinter import filedialog


def send_to_printer(file_path, printer_ip, printer_port=9100):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((printer_ip, printer_port))
            s.sendall(file_content)

        print(f"文件 '{file_path}' 已成功发送到打印机 {printer_ip}:{printer_port}")
    except Exception as e:
        print(f"发送文件时发生错误：{e}")


def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def send_file():
    file_path = file_entry.get()
    printer_ip = ip_entry.get()
    send_to_printer(file_path, printer_ip)


# 创建主窗口
root = tk.Tk()
root.title("打印机文件发送工具")

# 文件选择部分
file_label = tk.Label(root, text="选择文件:")
file_label.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)

file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

browse_button = tk.Button(root, text="浏览", command=browse_file)
browse_button.grid(row=0, column=2, pady=5, padx=5, sticky=tk.W)

# 打印机IP部分
ip_label = tk.Label(root, text="打印机IP地址:")
ip_label.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

ip_entry = tk.Entry(root, width=20)
ip_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

# 发送按钮
send_button = tk.Button(root, text="发送文件", command=send_file)
send_button.grid(row=2, column=0, columnspan=3, pady=10)

# 启动主循环
root.mainloop()
