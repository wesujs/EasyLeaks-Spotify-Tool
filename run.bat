@echo off

REM check if Python is installed

python --version >nul 2>&1
if %errorlevel% neq = 0 (
    echo Python is not installed or not in PATH. Pleas install Python 3.12 or greater and try again.
    pause
    exit /b 1
)

REM check if pip is installed

pip --version && (
    echo installing requirements...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install requirements.
        exit /b 1
    )
    echo Requirements installed successfully.
) || (
    echo pip is not installed or not in PATH. Please install pip and try again.
)