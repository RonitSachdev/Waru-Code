# �� WaruCodeRoast

GPTを使ったコードレビューを面白く批判するCLIツール！時には残酷に正直で面白いコードレビューが必要ですよね。

## 機能

- **複数の批判ペルソナ**: 残酷、コメディアン、教授、ハッカーのスタイルから選択
- **美しいCLIインターフェース**: シンタックスハイライト付きのリッチなターミナル出力
- **単一ファイル＆ディレクトリ批判**: 個別ファイルやディレクトリ全体を批判
- **建設的批判**: 面白いが実際に役立つフィードバック
- **多言語対応**: Python、JavaScript、TypeScript、Java、C++などに対応！

## 🚀 クイックスタート

### 1. 依存関係をインストール

```bash
pip install -r requirements.txt
```

### 2. OpenAI APIキーを取得

1. [OpenAI Platform](https://platform.openai.com/) にアクセス
2. アカウントを作成してAPIキーを取得
3. APIキーを設定:

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Windows:**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

### 3. 批判開始！

```bash
# 単一ファイルを批判
python waru_roast.py roast your_file.py

# 特定のペルソナで批判
python waru_roast.py roast your_file.py --persona comedian

# ディレクトリ全体を批判
python waru_roast.py roast-dir ./src/

# 利用可能なペルソナを表示
python waru_roast.py personas

# セットアップヘルプを表示
python waru_roast.py setup
```

## 批判ペルソナ

### 🔥 残酷 (Savage)
残酷に正直で、コードを容赦なく批判するが建設的なレビュアー。

### 🎤 コメディアン (Comedian)
スタンドアップコメディアンスタイルでジョーク、ダジャレ、機知に富んだ観察。

### 👨‍🏫 教授 (Professor)
何でも見てきた年配の教授 - 皮肉で見下すような態度だが知識豊富。

### 🖤 ハッカー (Hacker)
謎めいたハッカーで、技術的専門知識とエッジの効いたユーモアを混ぜてコードをレビュー。

## 使用例

### Pythonファイルを批判
```bash
python waru_roast.py roast my_script.py --persona savage
```

### コンテキスト付きで批判
```bash
python waru_roast.py roast my_script.py --context "これは猫の行動を予測する機械学習モデルです"
```

### 大量批判セッション
```bash
# ディレクトリ内のすべてのPythonとJavaScriptファイルを批判
python waru_roast.py roast-dir ./project/ --extensions py,js,ts

# ディレクトリ全体をコメディアンペルソナで批判
python waru_roast.py roast-dir ./project/ --persona comedian
```

## 得られるもの

各批判には以下が含まれます：
- 🔥 **第一印象** - コードへの最初の感想
- 😂 **笑ったところ** - 面白い部分（意図的かどうかは別として）
- 🤔 **実際に良いところ** - 正しくできている部分
- 💡 **改善提案** - 建設的フィードバック
- 🎯 **最終判定** - 全体的な評価

## 🛠️ 対応ファイルタイプ

このツールは以下のコードを批判できます：
- Python (`.py`)
- JavaScript (`.js`, `.jsx`)
- TypeScript (`.ts`, `.tsx`)
- Java (`.java`)
- C/C++ (`.c`, `.cpp`)
- C# (`.cs`)
- PHP (`.php`)
- Ruby (`.rb`)
- Go (`.go`)
- Rust (`.rs`)
- Swift (`.swift`)
- Kotlin (`.kt`)

そして他にも多数！`--extensions`フラグでカスタム拡張子を指定できます。

## 🔧 設定

### 環境変数
- `OPENAI_API_KEY`: あなたのOpenAI APIキー（必須）

### カスタム拡張子
```bash
# PythonとGoファイルのみを批判
python waru_roast.py roast-dir ./src/ --extensions py,go
```

## 🎨 出力例

```
🔥 WaruCodeRoastへようこそ 🔥
コードが建設的に破壊される準備をしてください...！

┌─ 批判されるコード ──────────────────────────────────────────────┐
│ 1  def calculate_sum(a, b):                                       │
│ 2      return a + b                                               │
│ 3                                                                  │
│ 4  # これは非常に複雑な関数です                                  │
│ 5  def complex_calculation(x):                                    │
│ 6      return x * 2                                               │
└───────────────────────────────────────────────────────────────────┘

┌─ 🔥 批判結果 🔥 ─────────────────────────────────────────────────┐
│                                                                     │
│ 🔥 第一印象                                                          │
│ まあ、どこから始めればいいのかな？このコードは2010年のチュートリアル│
│ を見ているような感じだね。                                          │
│                                                                     │
│ 😂 笑ったところ                                                      │
│ "これは非常に複雑な関数です" - そして2を掛けるだけ。                │
│ 死ぬほど笑った！😂                                                  │
│                                                                     │
│ 🤔 実際に良いところ                                                  │
│ 少なくとも命名は一貫しているね。                                    │
│                                                                     │
│ 💡 改善提案                                                          │
│ - 型ヒントを追加                                                    │
│ - より説明的な名前を検討                                            │
│ - 実際に複雑さを追加してみては？                                    │
│                                                                     │
│ 🎯 最終判定                                                          │
│ 2/10 - 友達にはお勧めしないが、少なくとも動作はする！              │
└─────────────────────────────────────────────────────────────────────┘
```

## 🤝 貢献

より多くの批判ペルソナや機能を追加したいですか？ぜひ貢献してください！

1. リポジトリをフォーク
2. 機能ブランチを作成
3. 改善を追加
4. プルリクエストを送信

## 📄 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細はLICENSEファイルを参照してください。

## ⚠️ 免責事項

このツールは娯楽と建設的フィードバックを目的としています。コードを批判するかもしれませんが、すべて良い意味での冗談です！コーディングスキルを向上させながら笑ってください。

---
