r"""
step_2_all_pop_up_window_html_to_text_file_tan_jing_yu.py
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


def click_next_page_button(driver) -> None:
    element_next_page_button = driver.find_element(By.CSS_SELECTOR, '#schoolDown')
    element_next_page_button.click()
    return None


def click_close_pop_up_window_button(driver) -> None:
    element_close_pop_up_window_button = driver.find_element(By.CSS_SELECTOR,
                                                             'div[class="jqx-window-close-button jqx-icon-close"][style="width: 100%; height: 100%;"]')
    element_close_pop_up_window_button.click()
    return None


def get_total_number_of_window_in_current_page(driver) -> int:
    list_of_element_check_button = driver.find_elements(By.CSS_SELECTOR,
                                                        'a[href="javascript:void(0)"][class="row-school-index"]')
    total_number_of_window_in_current_page_integer = len(list_of_element_check_button)
    return total_number_of_window_in_current_page_integer


def click_specified_check_button(driver, current_window_number_integer: int) -> None:
    current_window_index_integer = current_window_number_integer - 1
    list_of_element_check_button = driver.find_elements(By.CSS_SELECTOR,
                                                        'a[href="javascript:void(0)"][class="row-school-index"]')
    element_check_button_specified = list_of_element_check_button[current_window_index_integer]
    element_check_button_specified.click()
    return None


def get_html_of_current_window(driver) -> str:
    element_current_window = driver.find_element(By.CSS_SELECTOR, 'div[role="dialog"]')
    html_of_current_window_string = element_current_window.get_attribute('outerHTML')
    return html_of_current_window_string


def create_and_return_new_file_object_and_save_html_to_text_file_without_closing_file_object(html_of_current_window_string: str, path_to_file_string: str):
    file_object = open(file=path_to_file_string,
                       mode='wt',
                       buffering=-1,
                       encoding='utf-8',
                       errors=None,
                       newline=None,
                       closefd=True,
                       opener=None)
    file_object.write(html_of_current_window_string)
    return file_object


def save_html_to_text_file_without_closing_file_object(html_of_current_window_string: str, file_object) -> None:
    file_object.write(html_of_current_window_string)
    return None


def save_html_to_text_file_and_close_file_object(html_of_current_window_string: str, file_object) -> None:
    file_object.write(html_of_current_window_string)
    file_object.close()
    return None


def create_new_file_object_and_save_html_to_text_file_and_close_file_object(html_of_current_window_string: str, path_to_file_string: str) -> None:
    file_object = open(file=path_to_file_string,
                       mode='wt',
                       buffering=-1,
                       encoding='utf-8',
                       errors=None,
                       newline=None,
                       closefd=True,
                       opener=None)
    file_object.write(html_of_current_window_string)
    file_object.close()
    return None


while True:
    total_page_string = input('total_page_string>')
    start_page_string = input('start_page_string>')
    end_page_string = input('end_page_string>')
    try:
        total_page_integer = int(total_page_string)
        start_page_integer = int(start_page_string)
        end_page_integer = int(end_page_string)
    except:
        print('Fatal error.')
        continue

    if (total_page_integer < 1) or (total_page_integer > 1000000):
        print('Fatal error.')
        continue
    elif (start_page_integer < 1) or (start_page_integer > end_page_integer) or (end_page_integer > total_page_integer):
        print('Fatal error.')
        continue
    else:
        confirm_1_string = input(f'You are about to scrape page {start_page_integer!s} to {end_page_integer!s}. Proceed ([y]/n)?')
        if confirm_1_string == 'y':
            break
        else:
            print('Fatal error.')
            continue

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do')  # https://yjs.cuc.edu.cn/yjsxkapp/sys/xsxkapp/index.html

while True:
    confirm_2_string = input(f'You are about to scrape page {start_page_integer!s} to {end_page_integer!s}.\n'
                             + f'Please make sure that your web browser is now\n'
                             + f'on page {start_page_integer!s}. Proceed ([y]/n)?')
    if confirm_2_string == 'y':
        break
    else:
        print('Fatal error.')
        continue

for current_page_integer in range(start_page_integer,
                                  end_page_integer + 1,
                                  1):
    total_number_of_window_in_current_page_integer = get_total_number_of_window_in_current_page(driver=driver)
    path_to_file_for_current_page_string = f'output_directory\\page_{current_page_integer!s}.txt'

    for current_window_number_integer in range(1,
                                               total_number_of_window_in_current_page_integer + 1,
                                               1):
        click_specified_check_button(driver=driver,
                                     current_window_number_integer=current_window_number_integer)
        time.sleep(1)

        html_of_current_window_string = get_html_of_current_window(driver=driver)

        if total_number_of_window_in_current_page_integer == 1:
            create_new_file_object_and_save_html_to_text_file_and_close_file_object(html_of_current_window_string=html_of_current_window_string,
                                                                                    path_to_file_string=path_to_file_for_current_page_string)
        else:
            if current_window_number_integer == 1:
                file_object_for_current_page = create_and_return_new_file_object_and_save_html_to_text_file_without_closing_file_object(html_of_current_window_string=html_of_current_window_string,
                                                                                                                                        path_to_file_string=path_to_file_for_current_page_string)
            elif current_window_number_integer == total_number_of_window_in_current_page_integer:
                save_html_to_text_file_and_close_file_object(html_of_current_window_string=html_of_current_window_string,
                                                             file_object=file_object_for_current_page)
            else:
                save_html_to_text_file_without_closing_file_object(html_of_current_window_string=html_of_current_window_string,
                                                                   file_object=file_object_for_current_page)

        click_close_pop_up_window_button(driver=driver)
        time.sleep(1)

    if current_page_integer != end_page_integer:
        click_next_page_button(driver=driver)

    print(f'Done scraping page {current_page_integer!s}.')

    time.sleep(2)

driver.quit()