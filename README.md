# gekkan-io-2023-09-OrangePi5-microbit

# OSインストール後の環境構築手順

1. SSHの設定(下記のQiita記事の手順を実施)

- [OrangePi5(debian)でSSHできるようにする](https://qiita.com/Inoue_Minoru/items/64bfa3bec8915ae329a7)
- [OrangePi5(debian)でホスト名.localでSSHできるようにする](https://qiita.com/Inoue_Minoru/items/60b0c3b7a7abe03a500c)

2.  カメラの設定(下記のQiita記事の手順を実施)

[OrangePi5(debian)のカメラコネクタからOV13850を使ってみる](https://qiita.com/Inoue_Minoru/items/8fde94574657e3796f34)

3. UARTの設定(下記のQiita記事の手順を実施)

[OrangePi5(debian)でUART通信してみた](https://qiita.com/Inoue_Minoru/items/7ed9eafce2bc7852eb89)

4. OrangePi5にsshで入り、`git clone　https://github.com/henjin0/gekkan-io-2023-09-OrangePi5-microbit` を実行する。

- sshで入った直後のフォルダ(ホームディレクトリ:`/home/orangepi/`)にてコマンド実行

5. Teachable machineで学習データ取得



6. SCPコマンドでコピー

macOSである場合は、`result.zip`が存在するフォルダに移動し、下記コマンドを実行する。

```shell
scp result.zip orangepi@<OrangePi5のipアドレス or ドメイン名>:/home/orangepi/gekkan-io-2023-09-OrangePi5-microbit
```

7. `pip3 install -r requirement.txt`実行
