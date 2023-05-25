
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.top_bars.top_navigate_bar import TopNavigateBar


class TemplatesPage(TopNavigateBar):
    """ Templates page - contains variety of templates to select """

   # _TEMPLATES_BLOCK = (By.CSS_SELECTOR, "#template-gallery tbody tr")
    _TEMPLATES_BLOCK = (By.XPATH,"//ul[@class='absolute right-0 z-20 py-1 mt-2 w-auto min-w-full text-left text-gray-700 whitespace-nowrap bg-white rounded-md ring-1 ring-black ring-opacity-5 shadow-lg origin-top-right focus:outline-none']//p[@class='text-base font-normal group-hover:text-white']")
    _CHOOSE_BUTTON = (By.CSS_SELECTOR, "a .btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_template(self, template_name: str) -> None:
        self._wait.until(
            expected_conditions.visibility_of_all_elements_located(self._TEMPLATES_BLOCK))
        templates = self._wait.until(expected_conditions.visibility_of_all_elements_located(self._TEMPLATES_BLOCK))
        for template in templates:
            if template_name in template.text:
                #button = template.find_element(*self._CHOOSE_BUTTON)
                button = template.find_element(*self._TEMPLATES_BLOCK)
                self.move_to_element(button)
                button.click()
                break
