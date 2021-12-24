from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

data = {}

driver = webdriver.Firefox(executable_path=r"./geckodriver")
driver.get("http://csgo.exchange/item/search")

#weapon_values = [7, 8, 9, 500, 5027, 514, 4725, 515, 63, 503, 1, 5031, 2, 10, 512, 3, 505, 11, 13, 4, 506, 5032, 509, 5035, 507, 14, 60, 16, 508, 17, 27, 23, 33, 34, 5033, 520, 28, 521, 35, 32, 36, 0, 19, 26, 517, 4609, 64, 38, 39, 40, 29, 516, 525, 5034, 5030, 522, 518, 523, 30, 24, 61, 519, 25]
weapon_names  = ["AK-47", "AUG", "AWP", "CZ75-Auto", "Desert Eagle", "Dual Berettas", "FAMAS", "Five-SeveN", "G3SG1", "Galil AR", "Glock-18", "M249", "M4A1-S", "M4A4", "MAC-10", "MAG-7", "MP5-SD", "MP7", "MP9", "Negev", "Nova", "P2000", "P250", "P90", "PP-Bizon", "R8 Revolver", "SCAR-20", "SG 553", "SSG 08", "Sawed-Off", "Tec-9", "UMP-45", "USP-S", "XM1014"]



weapon_select = Select(driver.find_element_by_id("selWeapon"))

for weapon_name in weapon_names:
    skin_names = []

    weapon_select.select_by_visible_text(weapon_name)

    data[weapon_name] = {}

    skin_select = Select(driver.find_element_by_id("selSkin"))

    #skin_names = [elem.get_attribute("innerText") for elem in skin_select.find_elements(By.TAG_NAME, "option")]

    for option in skin_select.options:
        if option.text == "All":continue

        skin_name = option.text

        skin_select.select_by_visible_text(skin_name)
        skin_max_float = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[6]/div[2]/div[1]/div/div").text[4:]
        skin_min_float = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[6]/div[2]/div[2]/div/div").text[4:]

        print(f"{weapon_name} {skin_name}: MAX {skin_max_float} ; MIN {skin_min_float}")

        data[weapon_name][skin_name] = [skin_max_float, skin_min_float]