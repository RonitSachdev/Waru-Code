#!/usr/bin/env python3
"""
WaruCodeRoastの簡単なテストスクリプト
APIキーを必要とせずに基本的な機能をテストします
"""

import os
import sys
from pathlib import Path

def test_imports():
    """必要なモジュールがインポートできるかテスト"""
    try:
        import click
        import rich.console
        import rich.panel
        import rich.syntax
        import rich.text
        print("✅ すべてのインポートが成功しました")
        return True
    except ImportError as e:
        print(f"❌ インポートエラー: {e}")
        return False

def test_file_reading():
    """ツールがファイルを読み込めるかテスト"""
    try:
        from waru_roast import CodeRoaster
        roaster = CodeRoaster()
        content, ext = roaster.get_file_content("sample_code.py")
        if content and ext:
            print("✅ ファイル読み込みが動作します")
            return True
        else:
            print("❌ ファイル読み込みに失敗しました")
            return False
    except Exception as e:
        print(f"❌ ファイル読み込みエラー: {e}")
        return False

def test_cli_structure():
    """CLIコマンドが正しく構造化されているかテスト"""
    try:
        from waru_roast import cli
        commands = cli.commands
        expected_commands = ['roast', 'roast-dir', 'personas', 'setup']
        
        for cmd in expected_commands:
            if cmd in commands:
                print(f"✅ コマンド '{cmd}' が見つかりました")
            else:
                print(f"❌ コマンド '{cmd}' が見つかりません")
                return False
        return True
    except Exception as e:
        print(f"❌ CLI構造エラー: {e}")
        return False

def test_sample_file_exists():
    """サンプルファイルが存在するかテスト"""
    if Path("sample_code.py").exists():
        print("✅ サンプルファイルが存在します")
        return True
    else:
        print("❌ サンプルファイルが見つかりません")
        return False

def main():
    """すべてのテストを実行"""
    print("🧪 WaruCodeRoastをテスト中...\n")
    
    tests = [
        ("インポートテスト", test_imports),
        ("ファイル読み込みテスト", test_file_reading),
        ("CLI構造テスト", test_cli_structure),
        ("サンプルファイルテスト", test_sample_file_exists),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"{test_name}を実行中...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 テスト結果: {passed}/{total} テストが成功しました")
    
    if passed == total:
        print("🎉 すべてのテストが成功しました！WaruCodeRoastの使用準備ができました！")
        print("\n次のステップ:")
        print("1. https://platform.openai.com/ からOpenAI APIキーを取得")
        print("2. 設定: set OPENAI_API_KEY=your-key-here")
        print("3. 試してみる: python waru_roast.py roast sample_code.py")
    else:
        print("❌ 一部のテストが失敗しました。上記のエラーを確認してください。")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 