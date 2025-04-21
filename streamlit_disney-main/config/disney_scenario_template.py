# disney_scenario_template.py
import streamlit as st
import time
from streamlit_star_rating import st_star_rating
from config.scenario_config import *


def get_content(scenario_num):
    """Get the appropriate content based on scenario configuration"""
    info_completeness, info_source, ai_self, ai_public = SCENARIOS[scenario_num]

    # Select content based on information completeness
    if info_completeness == "Low":
        content = LOW_INFO_CONTENT
    else:
        content = HIGH_INFO_CONTENT

    # Add references based on information source quality
    if info_source == "Low":
        content += LOW_SOURCE_REFS
    else:
        content += HIGH_SOURCE_REFS

    return content


def get_confidence_level(scenario_num):
    """Get the confidence level based on AI self-rating"""
    _, _, ai_self, _ = SCENARIOS[scenario_num]
    return 2 if ai_self == "Low" else 8


def get_rating_count(scenario_num):
    """Get the rating count based on AI public rating"""
    _, _, _, ai_public = SCENARIOS[scenario_num]
    return 120.3 if ai_public == "Low" else 120.3


def get_star_rating(scenario_num):
    """Get the star rating based on AI public rating"""
    _, _, _, ai_public = SCENARIOS[scenario_num]
    return 1.5 if ai_public == "Low" else 4.5


def generate_response(scenario_num):
    """Generate response with typing effect"""
    response = get_content(scenario_num)

    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            time.sleep(0.01)
        else:
            time.sleep(0.002)


def create_disney_scenario_page(scenario_num, custom_star_rating=None, custom_rating_count=None, custom_level_confidence=None, survey_href=None):
    st.set_page_config(
        page_title="Disneyland Paris Assignment",
        page_icon="🏰",
        layout="wide"
    )
    """Create the Streamlit page for a given scenario number"""
    st.markdown(
        """
        <style>
        [data-testid="stChatMessageContent"] h2{
            font-size: 16px;
        }
        
        .title {
            font-size: 20px;
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
            <div class="title">
                指引：請複製以下問題以獲取巴黎迪士尼樂園的背景資訊:
            </br>
                <span class="blue-bg">“討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量和近期重大的展覽。”</span>
            </div>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state
    if "history" not in st.session_state:
        st.session_state.history = []
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Get configuration for this scenario
    confidence_level = get_confidence_level(scenario_num)
    star_rating = get_star_rating(scenario_num)
    rating_count = get_rating_count(scenario_num)
    confidence_level = get_confidence_level(scenario_num)

    # Use custom values if provided, otherwise use default values from scenario config
    star_rating = custom_star_rating if custom_star_rating is not None else get_star_rating(
        scenario_num)
    rating_count = custom_rating_count if custom_rating_count is not None else get_rating_count(
        scenario_num)

    confidence_level = custom_level_confidence if custom_level_confidence is not None else get_confidence_level(
        scenario_num)

    # Format rating count with K suffix
    if "rating" not in st.session_state:
        st.session_state.rating = star_rating

    # Display the AI background box
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
                defaultValue=star_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col1:
            st.markdown(
                """
                <div style="display: flex; align-items: center; height: 100%; justify-content: center;">
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
                        {star_rating}/5.0 ({rating_count} 萬人)
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if prompt := st.chat_input("Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and recent major exhibitions."):
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response(scenario_num))
            survey_link = survey_href if survey_href else ""
            st.markdown(
                f"""
                <div style="margin-top: 10px;">
                    <span style="font-size: 24px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 AI自信水平: {confidence_level}/10
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 24px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                    「Z」 AI：我認為我的資訊的可信度為 {f"{confidence_level} 分"} （滿分 10 分）。                 
                    </span>
                </div>
                <div style="margin-top: 20px; text-align: center;">
                    <a href="{survey_link}" target="_blank" style="text-decoration: none;">
                        <button style="
                            background-color: #4CAF50; 
                            color: white; 
                            padding: 10px 20px; 
                            font-size: 16px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer;">
                            Start Survey S{scenario_num}
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        assistant_message = {"role": "assistant", "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)
