from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class TrackingNovaPoshta(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(TrackingNovaPoshta.URL)

    def try_to_track_parcel(self, number_of_parcel):
        number_elem = self.driver.find_element(By.ID, "en")
        number_elem.send_keys(number_of_parcel)

        search_btn = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        search_btn.click()


    def check_title(self, expected_title):
        return self.driver.title == expected_title