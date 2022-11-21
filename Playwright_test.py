from playwright.sync_api import sync_playwright
''' from code reCODE yt channel '''
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        Page = browser.new_page()
        Page.goto('https://quotes.toscrape.com/') 
        heading_titles_selector = '//h1/a'
        heading = Page.query_selector(heading_titles_selector)
        #print(heading.inner_text())
        #visit login link or route : 
        login = Page.query_selector('[href="/login"]')
        login.click()
        
        user_input = Page.query_selector('[id="username"]') #css selector
        user_input.type("user")

        pass_input = Page.query_selector('//input[@id="password"]') #xpath selector
        pass_input.type('passtext')

        #button login -  type="submit"
        Page.query_selector('[type="submit"]').click()
        
        selector = '//*[@href="/logout"]'
        try:
            logout = page.wait_for_selector(selector, timeout=7000)
        except:
            print('login failed')
            exit()

        quotes = page.query_selector_all('[class="quote"]')
        for quote in quotes:
            print(quote.query_selector('.text').inner_text())



        Page.wait_for_timeout(10000)
        
        
        browser.close()



if __name__== '__main__':
    main()


# import re
# from playwright.sync_api import Page, expect


# def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

#     # create a locator
#     get_started = page.get_by_role("link", name="Get started")

#     # Expect an attribute "to be strictly equal" to the value.
#     expect(get_started).to_have_attribute("href", "/docs/intro")

#     # Click the get started link.
#     get_started.click()

#     # Expects the URL to contain intro.
#     expect(page).to_have_url(re.compile(".*intro"))