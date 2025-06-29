@echo off
echo 🔥 WaruCodeRoast - コード批判CLI 🔥
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Pythonがインストールされていないか、PATHにありません
    echo https://python.org からPythonをインストールしてください
    pause
    exit /b 1
)

REM Check if requirements are installed
echo 依存関係をチェック中...
python -c "import click, rich, openai" >nul 2>&1
if errorlevel 1 (
    echo 📦 依存関係をインストール中...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 依存関係のインストールに失敗しました
        pause
        exit /b 1
    )
)

REM Check if API key is set
if "%OPENAI_API_KEY%"=="" (
    echo ⚠️  OPENAI_API_KEYが設定されていません
    echo OpenAI APIキーを設定してください:
    echo set OPENAI_API_KEY=your-api-key-here
    echo.
    echo または実行: python waru_roast.py setup
    echo.
)

REM Run the CLI tool
python waru_roast.py %*

pause 