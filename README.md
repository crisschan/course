# Course  

**ppt直接转成视频，ppt备注内容转换为视频语音**

使用了腾讯云的tts接口，语音合成免费额度为每月100万字符，相当于一本《西游记》的字数。每月1日重置免费额度。 接口请求频率限制：20次/每秒。合成语音的源文本。中文最大支持600个汉字（全角标点符号算一个汉字），英文最大支持1800个字母（半角标点符号算一个字母）。
    https://cloud.tencent.com/document/product/1073/34093详情看代码。
## 使用

把PPT放到ppt文件夹中，在setting.py文件中修改对应的配置
去腾讯云申请免费使用的tss接口用量，将secretid和secretkey贴入setting.py文件的对应参数中
然后运行代码。

- 1 将ppt分解为图片和ppt的备注文字存入文本文件中（分别位于origin下的img和origin下的txt）
- 2 将txt中的文本通过腾讯云的接口生成对应的wav格式的音频
- 3 依据图片生成对应的视频，并将wav的音频混剪入视频中
- 4 上述过程一页ppt对应一个视频文件，然后将所有的视频合并成一个大的课件视频。
## requirements

这里的requirements文件是通过pipreqs生成的。

    pip3 install pipreqs
    pipreqs ./ --encoding=utf8

使用方法：

    pip install -r requriements.txt 

