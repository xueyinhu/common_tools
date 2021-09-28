### 这是一个简易受限的Markdown文本语种转换器

---

<font size=3>这个脚本用于将Markdown中的中文文本转换成同等含义的日语等语种的文本，语种转换使用了百度翻译API。</font>

1. 使用步骤：

   1. 安装 mistletoe， html2text 模块

      ```shell
      pip install mistletoe
      pip install html2text
      ```

   2. 将要转换的 .md 文件替换 ./test/test.md

   3. 修改use.storage文件，写入appid、appkey、to_lang等参数，from_lang不需要修改，也不要新增行。

      ```text
      appid: ??? 百度翻译API的appid
      appkey: ??? 百度翻译API的appkey
      from_lang: zh
      to_lang: jp/en/... 百度翻译API提供的语种缩写
      ```

   4. 执行转换代码

      ```shell
      python start_conversion.py
      ```

2. 转换结果：

   1. 原先的中文文本markdown文件

      ```markdown
      #### Hello mistletoe! 好耶！
      
      ---
      
      <font size=3 color=red>你好，请帮我解析Markdown。</font>
      $$ s = 23 $$
      
      
      > 你要明白，你追寻的是快乐。
      
      `npm install marked`
      ```

   2. use.storage文件进行修改

      ```test
      to_lang: jp
      ```

      ```markdown
      #### Hello mistletoe! はい！
      
      * * *
      
      こんにちは，解析してくださいMarkdown。 $$ s = 23 $$
      
      > 分かります，あなたが探しているのは楽しみです。。
      
      `npm install marked`
      ```

   3. use.storages文件进行修改

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

      

   