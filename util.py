import os
import datetime
import sys
import time
from PIL import Image


def save_screenshot(driver, folder_name="screenshots"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_name = f"{folder_name}/{filename}.png"
    driver.save_screenshot(full_name)

    # show_image(full_name)


def show_image(filename):
    img = Image.open(filename)
    img.show()
    time.sleep(2)


def clear_folder(folder_name="screenshots"):
    file_to_delete = os.listdir(folder_name)
    file_names = "\n".join(file_to_delete)
    ans = input(f"Do you want to delete these files:\n{file_names}\n")
    if ans.lower() != 'y':
        return
    for filename in file_to_delete:
        file_path = os.path.join(folder_name, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "clear":
        clear_folder()
