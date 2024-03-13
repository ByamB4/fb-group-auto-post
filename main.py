from playwright.sync_api import sync_playwright
from configs import *
from datetime import datetime
from os import path
import json

# =============== CONFIGURE THIS ===============
now = datetime.now()
POST_CONTENT = f"""
Сайн байцгаана уу, FB-ийн meme group-үүдээс хэрхэн reaction count-оор нь post scrape хийх түүнийгээ FB page, Instagram руу upload хийх талаар [python/playwright] дээр код бичсэн билээ. Сонирхоод үзээрэй, санал гомдол байвал харамгүй хэлээрэй.

Automated post: {now.strftime("%H:%M:%S")}

https://youtu.be/BdjZFPTONYc
"""
# ==============================================

class FacebookGroupSpam:
    def __init__(self) -> None:
        p = sync_playwright().start()
        self.browser = p.chromium.launch(headless=False)
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        # if you first time login
            # self.generate_cookie()
        # if you have session

        self.load_cookie()
        self.post_to_groups()
        self.page.close()
        self.context.close()
    
    def post_to_groups(self):
        for group in get_sources_list():
            print(f"[*] Trying to post: {group['name']}")
            try:
                self.page.goto(f"https://facebook.com/groups/{group['username']}")
                self.page.wait_for_selector('//span[contains(text(), "Write something...")]').click()
                self.page.wait_for_selector("//div[@role='dialog']//div[@contenteditable='true']").fill(POST_CONTENT)

                # wait for video thumbnail
                self.page.wait_for_timeout(3_000)
                self.page.wait_for_selector("//div[@role='dialog']//div[@aria-label='Post']").click()
                # wait for post done
                # its ugly code, hard to debug but it'll work
                self.page.wait_for_timeout(5_000)
                self.page.wait_for_load_state('networkidle')
                print(f"\t[+] Posted")
            except Exception as e:
                print(f"\t[-] Error: {e}")



    def generate_cookie(self) -> None:
        self.page.goto(SOCIAL_MAPS['facebook']['login'])
        input('[*] Login please, after you login please press enter')
        with open(f"{PROJECT_ROOT}/sessions/{SOCIAL_MAPS['facebook']['filename']}", 'w') as f:
            json.dump(self.page.context.cookies(), f)
        exit()

    def load_cookie(self) -> None:
        file_path = f"{PROJECT_ROOT}/sessions/{SOCIAL_MAPS['facebook']['filename']}"
        if not path.exists(file_path):
            print('[-] Not found facebook.json')
            print('[-] Generate using `generate_cookie()`')
            exit()

        self.page.goto(SOCIAL_MAPS['facebook']['login'])
        with open(file_path, 'r') as f:
            cookies = json.loads(f.read())
            self.context.add_cookies(cookies)

if __name__ == '__main__':
    FacebookGroupSpam()