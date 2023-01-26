from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, '[class="input__control mini-suggest__input"]')
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CSS_SELECTOR, '[class="mini-suggest__popup-content"]')
    LOCATOR_YANDEX_LINK_CLASS = (By.CSS_SELECTOR, '[class="Link Link_theme_normal OrganicTitle-Link organic__url link"]')
    LOCATOR_YANDEX_PICS = (By.CSS_SELECTOR, '[class="navigation__item navigation__item_name_images"]')
    LOCATOR_YANDEX_SEARCH_PICS_RESULT = (By.CSS_SELECTOR, '[class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    LOCATOR_YANDEX_SEARCH_FIELD_TEXT = (By.CSS_SELECTOR, '[class="input__control mini-suggest__input"]')
    LOCATOR_YANDEX_PHOTO = (By.CSS_SELECTOR, '[class="MMImage-Preview"]')
    LOCATOR_YANDEX_ARROW = (By.CSS_SELECTOR, '[class="CircleButton-Icon"]')
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, '[class="serp-item__link"]')
    LOCATOR_YANDEX_MODAL_FORM = (By.CSS_SELECTOR, '[class="Modal Modal_visible Modal_theme_normal MMViewerModal ImagesViewer"]')
    LOCATOR_YANDEX_SELF_IMG_NAME = (By.CSS_SELECTOR, '[class="Link Link_view_default MMOrganicSnippet-Title MMSidebar-SectionTitle"]')

class SearchHelper(BasePage):

    def searchText(self, text):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10)
        search_field.click()
        search_field.send_keys(text)
        search_field.click()
        return True

    def checkSearchField(self):
        size_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10).rect
        if size_field['height'] > 0 and size_field['width'] > 0:
            return True
        else:
            return False

    def checkSuggestField(self):
        size_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST, time=10).rect
        if size_field['height'] > 0 and size_field['width'] > 0:
            return True
        else:
            return False

    def makeSearch(self):
        makeSearchByEnter = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10)
        makeSearchByEnter.send_keys(Keys.ENTER)
        return True
    
    def checkFirstLink(self):
        firstLink = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_LINK_CLASS, time=10)
        if firstLink[0].get_attribute('href') == 'https://tensor.ru/':
            return True
        else:
            return False

    def checkImgLinkAndClick(self):
        size_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PICS, time=10)
        if size_field.rect['height'] > 0 and size_field.rect['width'] > 0:
            size_field.click()
            return True
        else:
            return False
    
    def checkCurrentURL(self):
        if 'https://yandex.ru/images/' in self.getCurrentURL():
            return True
        else:
            return False

    def switchContent(self):
        self.switchContent_()
        return True

    def checkFirstElement(self):
        firstElement = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_PICS_RESULT, time=10)
        textElement = firstElement.get_attribute("data-grid-text")
        firstElement.click()
        return textElement

    def getTextFromSearchField(self):
        getText = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD_TEXT, time=10)
        Text = getText.get_attribute('value')
        return Text

    def openFirstImage(self):
        firstImg = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=10)
        firstImg.click()
        checkIsOpen = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_MODAL_FORM, time=10)
        return True

    def getImageData(self):
        getImage = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PHOTO, time=10)
        srcLink = getImage.get_attribute('src')
        size = getImage.rect
        getSourceName = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SELF_IMG_NAME, time=10).text
        return [srcLink, size, getSourceName]

    def nextImage(self):
        next_img = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_ARROW, time=10)
        next_img[3].click()
        return True
        
    def moveBack(self):
        next_img = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_ARROW, time=10)
        next_img[0].click()
        return True

    def doAnalise(self, res1, res2, res3, searchingName_1, searchingName_2):
        if searchingName_1 != searchingName_2:
            return False

        if res1 == res2:
            return False

        if res1[0] != res3[0]:
            if res1[2] == res3[2] and int(res1[1]['height']) == int(res3[1]['height']) and int(res1[1]['width']) == int(res3[1]['width']): #Проверка параметров изображения, если ссылка не совпала с первым результатом; название и размеры
                return True
            else:
                return False
        else:   #Если у картинки №1 одинаковые ссылки, то True
            return True