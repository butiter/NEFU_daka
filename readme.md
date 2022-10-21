# 学工部打卡





### 使用教程：

- 首先，下载对应chrome版本的chromedriver，并安装chrome浏览器。

  - chrome浏览器106.0.5249.119对应chromedriver已附在文件中
  - 其他版本可前往http://chromedriver.storage.googleapis.com/index.html 下载
  - 顺便一提，版本号不用完全对的上，差不多就行

- 然后，安装selenium库。

  - 笔者所使用的版本是2.48.0。

  - Python版本是3.8

  - selenium新版本中，很多方法名字都变了，建议下载俺这个版本

  - ```text
    pip install selenium==2.48.0
    ```

- 最后，更改代码的如下信息：

- ```python
  count_id = "XXXXXXXXXX" # 你的学号哦
  count_psd = "你的密码" # 你的密码哦
  userinput_mounth = 10 # 打卡的月份
  userinput_begin_day = 2 # 打卡的起始日期
  userinput_end_day = 20 # 打卡的结束日期
  userinput_url = r"核酸截图全路径"
  ```

- 最最后，点击运行！
  - 本程序会自动在打卡月份的[userinput_begin_day,userinput_end_day]区间内自动打卡。

- 示例：

- ```python
  count_id = "2222222222" # 你的学号哦
  count_psd = "passwd" # 你的密码哦
  userinput_mounth = 10 # 打卡的月份
  userinput_begin_day = 2 # 打卡的起始日期
  userinput_end_day = 20 # 打卡的结束日期
  userinput_url = r"C:\Users\source\repos\P1.png"
  
  # 他就会对2222222222用户，从10.2号，一直打卡到10.20号
  每次上传的核酸截图都是同一张，P1.png
  ```




### 免责声明

- 请严格遵守当地防疫法律法规，本代码仅供selenium库学习使用，所产生的一切法律纠纷，与本人无关。
- 疫情当前，防疫为重，使用此代码前，必须声明：你严格的遵守了一切核酸安排，次次不落；使用本代码只是为了减少重复的工作量、学习Python。
- 如果在没做核酸的情况下声明自己做核酸了，这是违反法律法规的！！！！！！！
- 如有侵权等纠纷，请联系本人，本人将即刻删除。