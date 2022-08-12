from selenium import webdriver
import pyautogui
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=options)

def test_setup():
    driver.maximize_window()  

def test_login():
    driver.get("https://stg-oauth.privy.id/login?client_id=v5SCIvXPW1ZO7LLj_Fu2Vj-RIkKUBjR_qkvNymBg4Co&redirect_uri=http%3A%2F%2Flocalhost%2Fauth%2Fcallback&response_type=code&state=eyJyZWRpcmVjdFVybCI6Ii9sb2dpbi9wcml2eSJ9&scope=public")
    driver.find_element_by_name("user[privyId]").send_keys("HJF9731")
    time.sleep(1)
    driver.find_element_by_css_selector("button.btn-alt").click()
    driver.find_element_by_css_selector("button.btn-alt").click()
    time.sleep(1)
    driver.find_element_by_name("user[secret]").send_keys("aha84c4")
    time.sleep(1)
    driver.find_element_by_css_selector("button.btn-alt").click()
    driver.find_element_by_css_selector("button.btn-alt").click()
    time.sleep(1)

def analytics():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/input[1]').click()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/input[1]').clear()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/input[1]').send_keys("testing senin")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/span').click()
    time.sleep(2)                 

def test_subscriberlist():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/nav/div[1]/div[2]/div[1]/div[1]/div[2]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/nav/div[1]/div[2]/div[1]/div[2]/a[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[3]/div/div[1]/div/div/div/div[1]/input').send_keys("subscriber example")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dashboard-app"]/div/main/div/div[1]/div/button/span').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/span/div/div[1]/div[1]/div/div[2]/button/span').click()
    time.sleep(2)

    pyautogui.write("tes.jpg")
    pyautogui.press("enter") 
    time.sleep(4)

    #npwp
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div/span/div/div[1]/div[2]/form/div[2]/div/div/span/div/div/div[1]/div/input').send_keys("966657739246387")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dashboard-content"]/div/span/div/div[1]/div[2]/form/div[2]/button[1]/span').click()
    time.sleep(4)

    pyautogui.write("tes.jpg")
    pyautogui.press("enter") 
    time.sleep(4)

    #nama
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div/span/div/div[1]/div[2]/form/div[4]/div/span/div/div/div[1]/div/input').send_keys("test")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div/span/div/div[1]/div[2]/form/div[6]/div/span/div/div/div[1]/div/input').send_keys("089507747573")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div/span/div/div[1]/div[2]/form/div[8]/div/span/div/div/div/div/textarea').send_keys("jakarta")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div/span/div/div[1]/div[2]/form/div[12]/div/span/div/div/div[1]/div/input').send_keys("HJF9731")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div[2]/form/div[20]/div/div/div[2]/div/span/div/div/div/div/input').send_keys("product-dendy")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div[2]/form/div[20]/div/div/div[4]/div/span/div/div/div/div/input').send_keys("project-dendy")
    time.sleep(2)
    #button next tahap 1
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[2]/button').click()
    time.sleep(2)
    #addmoredocument
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div[1]/div[2]/button/span/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/span/div/div[1]/div[2]/form/div/button[2]/span').click()
    time.sleep(2)

    pyautogui.write("tes.pdf")
    pyautogui.press("enter") 
    time.sleep(4)

    #button next tahap 2
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[2]/button[2]/span').click()
    time.sleep(2)
    #button next tahap 3
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[2]/button[2]/span').click()
    time.sleep(4)
    #button next tahap 4
    driver.find_element_by_xpath("//div[@id='dashboard-content']/div/div[3]/div[4]/button[2]/span").click()
    time.sleep(5)           
    driver.find_element_by_css_selector("i.v-icon.notranslate.mdi.mdi-close.theme--light").click()
    time.sleep(2)

def test_changerequest():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/nav/div[1]/div[2]/div[1]/div[2]/a[2]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div[1]/input').send_keys("tes")

def test_invoice():
    driver.find_element_by_link_text('Invoice').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[1]/input').send_keys("2022/INV/SUBE3AB4C/12-1")
    time.sleep(2)                 

def test_user():
    driver.find_element_by_link_text("User").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='btn:user/add']").click()
    time.sleep(1)
    driver.find_element_by_css_selector("[test-id='input:user/add-dialog/privyid']").send_keys("tes")
    time.sleep(1)
    driver.find_element_by_css_selector("[test-id='input:user/add-dialog/name']").send_keys("tes")
    time.sleep(1)                         
    driver.find_element_by_css_selector("[test-id='btn:user/add-dialog/save']").click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/span/div[1]/div[1]/div/div[1]/div/div/div/div[1]/input').send_keys("tes")
    time.sleep(2)

def test_enterprise():
    driver.find_element_by_link_text("Enterprise").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='input:filter/enterprise/company-name']").send_keys("test")
    time.sleep(3)                 

def test_activitylog():
    driver.find_element_by_link_text("Activity Log").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='input:filter/activity-log/name']").send_keys("Get List Actifity Log Privy")
    time.sleep(5)

def test_notification():
    driver.find_element_by_css_selector('i.v-icon.notranslate.mdi.mdi-bell-outline.theme--light').click()
    time.sleep(3)
    #driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/footer/button/span').click()
    #time.sleep(1)                 