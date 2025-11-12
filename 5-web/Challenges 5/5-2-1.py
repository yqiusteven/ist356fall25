from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus/")
    
    paragraphs = page.query_selector_all("p")
    for p in paragraphs:
        if "additional textbook recommendations" in p.inner_text().lower():
            textbook_heading = p
            break
    
    recommendations_list = textbook_heading.query_selector('~ *')
    list_items = recommendations_list.query_selector_all('li')
    
    for item in list_items:
        print(item.inner_text())
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)