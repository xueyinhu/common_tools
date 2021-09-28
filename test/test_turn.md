### これは簡単に制限されているMarkdownテキスト言語変換器

* * *

このスクリプトはMarkdownの中国語テキストを同じ意味の日本語などの言語に変換します。，言語の変換に百度の翻訳が使われました。API。

  1. 使用手順：

    1. インストール mistletoe， html2text モジュール
        
                pip install mistletoe
        pip install html2text
        

    2. 変換する .md ファイル置換 ./test/test.md

    3. 変更use.storageファイル，書き込みappid、appkey、to_langパラメータ，from_lang不需要変更，行を追加しないでください。
        
                appid: ??? バイドゥの翻訳APIのappid
        appkey: ??? バイドゥの翻訳APIのappkey
        from_lang: zh
        to_lang: jp/en/... バイドゥの翻訳API提供の语种缩写
        

    4. 変換コードを実行
        
                python start_conversion.py
        

  2. 結果を変換：

    1. 原先の中文文本markdownファイル
        
                #### Hello mistletoe! はい！
        
        ---
        
        <font size=3 color=red>こんにちは，解析してくださいMarkdown。</font>
        $$ s = 23 $$
        
        
        > ポイントかります，你追寻の是快乐。
        
        `npm install marked`
        

    2. use.storageファイル进行変更
        
                to_lang: jp
        
        
                #### Hello mistletoe! はい！
        
        * * *
        
        こんにちは，解析してくださいMarkdown。 $$ s = 23 $$
        
        > ポイントかります，あなたが探りを入れるしているのは楽しみしみです。。
        
        `npm install marked`
        

    3. use.storagesファイル进行変更
        
                to_lang: en
        
        
                #### Hello mistletoe! Allyes ！
        
        * * *
        
        Hello，Please help me analyzeMarkdown。 $$ s = 23 $$
        
        > You have to understand，What you seek is happiness。
        
        `npm install marked`
        

