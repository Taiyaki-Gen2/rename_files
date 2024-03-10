# 【Python】複数ある画像のファイル名を、自分の好きな名前で、一括で変更してみる！

## 背景
[Windowsでは、パスやファイル名、フォルダ名に長さの制限が設けられており、](https://atmarkit.itmedia.co.jp/ait/articles/2106/02/news024.html)その制限を超えると「指定されたファイル名は、無効かまたは長すぎます。」といった、様々なエラーが発生します。

また、Pythonによるファイル操作においてもエラーが発生します。私自身、畳み込みニューラルネットワーク（CNN）をはじめ、Pythonを使って、インターネットから取得した画像を操作することがよくありますが、長すぎるファイル名が原因で、画像が存在しているにもかかわらず、`FileNotFoundError`が発生したことがありました。

## 目的
前述したような問題を解決する1つの方法は、単純にファイル名を短くすることです。

しかし、場合によっては何千何万枚のファイル名を変える必要があり、手作業ではほぼ不可能な時があります。私自身、CNNを用いてAIに学習させるときは、何千何百といった画像を使います。

また、[Windowsには、選択したファイル名を一括で変更する機能があります。](https://www.yrl.com/column/wazaari_pc/change_to_sequential-file-name.html)しかし、この機能は「共通名 (連番)拡張子」というように、共通名の最後に(連番)が付くため、任意の箇所に連番を付けることができません。また、何千何万枚もファイルがある場合、全て選択するには手間がかかります。

そこで今回は、次のようなディレクトリ構成にある画像のファイル名を、一括、任意の名前、および一瞬で変更するPythonスクリプトを作成しました。

![ディレクトリ構成.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3690600/0159fe8b-37a3-af10-392f-852f83bbcb9c.png)

## コーディング
### コード全体
下記がコードの全体です。全11行で、ライブラリも`os`しか使わない非常にシンプルなものになっています。

```python:ex_rename_file.py
import os

dir_folders = input("\n- フォルダ名を入力してください: ")

dir_pictures = os.listdir(dir_folders)

for i in dir_pictures:
    number = 1
    for j in os.listdir(dir_folders + "/" + i):
        ext = os.path.splitext(j)[1]
        file_before = dir_folders + "/" + i + "/" + j
        file_after = dir_folders + "/" + i + "/" + i + "_" + str(number) + ext
        os.rename(file_before, file_after)
        number += 1
```

### コードの説明
次からコードの説明をします。先ほどのディレクトリ構成の図と合わせて説明します。

```python:ex_rename_file.py
import os
```

1行目は、今回使う`os`というライブラリをインポートしています。

```python:ex_rename_file.py
dir_folders = input("\n- フォルダ名を入力してください: ")
```

2行目は、[`input`](https://qiita.com/y-vectorfield/items/4330f36b4e6fe9d995ab)関数を使って、ターミナルで「folderディレクトリ」の名前を入力し、それを`dir_folder`に格納しています。

```python:ex_rename_file.py
dir_pictures = os.listdir(dir_folders)
```

3行目は、[`os.listdir`](https://qiita.com/Morio/items/f34dab8825c9d76664f5 )を使って、「folderディレクトリ」にある各「サブディレクトリ（pictureディレクトリ1, pictureディレクトリ2 etc.）」の名前を取得し、`dir_pictures`に格納しています。なお、次のように、各「サブディレクトリ」の名前はリストで格納されます。

![dir_pictures.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3690600/15f575ec-54bd-8825-20dc-f26669c6dd1b.png)

```python:ex_rename_file.py
for i in dir_pictures:
    number = 1
    for j in os.listdir(dir_folders + "/" + i):
        ext = os.path.splitext(j)[1]
        file_before = dir_folders + "/" + i + "/" + j
        file_after = dir_folders + "/" + i + "/" + i + "_" + str(number) + ext
        os.rename(file_before, file_after)
        number += 1
```

4行目から8行目は、[`for`](https://qiita.com/Morio/items/e8aed85346c0055beea7 )文を使って、各「サブディレクトリ」内の画像に対して、順番に名前の変更を行っています。

名前の変更には、[`os.rename`](https://qiita.com/shi_ei/items/44f6847e4275f21be1df)を使います。`os.rename`では、第一引数に変更前のファイルのパス、第二引数に変更後のファイルのパスを指定します。

今回、`file_after`を見てもらうとわかるように、変更後のファイル名が「(サブディレクトリ名)_(連番)(拡張子)」となるようにしています。また、拡張子は、[`os.path.splittext`](https://qiita.com/ramj/items/16b28b0bad323f1c6019)を使って取得し、変更前と変更後の拡張子が同じになるようにしています。

## 実行
「folderディレクトリ」があるディレクトリで、`ex_rename_file.py`を実行します。実行すると、次のように「folderディレクトリ」の名前の入力を求められるため、入力してEnterを押します。

![フォルダ名を入力してください.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3690600/e5ea2325-9c1e-13b4-3b15-0da8df8b867d.png)

#### 結果
下図が結果です。今回、`rename_test`という「folderディレクトリ」に、`cat`, `dog`, `elephant`, `giraffe`, `lion`の5つの「サブディレクトリ」があり、その中にそれぞれ画像が複数入っています。変更前と変更後を比較すると、全ての画像ファイルの名前が「(サブディレクトリ名)_(連番)(拡張子)」に変更されていることがわかります。

<img width="500" alt="結果.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3690600/3d72d705-a665-5508-e65b-6beee7a4c7d3.png">

## まとめ
数行の記述で、複数の画像のファイル名を、一括、任意の名前、および一瞬で変更するPythonスクリプトを作成しました。

今回は、サブディレクトリ内に数枚しか画像がありませんでしたが、何千何万枚ある場合でも問題なく動作します。

また、画像ファイルが対象でしたが、実際は、txtやpyなど、他のファイルの名前を変更する場合でも動作します。

最後に、今回がはじめての投稿なので、質問や不備、改善点などがありましたら、是非連絡してください。

# 参考

https://atmarkit.itmedia.co.jp/ait/articles/2106/02/news024.html

https://www.yrl.com/column/wazaari_pc/change_to_sequential-file-name.html

https://qiita.com/y-vectorfield/items/4330f36b4e6fe9d995ab 

https://qiita.com/Morio/items/f34dab8825c9d76664f5 

https://qiita.com/Morio/items/e8aed85346c0055beea7 

https://qiita.com/shi_ei/items/44f6847e4275f21be1df 

https://qiita.com/ramj/items/16b28b0bad323f1c6019
