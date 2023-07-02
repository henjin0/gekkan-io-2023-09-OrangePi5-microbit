# gekkan-io-2023-09-OrangePi5-microbit

## 動作環境(OrangePi5側)
- OS: debian1.1.4(bullseye)
- 使用カメラ: ov13850
- node.js: v14.21.3
- npm: npm@6.14.18
- Node-RED v3.0.2 (npm install)
- Python 3.9.1

## OSインストール後の環境構築手順
下記の手順を実行する前に、OrangePi5をネットにつなげるようにしておく。
- 有線LANであれば、そのままLANケーブルとルーターを繋げばOK
- 無線LANであれば、下記のUSBドングルを挿せば接続可能。また、ディスプレイなどを繋いで画面右の無線LANマークからLANに接続しておく。

https://amzn.asia/d/5rllfbl

また、teachable machineによる学習データ作成とSSHによるファイル送受のため、同じLANの中に母艦となるPCを別に用意しておく。

### 1. SSHの設定
下記のQiita記事の手順を実施
- [OrangePi5(debian)でSSHできるようにする](https://qiita.com/Inoue_Minoru/items/64bfa3bec8915ae329a7)
- [OrangePi5(debian)でホスト名.localでSSHできるようにする](https://qiita.com/Inoue_Minoru/items/60b0c3b7a7abe03a500c)

### 2.  カメラの設定
下記のQiita記事の手順を実施した。また、今回はカメラを自立させやすい都合からcam2コネクタを使いました。
- [OrangePi5(debian)のカメラコネクタからOV13850を使ってみる](https://qiita.com/Inoue_Minoru/items/8fde94574657e3796f34)

### 3. UARTの設定
下記のQiita記事の手順を実施
- [OrangePi5(debian)でUART通信してみた](https://qiita.com/Inoue_Minoru/items/7ed9eafce2bc7852eb89)

### 4. 本リポジトリをcloneする
OrangePi5にsshで入り、`git clone　https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit` を実行する。
- sshで入った直後のフォルダ(ホームディレクトリ:`/home/orangepi/`)にてコマンド実行

### 5. Teachable machineで学習データ取得
- 下記リンクにアクセスし、`画像プロジェクト`→`標準の画像モデル`を選択する。

[teachable machine](https://teachablemachine.withgoogle.com/train)

<img width="1225" alt="スクリーンショット 2023-07-02 19 59 43" src="https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit/assets/6815823/b381189b-6231-4c27-b98b-a6b516e8025f">

<img width="1225" alt="スクリーンショット 2023-07-02 20 00 06" src="https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit/assets/6815823/9743245b-e545-4c50-ab6c-4ba482157e8e">

- クラス名を`smile`と`neutral`にし、それぞれの表情で学習させる。学習時の枚数は100~150枚でOK。

![smile_neutral](https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit/assets/6815823/3f1b7967-be5c-4fd9-97e0-a67425417029)

学習する際の手順はこちらを参照すると非常にわかりやすいです！
[Teachable Machine Tutorial 2: Train](https://www.youtube.com/watch?v=CO67EQ0ZWgA&t=1s&ab_channel=ExperimentswithGoogle)

- `プレビュー`の`モデルをエクスポートする`をクリックし、`Tensorflow`→`Keras`→`モデルをダウンロード`を選択する。

<img width="381" alt="image" src="https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit/assets/6815823/a65d1ca4-9d7b-416e-88a0-6ff93a5a1768">

<img width="840" alt="スクリーンショット 2023-07-02 20 35 16" src="https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit/assets/6815823/c449f852-aaab-4ac4-997f-01920b1616e0">

`converted_keras.zip`がダウンロードされるため、zipを展開する。

### 6. SCPコマンドでコピー
macOSである場合は、`converted_keras.zip`の展開後フォルダの中へ移動し、下記コマンドを実行する。

```shell
scp <converted_keras内までのフォルダパス>/keras_model.h5 orangepi@<OrangePi5のipアドレス or ドメイン名>:/home/orangepi/gekkan-io-2023-09-OrangePi5-microbit
```

```shell
scp <converted_keras内までのフォルダパス>/labels.txt orangepi@<OrangePi5のipアドレス or ドメイン名>:/home/orangepi/gekkan-io-2023-09-OrangePi5-microbit
```

### 7. Python側準備
`pip3 install -r requirement.txt`を実行し、パッケージをインストールする

### 8. node.js(v14.21.3)をインストールする。
下記の記事などを参考に、nvm経由でインストールするとなお良し。

https://maku77.github.io/nodejs/env/nvm.html

### 9. node-redインストール
下記手順に基づいて、node-redをインストールする。

https://nodered.jp/docs/getting-started/local

### 10. ローカルPCで接続確認
- `/home/orangepi/gekkan-io-2023-09-OrangePi5-microbit`で`node-red`コマンドを実行する。
- 同じLAN内にあるPCのブラウザから`<OrangePi5のipアドレス or ドメイン名>:1880`にアクセスしたときに、画面上にnode-redのダッシュボードが表示されることを確認する。

### 11. node-redフロー準備
下記リンクの`flow.json`を展開し、動作することを確認する。

`flow.json`の展開方法は下記リンクを参考に実施する。

https://nodered.jp/docs/user-guide/editor/workspace/import-export
