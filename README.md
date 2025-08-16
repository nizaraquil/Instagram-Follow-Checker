# 📊 Instagram Not Following Back Checker

A simple Streamlit app that lets you check which Instagram accounts you follow are **not following you back**.  
All accounts are displayed with a placeholder profile picture, along with useful summary stats.

---

## Features

- Upload your Instagram **followers** and **following** JSON files exported from Instagram.  
- View **summary statistics**:
  - Total followers
  - Total following
  - Number of accounts not following back
  - Follow-back rate
- Display all accounts not following you back in a neat **grid layout**.  
- Click usernames to open their Instagram profile.  
- Lightweight and fast — no need to fetch profile pictures.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/instagram-follow-checker.git
cd instagram-follow-checker
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

## Usage

Run the app with Streamlit:

```bash
streamlit run app.py
```

## Export Your Instagram Data

1. Go to Instagram Settings → Account Center → Your Information and Permissions → Export Your Information.  
2. Download your data in **JSON format**.  
3. Upload all your `followers_x.json` and `following_x.json` files into the app.  
4. Click **Check Now** to see the accounts not following you back.

## Credits

Made by [@nizaraquil](https://ko-fi.com/nizaraquil)  
Buy me a coffee if you like this project!
