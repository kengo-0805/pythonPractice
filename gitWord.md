# Git基本事項
# 用語
## コミット
ユーザーが任意のタイミングで記録を保存する操作．
## リポジトリ
コミットを貯めておく場所．

すでにGitで管理されているプロジェクトの開発に参加する場合はリポジトリをコピー（クローン）して使う．

### ワークツリー
変更するファイルを保持する場所．
### ステージングエリア
コミットするファイルを登録する場所．
### Gitディレクトリ
コミットを格納する場所．

# GitHubにあげるまでの手順
今回はGitのインストールやGitHubのアカウント作成などの初期設定の説明は省く．

あらかじめ登録してある人が新しいプロジェクトを始めるという状況を想定．
1. リモートリポジトリをローカルへ複製する or ローカルで作成したリポジトリをリモートへ反映させる

    今回はリモート側のリポジトリとして先にGitHubへリポジトリを作成し，それをローカルへ複製するという方法で進める．
    ```
    $ git clone GitHubのリポジトリURL
    ```
    
    例）
    
    ```
    $ git clone https://github.com/kengo-0805/lab_memo
    ```
    GitHubのファイルが複製されるので cd コマンドでコピーしたディレクトリに移動する．

2. 作業用ブランチを作成する

    Gitではbranchを作成し作業を行い，完成したらmasterにmergeするのが基本なのでここでbranchを作成する．

    以下のコマンドで現在いるbranchが確認できる．
    ```
    $ git branch
    * master
    ```
    ブランチの作成には以下のコマンドを使う．
    ```
    $ git branch ブランチ名
    ```
    例）
    ```
    $ git branch work
    ```

    ブランチを作成したら以下のコマンドでブランチを切り替える

    ```
    $ git checkout ブランチ名
    ```

    例）
    ```
    $ git checkout work
    ```
    ブランチを切り替えたらファイルの編集を行い，バージョンアップを行う．


    
3. コミットをする
    
    書き換えたファイルはリモートリポジトリに保存しておきたいので以下のコマンドを実行する．
    ```
    $ git add ファイル名
    ```
    このコマンドで指定したファイルがコミット対象になる．
    
    今回はフォルダにあるファイルを全てコミットする予定なので以下のコマンドを実行する．
    ```
    $ git add .
    ```
    これでコミットの準備ができたので以下のコマンドでコミットを行う．
    ```
    $ git commit -m 'コメント’
    ```
    これでコミットは完了．（-mを付けなかった場合はvi上でコメントの入力を求められる．）

4. ブランチをマージする
    
    今回はmasterにworkを取り込む．
    
    まずはmasterブランチに移動する．
    ```
    $ git checkout master
    Switched to branch 'master'
    Your branch is up to date with 'origin/master'.
    ```
    このまま編集したファイルを開いてもブランチを切り替えているので変更が反映されていない．

    例）
    ```
    $ git merge work
    Updating ac63b89..3eefb35
    Fast-forward
    README.md | 1 +
    1 file changed, 1 insertion(+)
    ```
    このコマンドでマージが成功すると編集した内容がmasterに反映される．

5. リモートにpushをする
    
    いよいよ変更内容をGItHubに反映させる．
    
    例）
    ```
    $ git push origin work
    Counting objects: 3, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 338 bytes | 338.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    remote: 
    remote: Create a pull request for 'work' on GitHub by visiting:
    remote:      https://github.com/kengo-0805/lab_memo/pull/new/work
    remote: 
    To https://github.com/kengo-0805/lab_memo
    * [new branch]      work -> work
    ```
    これでGitHubにちゃんと反映されていたら成功！
    
6. おさらい

    大事なのは以下のコマンドでこの流れは絶対である．
    ```
    $ git clone URL
    $ git add .
    $ git commit -m 'コメント'
    $ git push origin master
    ```
7. 知っていると便利なコマンド


    ```
    $ git status
    ```
    このコマンドで今の状態を確認できる．

    慣れるまでは何かを実行するたびにこのコマンドで確認した方がいいかも．
    ```
    $ git branch
    ```
    このコマンドで現在どのブランチにいるのかを確認できる．
8. 不十分な点
    - 開発はGitHub→Gitという流れよりローカル→リモートという流れが自然？
    - ブランチ切ったままファイルの移動をしてしまった場合どうなっちゃう？