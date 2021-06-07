import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import *
from tkinter import messagebox

root = Tk()
email = StringVar()
password = StringVar()
times = IntVar()

def execute_bot():
    if email.get() != "" and password.get() != "" and times.get() != 0:
        bot = Bot(email.get(), password.get(), int(times.get()))
    else:
        messagebox.showerror(message="The fields are empty!", title="ERROR!")

class Bot:
    def __init__(self, email, password, times):
        self.email = email
        self.password = password
        self.times = times
        self.configure_selenium()

    def configure_selenium(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome()
        self.login(driver)
    
    def login(self, driver):
        driver.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
        elem = driver.find_element_by_xpath('//*[@id="username"]')
        elem.clear()
        elem.send_keys(self.email)
        elem = driver.find_element_by_xpath('//*[@id="password"]')
        elem.clear()
        elem.send_keys(self.password)
        elem = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
        elem.click()

        self.go_to_linkedin_my_network(driver)

    def go_to_linkedin_my_network(self, driver):
        for time in range(0, self.times):
            driver.get("https://www.linkedin.com/mynetwork/")
            wait = WebDriverWait(driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width']")))
            self.to_click(driver)
        messagebox.showinfo(message="The automation has been ended!")
        driver.close()

    def to_click(self, driver):
        profiles = driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width']")
        for profile in profiles:
            try:
                driver.execute_script("arguments[0].click();", profile)
                sleep(1)
            except:
                break

Label(root, text="Email: ").grid(row=0, column=0)
Label(root, text="Password: ").grid(row=1, column=0)
Label(root, text="Times: ").grid(row=2, column=0)

entry_email = Entry(root, textvariable=email)
entry_email.grid(row=0, column=1)

entry_password = Entry(root, textvariable=password)
entry_password.grid(row=1, column=1)

entry_times = Entry(root, textvariable=times)
entry_times.grid(row=2, column=1)

Button(root, text="Use the bot!", command=execute_bot).grid(row=3, column=0, columnspan=2)

root.title("Linkedin Bot")
root.geometry("200x100")
root.resizable(False, False)
root.mainloop()

