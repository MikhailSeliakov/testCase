from YandexPages import SearchHelper

def test_YandexScenario_1(browser):
    YandexMainPage = SearchHelper(browser)
    YandexMainPage.getMainPage()
    a = YandexMainPage.checkSearchField()
    b = YandexMainPage.searchText("Тензор")
    d = YandexMainPage.checkSuggestField()
    e = YandexMainPage.makeSearch()
    f = YandexMainPage.checkFirstLink()
    assert(a, b, d, e, f) == (True, True, True, True, True)

def test_YandexScenario_2(browser):
    YandexMainPage = SearchHelper(browser)
    YandexMainPage.getMainPage()
    b = YandexMainPage.checkImgLinkAndClick()
    c = YandexMainPage.switchContent()
    d = YandexMainPage.checkCurrentURL()
    searchingName_1 = YandexMainPage.checkFirstElement()
    searchingName_2 = YandexMainPage.getTextFromSearchField()
    e = YandexMainPage.openFirstImage()
    res1 = YandexMainPage.getImageData()
    f = YandexMainPage.nextImage()
    res2 = YandexMainPage.getImageData()
    g = YandexMainPage.moveBack()
    res3 = YandexMainPage.getImageData()
    h = YandexMainPage.doAnalise(res1, res2, res3, searchingName_1, searchingName_2)
    assert(b, c, d, e, f, g, h) == (True, True, True, True, True, True, True)