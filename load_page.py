def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
