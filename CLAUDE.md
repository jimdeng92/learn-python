# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

这是一个 **Python 个人学习仓库**，非应用/库项目。内容是按课时组织的独立练习脚本，学习资料来源为 https://github.com/jackfrued/Python-100-Days。

没有构建、测试、lint 流程，也没有 `requirements.txt`。每个 `.py` 文件都是可独立运行的示例脚本。

## 环境与运行

- Python 版本：**3.14**（`.venv` 虚拟环境，仅装了 pip）
- 运行单个脚本（Git Bash）：
  ```bash
  .venv/Scripts/python.exe "shang_gui_gu/day07/03 多态.py"
  ```
- 部分脚本依赖第三方库但**当前未安装**，运行前需先装：
  - `python-100-days/21 python 读写 Excel 文件/` → `openpyxl`（xlsx）、`xlrd`/`xlwt`（xls）
  - `python-100-days/22 python 处理图像/` → `pillow`
  - 安装示例：`.venv/Scripts/python.exe -m pip install openpyxl pillow xlrd xlwt`

## 代码组织

两条平行的学习路线，内容主题重叠（都覆盖数据类型、函数、面向对象等），互不引用：

- `shang_gui_gu/`（尚硅谷）：按 `dayNN/` 分目录，文件名形如 `NN 主题.py`（含中文和空格）。进度到 day07（面向对象三大特性：封装/继承/多态）。
- `python-100-days/`：扁平结构，文件名形如 `NN 主题.py`，进度到第 22 课（正则、Excel、图像处理）。

## 约定

- 文件名、注释、字符串大量使用**中文**，且文件名包含空格——命令行引用路径时务必加引号。
- `.editorconfig` 强制 `end_of_line = lf` 和文件末尾空行。
- 脚本以“可运行的教学示例”为目标，逻辑直白、无异常处理与工程化封装属正常现象，**不要按生产标准重构**这些练习代码。
