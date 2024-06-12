
# Parquet2Analysis

This repository contains scripts to analyze Parquet files using Python. The tools include functionality for data description, value analysis, and linear regression analysis with p-values.

## Files

- **create_sample_parquet.py**: A script to generate a sample Parquet file for testing.
- **analyze_parquet.py**: The main Python script to read, parse, and analyze Parquet files.
- **run_analysis.bat**: A Windows batch file to run the Python script with user inputs.

## How to Use

### Setting Up Your Environment

1. **Set Python as an Environment Variable**

   - Open Command Prompt.
   - Type `where python` to find the path to your Python executable.
   - Note the path (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\`).

   - Right-click on "This PC" or "My Computer" on your desktop or in File Explorer, and select "Properties."
   - Click on "Advanced system settings."
   - Click on the "Environment Variables" button.
   - In the "System variables" section, find the `Path` variable, select it, and click "Edit."
   - Click "New" and add the path to the Python executable.
   - Click "OK" to close all windows.

2. **Install Required Packages**

   Open Command Prompt and run the following commands to install the necessary packages:

   ```sh
   python -m pip install pandas pyarrow statsmodels
   ```

### Running the Scripts

1. **Generate a Sample Parquet File**

   - Run `create_sample_parquet.py` to generate a sample Parquet file named `sample_data.parquet`.

   ```sh
   python create_sample_parquet.py
   ```

2. **Run the Analysis**

   - Place `sample_data.parquet`, `analyze_parquet.py`, and `run_analysis.bat` in the same directory.
   - Double-click `run_analysis.bat` to open the terminal with a menu.
   - Follow the prompts to input the necessary information for the analysis.

### Example Inputs

1. **Menu Selection**: Enter `1` to run the analysis.

2. **Prompted Inputs**:

   ```text
   Enter the path to the Parquet file: sample_data.parquet
   Enter the names of the values we are interested in (space-separated): value_1 value_2
   Enter the dependent variable for regression analysis: dependent_var
   Enter the independent variables for regression analysis (space-separated): independent_var_1 independent_var_2
   Enter the functions to perform (description, analyze, regression) (space-separated): description analyze regression
   ```

<details>
  <summary>baby only</summary>
  
  ## For My Beloved Baby

  I created this tool just for you, my love. I hope it makes your work a little bit easier and reminds you of how much I care about you. You are always on my mind, and I love you more than words can say.
  
  ## 亲爱的宝宝
  
  我为你制作了这个工具，希望它能让你的工作变得轻松一些，也让你想起我有多么关心你。你一直在我心中，我爱你胜过千言万语。
  
</details>

## 中文说明

这个仓库包含使用 Python 分析 Parquet 文件的脚本。工具包括数据描述、值分析和带有 p 值的线性回归分析功能。

## 文件介绍

- **create_sample_parquet.py**：生成用于测试的示例 Parquet 文件的脚本。
- **analyze_parquet.py**：主要的 Python 脚本，用于读取、解析和分析 Parquet 文件。
- **run_analysis.bat**：用于运行 Python 脚本并接受用户输入的 Windows 批处理文件。

## 使用说明

### 设置您的环境

1. **将 Python 设置为环境变量**

   - 打开命令提示符。
   - 输入 `where python` 找到 Python 可执行文件的路径。
   - 记下路径（例如，`C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\`）。

   - 在桌面或文件资源管理器中右键点击“这台电脑”或“我的电脑”，选择“属性”。
   - 点击“高级系统设置”。
   - 点击“环境变量”按钮。
   - 在“系统变量”部分，找到 `Path` 变量，选择它并点击“编辑”。
   - 点击“新建”并添加 Python 可执行文件的路径。
   - 点击“确定”关闭所有窗口。

2. **安装所需的包**

   打开命令提示符并运行以下命令以安装必要的包：

   ```sh
   python -m pip install pandas pyarrow statsmodels
   ```

### 运行脚本

1. **生成示例 Parquet 文件**

   - 运行 `create_sample_parquet.py` 以生成名为 `sample_data.parquet` 的示例 Parquet 文件。

   ```sh
   python create_sample_parquet.py
   ```

2. **运行分析**

   - 将 `sample_data.parquet`、`analyze_parquet.py` 和 `run_analysis.bat` 放在同一目录中。
   - 双击 `run_analysis.bat` 以打开带有菜单的终端。
   - 按提示输入分析所需的信息。

### 示例输入

1. **菜单选择**：输入 `1` 运行分析。

2. **提示输入**：

   ```text
   Enter the path to the Parquet file: sample_data.parquet
   Enter the names of the values we are interested in (space-separated): value_1 value_2
   Enter the dependent variable for regression analysis: dependent_var
   Enter the independent variables for regression analysis (space-separated): independent_var_1 independent_var_2
   Enter the functions to perform (description, analyze, regression) (space-separated): description analyze regression
   ```
