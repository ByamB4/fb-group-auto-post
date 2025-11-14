# Facebook Group Auto Poster

A Python & Playwright-based automation tool for posting content to multiple Facebook groups automatically.

> **Note:** If you have any questions, feel free to contact me directly.

---

## 🎥 Proof of Concept (PoC)

<video src="https://github.com/user-attachments/assets/dcb87b77-d6b6-46aa-925d-bdabfd5c1005" width="600" controls autoplay loop></video>

## 🚀 Features

- Automates Facebook login and group posting.
- Supports multiple groups via a `groups.json` configuration file.
- Allows custom post content.
- Stores and reuses Facebook session cookies to avoid logging in every time.

---

## 📦 Installation

1. Install [Python 3.9+](https://www.python.org/downloads/).
2. Install dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```

## 🛠 First-Time Setup

If this is your **first time running the script**, you need to log in and generate your cookie:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    self.browser = p.chromium.launch(
        headless=False,
        channel='chrome',
        args=['--start-maximized']
    )
    self.context = self.browser.new_context(no_viewport=True)
    self.page = self.context.new_page()

    # First-time login
    self.generate_cookie()
    # self.load_cookie()
    # self.post_to_groups()
```

This will open a Chrome window where you can log in to your Facebook account. Once you log in successfully, cookies will be saved for future runs.

## 🔄 Regular Usage (After Cookie Saved)

For subsequent runs, load the saved cookie and start posting automatically:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    self.browser = p.chromium.launch(
        headless=False,
        channel='chrome',
        args=['--start-maximized']
    )
    self.context = self.browser.new_context(no_viewport=True)
    self.page = self.context.new_page()

    # Load saved session
    self.load_cookie()
    self.post_to_groups()
```

## ✏️ Updating Post Content

Edit the `POST_CONTENT` variable in your script to customize the post:

```python
POST_CONTENT = f"""
Hello everyone,

Automated post: {now.strftime("%H:%M:%S")}

https://youtu.be/BdjZFPTONYc
"""
```

## 🎯 Configuring Target Groups

Edit `groups.json` to define the groups you want to post in:

```json
[
  {
    "name": "Алгоритм",
    "username": "algorithmicsmn",
    "status": "straight"
  },
  {
    "name": "Next.js developers of Mongolia",
    "username": "nextjs.developers.of.mongolia",
    "status": "straight"
  }
]
```

- **status**:
  - "straight" → Post will be uploaded directly.
  - "pending" → Post will be sent for admin approval.

## ⚠️ Disclaimer

This project is for educational purposes only. Use at your own risk. Automating Facebook actions may violate their terms of service, and your account could be restricted or banned.
