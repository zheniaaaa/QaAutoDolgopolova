from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class KcdCart(BasePage):
    URL = "https://bookclub.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(KcdCart.URL)


    # Choosing the section that we are interested in 
    def look_for_ineresting_section(self):
        section_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/header/div[3]/nav[1]/div/ul/li[1]/a")
        section_btn.click()

    def add_ineresting_book_to_cart(self):
        to_cart_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/section/section/section/section[1]/div[1]/div[4]/noindex/a/div/img")
        to_cart_btn.click()

    def try_to_open_cart(self):
        cart_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/header/div[3]/div/div[2]/div[9]/a/div")
        cart_btn.click()

    def delete_book_from_cart(self):
        delete_btn = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div[2]/div[1]/table/tbody/tr/td/form[1]/div[2]/table/tbody/tr[2]/td[6]/a")
        delete_btn.click()

    def go_to_another_section(self):
        section2_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/header/div[3]/nav[1]/div/ul/li[2]/a")
        section2_btn.click()

    def add_another_book_to_cart(self):
        to_cart = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/section/section/section/section[1]/div[1]/div[4]/noindex/a")
        to_cart.click()

    def add_one_more_book_to_cart(self):
        btn_tocart = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/section/section/section/section/section[1]/div[2]/div[4]/noindex/a")
        btn_tocart.click()
    
    # Increasing quantity of books
    def try_to_increase_qnt_of_books_to_10(self, qnt):
        qnt_elem = self.driver.find_element(By.ID, "count61392")
        qnt_elem.send_keys(qnt)

    def click_to_save_changes(self):
        click = self.driver.find_element(By.ID, "allcontent")
        click.click()

    # Work with promocod
    def enter_wrong_promocod(self, promocod):
        field_for_promocod = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div[2]/div[1]/table/tbody/tr/td/form[1]/div[2]/table/tbody/tr[5]/td[2]/div/div[1]/input")
        field_for_promocod.send_keys(promocod)

        btn_confirm = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/section/div[2]/div[1]/table/tbody/tr/td/form[1]/div[2]/table/tbody/tr[5]/td[2]/div/div[2]")
        btn_confirm.click()
        
        
        


   
