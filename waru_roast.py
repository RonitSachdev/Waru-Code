#!/usr/bin/env python3
"""
WaruCodeRoast - GPTを使ったコードレビューを面白く批判するCLIツール
時には残酷に正直で面白いコードレビューが必要ですよね！
"""

import os
import sys
import click
import openai
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich.prompt import Prompt
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Initialize Rich console
console = Console()

# Configure OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CodeRoaster:
    """コードを批判する機能を扱うメインクラス"""
    
    def __init__(self):
        self.roast_personas = {
            "savage": "あなたは残酷に正直で、コードを容赦なく批判するコードレビュアーです。ユーモア、皮肉、機知を使いながらも、建設的なフィードバックを提供します。",
            "comedian": "あなたはコードをレビューするスタンドアップコメディアンです。ジョーク、ダジャレ、機知に富んだ観察をしながら、役立つ提案をします。",
            "professor": "あなたは何でも見てきた年配の教授です。皮肉で見下すような態度ですが、知識豊富なコードレビューをします。",
            "hacker": "あなたは謎めいたハッカーで、技術的専門知識とエッジの効いたユーモアを混ぜてコードをレビューします。"
        }
    
    def get_file_content(self, file_path):
        """ファイル内容を読み込んでシンタックスハイライト付きで返す"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content, Path(file_path).suffix
        except Exception as e:
            console.print(f"[red]ファイル読み込みエラー: {e}[/red]")
            return None, None
    
    def roast_code(self, code_content, file_extension, persona="savage", context=""):
        """コードをGPTに送って批判してもらう"""
        if not os.getenv("OPENAI_API_KEY"):
            console.print("[red]エラー: 環境変数にOPENAI_API_KEYが見つかりません！[/red]")
            console.print("OpenAI APIキーを設定してください:")
            console.print("Windows: set OPENAI_API_KEY=your-key-here")
            console.print("Linux/Mac: export OPENAI_API_KEY='your-key-here'")
            return None
        
        persona_prompt = self.roast_personas.get(persona, self.roast_personas["savage"])
        
        system_prompt = f"""
{persona_prompt}

あなたはコードをレビューして、批判的なコードレビューを提供します。あなたの回答は以下のようであるべきです：
1. 面白くて魅力的
2. 建設的（役立つフィードバックを提供）
3. 批判のスタイル（皮肉的、機知に富んでいるが、意地悪ではない）
4. 具体的なコード例と提案を含む
5. 絵文字とフォーマットを使って魅力的にする

以下のような批判のセクションで回答をフォーマットしてください：
- 🔥 第一印象
- 😂 笑ったところ
- 🤔 実際に良いところ
- 💡 改善提案
- 🎯 最終判定

面白くて役立つようにしてください！
"""

        user_prompt = f"""
このコードを批判してください：

ファイルタイプ: {file_extension}
コンテキスト: {context if context else '追加コンテキストなし'}

コード:
```
{code_content}
```

最高の批判的なコードレビューをお願いします！
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=1500,
                temperature=0.8
            )
            return response.choices[0].message.content
        except Exception as e:
            console.print(f"[red]OpenAI API呼び出しエラー: {e}[/red]")
            return None

def display_roast(code_content, file_extension, roast_result):
    """コードと批判結果を美しいフォーマットで表示"""
    console.print("\n")
    
    # コードを表示
    if file_extension:
        syntax = Syntax(code_content, file_extension[1:], theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="[bold blue]批判されるコード[/bold blue]", border_style="blue"))
    
    console.print("\n")
    
    # 批判を表示
    console.print(Panel(roast_result, title="[bold red]🔥 批判結果 🔥[/bold red]", border_style="red"))
    console.print("\n")

@click.group()
@click.version_option(version="1.0.0", prog_name="WaruCodeRoast")
def cli():
    """🔥 WaruCodeRoast - 残酷に正直で面白いコードレビュー！ 🔥"""
    pass

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--persona', '-p', 
              type=click.Choice(['savage', 'comedian', 'professor', 'hacker']),
              default='savage',
              help='批判するペルソナを選択')
@click.option('--context', '-c', 
              help='コードに関する追加コンテキスト')
