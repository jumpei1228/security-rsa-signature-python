# デジタル署名をPythonで実装する｜RSAで「改ざん」を見抜くしくみ

公開鍵暗号による電子署名を、Pythonのcryptographyライブラリで手を動かして実装。秘密鍵で署名し公開鍵で検証する流れ、なぜ1文字の改ざんでも検知できるのかを、動くコードで確かめます。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[デジタル署名をPythonで実装する｜RSAで「改ざん」を見抜くしくみ](https://security.yurufuwa.work/learn/rsa-signature-python)** — ゆるふわサイバーセキュリティ

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python rsa-signature-python.py
```

## これは何？

[ゆるふわサイバーセキュリティ](https://security.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
