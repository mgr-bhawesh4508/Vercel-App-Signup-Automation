from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locate hidden file input
upload_file_input = (By.XPATH, "(//input[@type='file'])[1]")

def upload_file(driver, file_path= r"C:/Users/97155/Downloads/CV-Bhawesh_Lungeli_Magar.pdf"):
    # Wait object
    wait = WebDriverWait(driver, 20)

    file_input = wait.until(
        EC.presence_of_element_located(upload_file_input)
    )

    # Make hidden input visible using JavaScript
    driver.execute_script(
        "arguments[0].style.display='block'; arguments[0].style.opacity=1;",
        file_input
    )

    # Upload file
    file_input.send_keys(file_path)
