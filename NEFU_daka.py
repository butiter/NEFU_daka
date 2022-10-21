from selenium import webdriver
import time



count_id = "你的学号"
count_psd = "你的密码"
userinput_mounth = 10 # 打卡的月份
userinput_begin_day = 2 # 打卡的起始日期
userinput_end_day = 20 # 打卡的结束日期
userinput_url = r"核酸截图全路径"


def get_str(x):
    if len(str(x)) < 2:
        return "'" + '0' + str(x) + "'"
    else:
        return "'" + str(x) + "'"



login_statu= False
browser = webdriver.Chrome()
while not login_statu:
    try:
        browser.get('http://dlyx.nefu.edu.cn/xsfw/sys/swmxggzptapp/*default/index.do')
        browser.find_element_by_id('un').send_keys(count_id)
        browser.find_element_by_id('pd').send_keys(count_psd)
        time.sleep(1)
        print (browser.current_url)
        browser.find_element_by_class_name('login_box_landing_btn').click()  # 成功
        print (browser.current_url)
        login_statu = True
        time.sleep(1)
    except:
        login_statu = False


for userinput_now_day in range(userinput_begin_day, userinput_end_day):
    browser.get('http://dlyx.nefu.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do#/')
    browser.refresh()
    time.sleep(3)
    browser.find_element_by_xpath("//div[text()='本科生组']").click()
    browser.get('http://dlyx.nefu.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do#/btadd')
    time.sleep(2)
    ls = browser.find_element_by_class_name("mt-bColor-after-grey-lv5").find_elements_by_class_name("emapm-item")

    ls[0]# 学号
    ls[1]# 姓名
    ls[2]# 日期
    #region ls[2]
    ls[2].click()
    time.sleep(1)
    #ls[2].find_element_by_xpath("//span[text()='19']").click()
    ck = ls[2].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    ymd = browser.find_elements_by_class_name("mint-picker-column")
    ymd[0].find_element_by_xpath("//span[text()='2022']").click()
    print(get_str(userinput_mounth))
    ymd[1].find_element_by_xpath("//span[text()=" + get_str(userinput_mounth) + "]").click()
    ymd[2].find_elements_by_xpath("//span[text()=" + get_str(1) + "]")[1].click()
    time.sleep(1)
    if userinput_now_day <= 12:
        for i in range(1,userinput_now_day + 1):
            ymd[2].find_elements_by_xpath("//span[text()=" + get_str(i) + "]")[1].click()
    else:
        for i in range(1,13):
            ymd[2].find_elements_by_xpath("//span[text()=" + get_str(i) + "]")[1].click()
        for i in range(13,userinput_now_day + 1):
            ymd[2].find_elements_by_xpath("//span[text()=" + get_str(i) + "]")[0].click()
    ymd[1].find_element_by_xpath("//span[text()=" + get_str(userinput_mounth) + "]").click()
    browser.find_element_by_xpath("//div[text()='确定']").click()
    #endregion
    ls[3]# 体温
    #region ls[3]
    browser.find_element_by_class_name("mint-field-core").send_keys("36")
    #endregion
    ls[4]# 是否确诊
    ls[5]# 是否疑似
    ls[6]# 是否密接
    ls[7]# 是否无症状
    ls[8]# 是否集中隔离
    ls[9]# 是否居家隔离
    ls[10]# 本人健康状况
    ls[11]# 是否医院就诊
    ls[12]# 家庭成员健康状况
    ls[13]# 系统生成居住地
    ls[14]# 居住地
    #region ls[14]
    ls[14].click()
    time.sleep(1)
    ck = ls[14].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    hlj = browser.find_element_by_xpath("//span[text()='黑龙江省']")
    browser.execute_script("$(arguments[0]).click()", hlj)
    time.sleep(1)
    hrb = browser.find_element_by_xpath("//span[text()='哈尔滨市']")
    browser.execute_script("$(arguments[0]).click()", hrb)
    time.sleep(1)
    sxq = browser.find_element_by_xpath("//span[text()='市辖区']")
    browser.execute_script("$(arguments[0]).click()", sxq)
    time.sleep(1)
    #endregion
    ls[15]# 是否疫区
    ls[16]# 是否有变化
    ls[17]# 填写类型
    ls[18]# 作废元素
    ls[19]# 是否已返校
    #region ls[19]
    ls[19].click()
    time.sleep(1)
    ck = ls[19].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    shi = browser.find_element_by_xpath("//span[text()='是']")
    browser.execute_script("$(arguments[0]).click()", shi)
    time.sleep(1)
    #endregion
    ls[20]# 健康码颜色
    ls[21]# 作废元素
    ls[22]# 是否全天在校
    #region ls[22]
    ls[22].click()
    time.sleep(1)
    ck = ls[22].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    shi = browser.find_elements_by_xpath("//span[text()='是']")[2]
    browser.execute_script("$(arguments[0]).click()", shi)
    time.sleep(1)
    #endregion
    ls[23]# 是否居家健康检测
    ls[24]# 其他情况
    ls[25]# 作废元素
    ls[26]# 作废元素
    ls[27]# 作废元素
    ls[28]# 核酸检测时间
    #region ls[28]
    ck = ls[28].find_element_by_class_name("mt-bg-after-grey")
    browser.execute_script("$(arguments[0]).click()", ck)
    ck = ls[28].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    ck = ls[28].find_element_by_class_name("mint-cell-no-bottom-line")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    new = browser.find_elements_by_class_name("mint-picker__columns")[1]
    ymd = new.find_elements_by_class_name("mint-picker-column")
    new.click()
    time.sleep(1)
    ymd[0].click()
    ymd[0].find_elements_by_xpath("//span[text()='2022']")[1].click()
    time.sleep(1)
    # if userinput_now_day <= 12:
    #     ymd[2].click()
    #     ymd[2].find_elements_by_xpath("//span[text()=" + date + "]")[2].click()
    # else:
    #     ymd[2].click()
    #     ymd[2].find_elements_by_xpath("//span[text()=" + date + "]")[1].click()
    ymd[2].find_elements_by_xpath("//span[text()='01']")[2].click()
    time.sleep(1)
    ymd[1].click()
    ymd[1].find_elements_by_xpath("//span[text()=" + str(userinput_mounth) + "]")[2].click()
    time.sleep(1)

    if userinput_now_day <= 12:
        for i in range(1,userinput_now_day + 1):
            tmp_date = get_str(i)
            ymd[2].find_elements_by_xpath("//span[text()=" + tmp_date + "]")[3].click()
    else:
        ymd[2].click()
        for i in range(1,13):
            tmp_date = get_str(i)
            ymd[2].find_elements_by_xpath("//span[text()=" + tmp_date + "]")[3].click()
        for i in range(13,userinput_now_day + 1):
            tmp_date = get_str(i)
            ymd[2].find_elements_by_xpath("//span[text()=" + tmp_date + "]")[1].click()
    time.sleep(1)
    browser.find_elements_by_xpath("//div[text()='确定']")[1].click()
    #endregion
    ls[29]# 核酸检测结果
    #region ls[29]
    ls[29].click()
    time.sleep(1)
    ck = ls[29].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    time.sleep(1)
    shi = browser.find_element_by_xpath("//span[text()='阴性']")
    browser.execute_script("$(arguments[0]).click()", shi)
    time.sleep(1)
    #endregion
    ls[30]# 截图上传
    #region ls[30]
    ck = ls[30].find_element_by_class_name("is-require")
    browser.execute_script("$(arguments[0]).click()", ck)
    ls[30].find_element_by_class_name("upload-file-wrap").send_keys(userinput_url)
    #endregion
    time.sleep(1)
    browser.find_element_by_xpath("//button[text()='提交']").click()
    time.sleep(2)
