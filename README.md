## 这个脚本的功能主要是：

1. 提供一个图形用户界面（GUI），用户可以通过点击按钮选择一个包含多个文本文件的文件夹。
2. 遍历用户选择的文件夹及其子文件夹，将其中的文本文件每两个分为一组进行处理。
3. 对于每组中的文本文件，读取文件内容，提取特定格式的数据（以“mm\tkN\tsec”开头的行之后，每行数据的前两列），并将提取的数据整理成数据列表，再转换为包含两列数据的`DataFrame`，为每对文件的`DataFrame`赋予特定的列名。
4. 将所有组处理得到的`DataFrame`进行合并，合并后的结果保存在一个新生成的 Excel 文件中，该文件存储在以当前时间命名的文件夹内，这个文件夹与执行脚本的`main.py`文件位于同一目录下。