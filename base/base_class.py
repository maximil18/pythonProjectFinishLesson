import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method get current URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    # Method assert words

    def assert_words(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # Method Screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        self.driver.save_screenshot(f'C:\\Users\\maksim.marfutov\\PycharmProjects\\pythonProjectFinishLesson\\screen\\screenshot{now_date}.png')

    # Method arrest url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good url')

