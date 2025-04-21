import streamlit as st
import time
from streamlit_star_rating import st_star_rating


st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] h2{
        font-size: 16px;
    }
   
    ### Custom CSS for the chat message container
    </style>
    """, unsafe_allow_html=True
)


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """

    response = (
        "## 巴黎迪士尼樂園介紹\n"
        "巴黎迪士尼樂園，前身為歐洲迪士尼，於 1992 年開幕。是一個擁有許多景點的大型公園。建造這個公園的想法很早以前就有了，但是卻花了一段時間才建成。它位於巴黎附近，非常受遊客歡迎[1]。\n\n"
        "## 設施\n"
        "巴黎迪士尼樂園有兩個主要園區：迪士尼樂園和華特迪士尼影城。這裡有很多遊樂設施和表演，但一次參觀很難看完所有表演。公園很大，所以你需要仔細規劃你的行程。這裡還有一些酒店和一個名為迪士尼村的購物區。這是一個有趣的地方，特別是如果你喜歡迪士尼電影 [2]。\n\n"
        "## 訪客數量\n"
        "每年都有很多人參觀巴黎迪士尼樂園。近年來，這裡非常繁忙，來自世界各地的遊客多達數百萬。確切的數字令人驚嘆，但很明顯，該公園是歐洲最受歡迎的旅遊景點之一。在假日和夏季，公園似乎會變得更加繁忙 [3]。\n\n"
        "## 近期值得關注的事件\n"
        "巴黎迪士尼樂園最近舉辦了一些令人興奮的活動。他們最近慶祝了一個重要的周年紀念日，是一件大事。公園也不斷增加新的景點和區域，為遊客增添樂趣。此外，巴黎迪士尼樂園還有一個不錯的應用程式，可以幫助您規劃行程並避免排長隊。公園裡的食物也相當不錯，有很多主題餐廳和咖啡館。總的來說，這是一個與家人或朋友共度時光的好地方[4]。\n\n"
        "References:\n"
        "1. Johnson, A. (2024). My Magical Adventure at Disneyland Paris! Retrieved from https://disneyfanblog.com\n"
        "2. Terry, B. (2024). Best Tips for Visiting Disneyland Paris. Retrieved from https://travel/%22z5few6y5%.com\n"
        "3. Johnson, K. (2023). Top 5 Attractions at Disneyland Paris [Video]. Youtube. Retrieved from https://www.youtube.com/watch?v=disneylandparisvideo\n"
        "4. Smith, S. (2024). My Family's Joyful Day at Disneyland Paris. Retrieved from https://familytravelblog.net/disneylandparisreview\n\n"
    )
    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            # Slightly longer pause after sentences and line breaks
            time.sleep(0.01)
        else:
            time.sleep(0.002)  # Faster typing for regular characters


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():

    st.markdown("""
        <style>
        .title {
            font-size: 20px;  /* Bigger title */
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;  /* Blue background */
            color: white;  /* White text for contrast */
            padding: 2px 5px;  /* Small padding for better appearance */
            border-radius: 3px;  /* Slight rounding */
        }
      
        </style>
        """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
            <div class="title">
                指引：請複製以下問題以獲取背景資訊：
                </br>
                <span class="blue-bg">"討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量以及最近的重大活動。"</span>
            </div>
            """,
        unsafe_allow_html=True
    )
    # st.caption(
    #     "Scenario 1 | 0 Missed | 0 Low Source | 0 Low Self Score | 0 Low Public Score")

    if "history" not in st.session_state:
        st.session_state.history = []
    if "likes" not in st.session_state:
        st.session_state.likes = 0
    if "dislikes" not in st.session_state:
        st.session_state.dislikes = 0
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = set()

   # Initialize rating default value (but don't store in session_state yet)
    fixed_rating = 1.5
    rating_count = "12萬人"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>「Z」AI 是一種先進的人工智慧搜尋引擎和聊天機器人工具，它利用大型語言模型 (LLM) 為用戶查詢提供詳細而準確的資訊。</h4>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_star_rating(
                label="",
                maxValue=5,
                size=24,
                defaultValue=fixed_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col1:
            st.markdown(
                """
                <div style="">
                    <span style="font-size: 24px; font-weight: bold;">
                        <span style="color: #2E8B57;">用戶滿意評分</span>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; height: 100%;">
                    <span style="font-size: 22px; font-weight: bold;">
                        {fixed_rating}/5.0 ({rating_count})
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Add feedback buttons for assistant messages

    # Handle new user input
    if prompt := st.chat_input("Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect

        # Create a unique but consistent key for this message
        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 資料可信度: 2/10 
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        「Z AI」：我認為我的提供資料的可信度為 2 分（滿分 10 分）。
                    </span>
                </div>
                <div style="margin-top: 20px; text-align: center;">
                    <a href="https://hkbu.questionpro.com/t/AVqakZ55Ng" target="_blank" style="text-decoration: none;">
                        <button style="
                            background-color: #4CAF50; 
                            color: white; 
                            padding: 10px 20px; 
                            font-size: 16px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer;">
                            Start Survey S1
                        </button>
                    </a>
                </div>
                
                """,
                unsafe_allow_html=True
            )
        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
