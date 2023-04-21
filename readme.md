# 语音转文字与文字转语音实现(基于科大讯飞平台)

## 1.安装

确保你所处的操作系统已安装ffmpeg、python版本大于或等于3.8

然后cd到工程目录下

安装所需依赖：

```bash
pip install -r requirements.txt
```

## 2.配置科大讯飞API

去[科大讯飞开放平台官网](https://www.xfyun.cn/)主策并申请语音识别的API并免费领取在线文字转语音和语音转文字次数后,获取到**APP_ID、API_KEY**与**SECRET_KEY**并将其填写到**ifly_api.txt**

例如：

```bash
APP_ID:123456789
API_KEY:xxxxxxxxxxxxxxxxxxx
SECRET_KEY:xxxxxxxxxxxxxxx
```

## 3.开始使用

打开终端输入如下指令即可开始使用

```
python main.py
```

根据提示可以录入声音并转化为文字，而后将文字转化为合成语音。
