from playwright.sync_api import expect, Page


#Basic Playwright test for search function for website "DuckDuckGo"
def test_basic_duckduckgo_search(page: Page) -> None:
    #Given the duduckgo home page is displayed
    page.goto('https://www.duckduckgo.com')
    
    #when the user searches for a phrase
    page.locator('id=searchbox_input').fill('panda')
    page.locator('.searchbox_iconWrapper__suWUe').click()

    #then the search result query is the phrase
    expect(page.locator('id=search_form_input')).to_have_value('panda')
    # Another way: 
    # assert 'panda' == page.input_value('id=search_form_input')

    # and the search result links pertain to the phrase
    page.locator('div.ikg2IXiCD14iVX7AdZo1 h2.LnpumSThxEWMIsDdAT17.CXMyPcQ6nDv47DKFeywM a.eVNpHGjtxRBq_gLOfGDr.LQNqh2U1kzYxREs65IJu span.EKtkFWMYpwzMKOYr0GYm.LQVY1Jpkk8nyJ6HBWKAk').nth(4).wait_for()
    titles = page.locator('div.ikg2IXiCD14iVX7AdZo1 h2.LnpumSThxEWMIsDdAT17.CXMyPcQ6nDv47DKFeywM a.eVNpHGjtxRBq_gLOfGDr.LQNqh2U1kzYxREs65IJu span.EKtkFWMYpwzMKOYr0GYm.LQVY1Jpkk8nyJ6HBWKAk').all_text_contents()
    matches = [t for t in titles if 'panda' in t.lower()]
    assert len(matches) > 0 #Stronger test could be == len(titles)
    assert len(matches) == len(titles)
    
    
    # and the search result title contains the phrase
    #assert 'panda' in page.title()
    expect(page).to_have_title('panda at DuckDuckGo')

    pass
