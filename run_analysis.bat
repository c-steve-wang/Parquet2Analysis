@echo off
setlocal

:menu
cls
echo Select an option:
echo 1. Run analysis
echo 2. Exit
set /p choice=Enter your choice (1 or 2): 

if "%choice%"=="1" goto run_analysis
if "%choice%"=="2" goto exit

:run_analysis
cls

:: Prompt user for inputs
set /p PARQUET_FILE=Enter the path to the Parquet file: 
set /p VALUE_NAMES=Enter the names of the values we are interested in (space-separated): 
set /p DEPENDENT_VAR=Enter the dependent variable for regression analysis: 
set /p INDEPENDENT_VARS=Enter the independent variables for regression analysis (space-separated): 
set /p FUNCTIONS=Enter the functions to perform (description, analyze, regression) (space-separated): 

:: Define the Python script
set PYTHON_SCRIPT=analyze_parquet.py

:: Run the Python script with user inputs
python %PYTHON_SCRIPT% %PARQUET_FILE% --value_names %VALUE_NAMES% --dependent_var %DEPENDENT_VAR% --independent_vars %INDEPENDENT_VARS% --functions %FUNCTIONS%

pause
goto menu

:exit
exit
