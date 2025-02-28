class ECommercePage:
    def __init__(self, page):
        self.page = page

    def visit(self, path=""):
        self.page.goto(f"http://localhost:3000{path}")

    def verify_page_url(self, expected_path):
        assert expected_path in self.page.url

    def click_element(self, selector):
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        element.click()

    def click_element_by_text(self, text):
        element = self.page.get_by_text(text, exact=True)
        element.wait_for(state="visible")
        element.click()

    def enter_text(self, selector, text):
        self.page.locator(selector).fill(text)

    def verify_message_visible(self, message):
        self.page.get_by_text(message).wait_for(state="visible")

    def verify_message_not_visible(self, message):
        assert self.page.locator(message).count() == 0
