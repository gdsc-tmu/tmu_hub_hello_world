# TMU Hub - Project Hello World
### Introduction

Hello World プロジェクトは，プロジェクト開発に参加したいがやり方がわからない方のために作った入り口プロジェクトなのである．Frontend と Backend を作り，実際に自分のページを一緒に作る．

### Preparation

このプロジェクトでは，Backend (Python, Django), Frontend (HTML, CSS) の基礎を触れます．執行はサーバーで行うので，ローカルでは Editor と Git さえあれば十分である．

`git clone` でプロジェクトをダウンロードする．

```bash
git clone https://github.com/gdsc-tmu/tmu_hub_hello_world.git
```

Windows を利用している方は，Git の代わりに Github Desktop を利用することも可能である．

### Structure

プロジェクトの主要部は，各 folder によって構成される．．ここでのフォルダー名は後で URL の naming space として使われる．まず１つ folder を新規に作って，先着順で好きな名前をつけよう．自分が作ったフォルダーを自由にいじって良いが，他人のフォルダーを触れないようにしよう．

なお，[`sora/`](https://github.com/gdsc-tmu/tmu_hub_hello_world/tree/main/sora) folder はサンプルとして作られた．これから，`sora/` 内の構造を解説しながら，真似して自分の folder を作るお．

`sora/` 内のファイル・フォルダーはおおよそ次のようになる．

- `static/` ：image, css, js, audio などの置き場．[kwsk](https://docs.djangoproject.com/en/4.1/howto/static-files/)
  - `冬の街路樹 Sora H.flac` ：サンプル static ファイル．ただのピアノ曲．
- `templates` ：html template の置き場．[kwsk](https://docs.djangoproject.com/en/4.1/topics/templates/)
  - `home.html` ：サンプル html ファイル．
- `__init__.py` ：空の `.py` ファイル．これによってフォルダーを上位プロジェクト TMU-Hub において Python のモジュールとして認識される．[kwsk](https://docs.python.org/3/reference/import.html#regular-packages)
- `urls.py` ：URL Dispatcher．すなわち URL ルートを定義するファイル．[kwsk](https://docs.djangoproject.com/en/4.1/topics/http/urls/)
- `views.py` ：ページを定義するファイル．

### Templates

