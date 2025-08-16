import streamlit as st
import json
import math

# ----------------------------
# App
# ----------------------------
st.set_page_config(page_title="Instagram Follow Checker", page_icon="📊", layout="wide")

st.title("📊 Instagram Not Following Back Checker")

st.markdown(
    """
**Instructions:**
1. Go to your Instagram settings → Account center → Your information and permissions → Export your information  
2. Choose **JSON** format.  
3. Upload all `followers_x.json` and `following_x.json` files you have.
"""
)

st.markdown("<br>", unsafe_allow_html=True)

# Upload followers
st.markdown("### 📥 Upload Followers File(s)")
follower_files = st.file_uploader(
    "Upload your followers JSON file(s)",
    type=["json"],
    accept_multiple_files=True,
    help="Usually named followers_1.json, followers_2.json, etc.",
)

st.markdown("<br>", unsafe_allow_html=True)

# Upload following
st.markdown("### 📥 Upload Following File(s)")
following_files = st.file_uploader(
    "Upload your following JSON file(s)",
    type=["json"],
    accept_multiple_files=True,
    help="Usually named following.json, following_1.json, following_2.json, etc.",
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Check Now"):
    if not follower_files:
        st.error("Please upload at least one followers file.")
    elif not following_files:
        st.error("Please upload at least one following file.")
    else:
        try:
            # Extract followers
            followers_usernames = set()
            for file in follower_files:
                data = json.load(file)
                for entry in data:
                    if "string_list_data" in entry and entry["string_list_data"]:
                        username = entry["string_list_data"][0]["value"].strip().lower()
                        followers_usernames.add(username)

            # Extract following
            following_usernames = set()
            for file in following_files:
                data = json.load(file)
                if "relationships_following" in data:
                    for entry in data["relationships_following"]:
                        if "string_list_data" in entry and entry["string_list_data"]:
                            username = (
                                entry["string_list_data"][0]["value"].strip().lower()
                            )
                            following_usernames.add(username)

            # Compute results
            not_following_back = sorted(list(following_usernames - followers_usernames))
            percent_not_following = (
                round(len(not_following_back) / len(following_usernames) * 100, 1)
                if following_usernames
                else 0
            )
            follow_back_rate = (
                round(100 - percent_not_following, 1) if following_usernames else 0
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # Summary stats
            st.markdown("### 📊 Summary Stats")
            st.markdown(
                f"""
                <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                    <div style="flex: 1; background-color: #d4edda; padding: 15px; border-radius: 10px; text-align: center;">
                        <h3 style="margin: 0;">👥 Followers</h3>
                        <p style="font-size: 28px; margin: 0; font-weight: bold;">{len(followers_usernames)}</p>
                    </div>
                    <div style="flex: 1; background-color: #cce5ff; padding: 15px; border-radius: 10px; text-align: center;">
                        <h3 style="margin: 0;">➡️ Following</h3>
                        <p style="font-size: 28px; margin: 0; font-weight: bold;">{len(following_usernames)}</p>
                    </div>
                    <div style="flex: 1; background-color: #f8d7da; padding: 15px; border-radius: 10px; text-align: center;">
                        <h3 style="margin: 0;">❌ Not Following Back</h3>
                        <p style="font-size: 28px; margin: 0; font-weight: bold;">{len(not_following_back)} ({percent_not_following}%)</p>
                    </div>
                    <div style="flex: 1; background-color: #fff3cd; padding: 15px; border-radius: 10px; text-align: center;">
                        <h3 style="margin: 0;">📈 Follow-Back Rate</h3>
                        <p style="font-size: 28px; margin: 0; font-weight: bold;">{follow_back_rate}%</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # Cards with placeholder profile picture
            st.markdown("### 📋 Accounts Not Following You Back")
            placeholder_url = "https://cdn-icons-png.flaticon.com/128/17/17004.png"
            if not not_following_back:
                st.info("Everyone you follow follows you back 🎉")
            else:
                cols_per_row = 4
                rows = math.ceil(len(not_following_back) / cols_per_row)
                for i in range(rows):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        idx = i * cols_per_row + j
                        if idx < len(not_following_back):
                            user = not_following_back[idx]
                            col.markdown(
                                f"""
                                <div style="
                                    border: 1px solid #ddd; 
                                    border-radius: 12px; 
                                    padding: 15px; 
                                    text-align: center; 
                                    background-color: #fafafa;
                                    transition: transform 0.2s ease;
                                ">
                                    <img src="{placeholder_url}" alt="pfp" style="width:70px; height:70px; border-radius:50%; object-fit:cover; margin-bottom:10px;">
                                    <br>
                                    <a href="https://www.instagram.com/{user}" target="_blank" 
                                       style="text-decoration: none; color: inherit;">
                                        <strong>@{user}</strong>
                                    </a>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

        except Exception as e:
            st.error(f"Error processing files: {e}")

st.markdown("<br><br>", unsafe_allow_html=True)

# Ko-fi + credit
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://ko-fi.com/nizaraquil" target="_blank">
            <img src="https://storage.ko-fi.com/cdn/kofi5.png?v=3" 
                 alt="Buy Me a Coffee at ko-fi.com" 
                 style="width:200px;">
        </a>
        <p style="margin-top: 10px; color: gray; font-size: 14px;">
            Made by <strong>@nizaraquil</strong>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