def roast(file_path, persona, context):
    """特定のファイルを批判"""
    console.print(Panel.fit(
        "[bold red]🔥 WaruCodeRoastへようこそ 🔥[/bold red]\n"
        "[yellow]コードが建設的に破壊される準備をしてください...！[/yellow]",
        border_style="red"
    ))
    
    roaster = CodeRoaster()
    code_content, file_extension = roaster.get_file_content(file_path)
    
    if not code_content:
        return
    
    with console.status("[bold green]コードを批判中...[/bold green]", spinner="dots"):
        roast_result = roaster.roast_code(code_content, file_extension, persona, context)
    
    if roast_result:
        display_roast(code_content, file_extension, roast_result)
    else:
        console.print("[red]コードの批判に失敗しました。APIキーを確認して再試行してください。[/red]")

@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--persona', '-p', 
              type=click.Choice(['savage', 'comedian', 'professor', 'hacker']),
              default='savage',
              help='批判するペルソナを選択')
@click.option('--extensions', '-e', 
              default='py,js,ts,jsx,tsx,java,cpp,c,cs,php,rb,go,rs,swift,kt',
              help='批判するファイル拡張子（カンマ区切り）')
def roast_dir(directory, persona, extensions):
    """ディレクトリ内のすべてのコードファイルを批判"""
    console.print(Panel.fit(
        "[bold red]🔥 大量批判セッション 🔥[/bold red]\n"
        "[yellow]ディレクトリ全体を批判する時間です！[/yellow]",
        border_style="red"
    ))
    
    roaster = CodeRoaster()
    extensions_list = [ext.strip() for ext in extensions.split(',')]
    
    # すべてのコードファイルを見つける
    code_files = []
    for ext in extensions_list:
        code_files.extend(Path(directory).rglob(f"*.{ext}"))
    
    if not code_files:
        console.print("[yellow]批判するコードファイルが見つかりません！[/yellow]")
        return
    
    console.print(f"[green]{len(code_files)}個のファイルを批判します！[/green]\n")
    
    for i, file_path in enumerate(code_files, 1):
        console.print(f"[bold blue]ファイル {i}/{len(code_files)}を批判中: {file_path.name}[/bold blue]")
        
        code_content, file_extension = roaster.get_file_content(file_path)
        if not code_content:
            continue
        
        with console.status(f"[bold green]{file_path.name}を批判中...[/bold green]", spinner="dots"):
            roast_result = roaster.roast_code(code_content, file_extension, persona)
        
        if roast_result:
            display_roast(code_content, file_extension, roast_result)
        
        if i < len(code_files):
            console.print("[yellow]次のファイルに進むにはEnterを押してください...[/yellow]")
            input()

@cli.command()
def personas():
    """利用可能な批判ペルソナを表示"""
    console.print(Panel.fit(
        "[bold red]🎭 利用可能な批判ペルソナ 🎭[/bold red]\n\n"
        "[bold green]savage[/bold green] - 残酷に正直な批判者\n"
        "[bold blue]comedian[/bold blue] - スタンドアップコメディアンスタイル\n"
        "[bold yellow]professor[/bold yellow] - 不機嫌な年配教授\n"
        "[bold magenta]hacker[/bold magenta] - 謎めいたハッカーの雰囲気",
        border_style="red"
    ))

@cli.command()
def setup():
    """ツールのセットアップ手順"""
    console.print(Panel.fit(
        "[bold red]🔧 セットアップ手順 🔧[/bold red]\n\n"
        "1. 依存関係をインストール: [green]pip install -r requirements.txt[/green]\n"
        "2. OpenAI APIキーを取得: [blue]https://platform.openai.com/[/blue]\n"
        "3. APIキーを設定:\n"
        "   [green]Windows: set OPENAI_API_KEY=your-key-here[/green]\n"
        "   [green]Linux/Mac: export OPENAI_API_KEY='your-key-here'[/green]\n"
        "4. 批判開始: [green]python waru_roast.py roast your_file.py[/green]\n\n"
        "[yellow]注意: APIを使用するにはOpenAIアカウントに課金を追加する必要があります[/yellow]",
        border_style="red"
    ))

if __name__ == '__main__':
    cli() 