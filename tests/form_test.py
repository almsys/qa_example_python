from pages.form_page import FormPage
from conftest import driver

class TestFormPage:
    def test_form(self, driver):  # Фикстура driver подключается автоматически
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        first_name, last_name, email = form_page.fill_fields_and_submit()
        result = form_page.form_result()
         # Пример проверки результата
        print(first_name, last_name, email)
        print(result)
        #assert "Thanks for submitting the form" in driver.page_source
        assert f'{first_name} {last_name}' == result[0]
        assert email == result[1]