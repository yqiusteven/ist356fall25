from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/about/")

    heading = page.query_selector("h1")
    print(heading.inner_text())

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)