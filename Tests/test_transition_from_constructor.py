from locators import StarBurgerMain
from config import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTransitionIngridients:

    def test_transition_to_breads(self, driver):
        driver.get(f'{URL}')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.BREAD_BUTTON).click()


    def test_transition_to_souce(self, driver):
        driver.get(f'{URL}')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.BREAD_BUTTON).click()


    def test_transition_to_toppings(self, driver):
        driver.get(f'{URL}')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.BREAD_BUTTON).click()



