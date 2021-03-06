### これは簡単に制限されているMarkdownテキスト言語変換器

---

<font size=3>このスクリプトはMarkdownの中国語テキストを同じ意味の日本語などの言語に変換します，言語の変換に百度の翻訳が使われましたAPI。</font>

1. 使用手順：

   1. 変換する .md ファイル置換 ./test/test.md

   2. 変更use.storageファイル，書き込みappid、appkey、to_langパラメータ，from_lang不需要変更，行を追加しないでください。

      ```text
      appid: ??? バイドゥの翻訳APIのappid
      appkey: ??? バイドゥの翻訳APIのappkey
      from_lang: zh
      to_lang: jp/en/... バイドゥの翻訳API提供する言語の略語
      ```

   3. 変換コードを実行

      ```shell
      python start.py
      ```

2. 結果を変換：

   1. 最初の中国語テキストmarkdownファイル

      ```markdown
      #### Hello mistletoe! 好耶！
      
      ---
      
      <font size=3 color=red>你好，请帮我解析Markdown。</font>
      $$ s = 23 $$
      
      > 你要明白，你追寻的是快乐。
      
      `npm install marked`
      ```

   2. use.storageファイルを変更します

      ```test
      to_lang: jp
      ```

      ```markdown
      #### Hello mistletoe! はい！
      
      * * *
      
      こんにちは，解析してくださいMarkdown。 $$ s = 23 $$
      
      > ポイントかります，あなたが探りを入れるしているのは楽しみしみです。
      
      `npm install marked`
      ```

   3. use.storagesファイルを変更します

      ```text
      to_lang: en
      ```

      ```markdown
      #### Hello mistletoe! Allyes ！
      
      * * *
      
      Hello，Please help me analyzeMarkdown。 $$ s = 23 $$
      
      > You have to understand，What you seek is happiness。
      
      `npm install marked`
      ```

      

   