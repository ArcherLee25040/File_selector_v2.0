import tkinter as tk
from tkinter import filedialog
import os
import importlib.util

# 设置颜色和字体
bg_color = "#f0f0f0"
button_color = "#4CAF50"
text_color = "white"
font_size = 14
font_family = "Helvetica"

def merge_txt_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    spec = importlib.util.spec_from_file_location("merge_function", "merge_function.py")
    merge_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(merge_module)
    merge_module.perform_merge(folder_path)

root = tk.Tk()
root.title("Txt 文件合并工具")
root.geometry("500x300")  
root.configure(bg=bg_color)

button = tk.Button(root, text="选择文件夹并合并", command=merge_txt_files, bg=button_color, fg=text_color, font=(font_family, font_size))
button.pack(pady=30)

label_result = tk.Label(root, text="", bg=bg_color, fg=text_color, font=(font_family, font_size))
label_result.pack()

root.mainloop()