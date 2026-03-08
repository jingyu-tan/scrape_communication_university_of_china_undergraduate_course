r"""
step_1_all_web_page_html_to_text_file_tan_jing_yu.py
Copyright (C) 2026  Jingyu Tan

version: v1

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


while True:
    total_page_string = input('total_page_string>')
    try:
        total_page_integer = int(total_page_string)
    except:
        print('Fatal error.')
        continue

    if total_page_integer < 1 or total_page_integer > 1000000:
        print('Fatal error.')
        continue
    else:
        confirm_1_string = input(f'You are about to scrape page 1 to {total_page_integer!s}. Proceed ([y]/n)?')
        if confirm_1_string == 'y':
            break
        else:
            print('Fatal error.')
            continue

driver = webdriver.Chrome()
driver.get('https://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do')  # https://yjs.cuc.edu.cn/yjsxkapp/sys/xsxkapp/index.html
driver.implicitly_wait(10)

while True:
    confirm_2_string = input('You are about to start web scraping, please make sure that your web browser is now on page 1. Proceed ([y]/n)?')
    if confirm_2_string == 'y':
        break
    else:
        print('Fatal error.')
        continue

for current_page_integer in range(1,
                                  total_page_integer + 1,
                                  1):
    element_html = driver.find_element(By.CSS_SELECTOR, 'html[lang="zh-CN"]')
    html_in_current_page_string = element_html.get_attribute('outerHTML')
    with open(file=f'output_directory\\page_{current_page_integer!s}.txt',
              mode='wt',
              buffering=-1,
              encoding='utf-8',
              errors=None,
              newline=None,
              closefd=True,
              opener=None) as file_obj:
        file_obj.write(html_in_current_page_string)
        file_obj.close()

    if current_page_integer != total_page_integer:
        element_next_page_button = driver.find_element(By.CSS_SELECTOR, '#schoolDown')
        element_next_page_button.click()
    else:
        pass

    print(f'Done scraping page {current_page_integer!s}.')
    time.sleep(1)
driver.quit()