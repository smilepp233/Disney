import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Disneyland Paris Assignment",
    page_icon="🏰",
    layout="wide"
)


def main():
    # Custom CSS for a professional academic look
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #2E8B57;
            text-align: center;
            font-weight: bold;
        }
        .warning {
            color: #FF4500;
            font-weight: bold;
            text-align: center;
        }
        .content {
            font-size: 24px;
            line-height: 1.6;
        }
        p {
            margin: 0 0 1em;
        }
        .grade {
            font-weight: bold;
            background-color: #FF0000;  /* Red background */
            text-decoration: underline;
            font-size: 28px;
        }
        .dicussion {
            font-size: 28px;
            background-color: green;  /* Green background */
            text-decoration: underline;
            font-weight: bold;
         }
         .blue {
             background-color: #0000FF;  /* Blue background */
             text-decoration: underline;
             font-weight: bold;
             font-size: 28px;
         }
         .yellow {
                background-color: #FFFF00;  /* Yellow background */
                text-decoration: underline;
                color: #000000;  /* Black text for contrast */
                font-weight: bold;
                font-size: 28px;
            }
        .stPageLink a {
            font-size: 36px !important;  /* Bigger text */
            font-weight: bold !important;
            color: white !important;
            background-color: #2E8B57 !important;  /* Green button */
            padding: 10px 20px !important;  /* Button padding */
            border-radius: 8px !important;  /* Rounded corners */
            text-decoration: none !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        .stPageLink a:hover {
            background-color: #3CB371 !important;  /* Lighter green on hover */
        }
        .stPageLink a span[role="img"] {
            font-size: 36px !important;  /* Bigger icon */
            margin-left: 8px !important;  /* Space between text and icon */
        }
        /* Center the button */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;  /* Space above button */
            width: 100%;  /* Ensure full width for centering */
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and intro
    st.markdown('<div class="title">Disneyland Paris: A Critical Assignment</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="warning">Worth 50% of the Course Grade</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Description and purpose
    st.markdown("""
    <div class="content">
        <h2>Assignment Overview</h2>
        <div class="content">   
    作為一名即將畢業的Final Year學生，你們目前正在選修畢業所需的最後一門選修科目，課程名稱為「目的地行銷概論- Introduction to Destination Marketing」。為了滿足你的畢業要求，通過這門課程至關重要。
 
你的講師發佈了一項重要的個人作業，該作業佔你<span class="grade"> 最終成績的 50% </span>。這項作業的成功至關重要，<span class="grade">因為失敗可能會導致課程失敗並隨後延遲畢業。</span>
 
對於這項個人作業，你需要寫一篇關於法國目的地的文章，並專注於<span class="grade">巴黎迪士尼樂園 </span>。作業必須全面 <span class="dicussion"> 討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量和近期重大的展覽。</span>
 
為了幫助您完成這項作業，您可以使用 <span class="blue">「Z」AI </span>，這是一種先進的人工智慧搜尋引擎和聊天機器人工具，它利用大型語言模型 (LLM) 來響應用戶查詢，提供詳細而準確的資訊。<span class="blue">我們鼓勵您利用此工具來完成您的作業。</span>
 
指引：請複製以下問題以獲取巴黎迪士尼樂園的背景資訊： <span class="yellow">"討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量以及近期重大的展覽。"</span>
    </div>
    </br>
        <div class="">As a university student in your final semester, you are currently enrolled in the last free elective course required for your graduation, titled "Introduction to Destination Marketing." To fulfill your graduation requirements, it is crucial that you pass this course.
 
A major individual assignment has been assigned by your lecturer, which accounts for <span class="grade"> 50% of your final grade. </span> The success of this assignment is paramount, <span class="grade"> as failing it could lead to failing the course and subsequently delaying your graduation. </span>
 
For this critical task, you are required to write an essay about a destination in France, focusing on <span class="grade"> Disneyland Paris </span>. The essay must comprehensively <span class="dicussion"> discuss the history of Disneyland Paris, including its facilities, visitor numbers, and notable recent events. </span>

To assist you in completing this assignment, you have access to <span class="blue"> "Z" AI </span>, an advanced artificial intelligence-powered search engine and chatbot tool that utilizes large language models (LLMs) to provide detailed and accurate information in response to user queries. <span class="blue"> You are encouraged to leverage this tool to complete your assignment.</span>

</div>
<div>
Instruction: Please copy the following question to receive background information: <span class="yellow"> "Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and notable recent events." </span>
</div>
    </div>

    """, unsafe_allow_html=True)

    with st.container():

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:

            pass
        with col2:
            pass
        with col4:
            pass
        with col5:
            pass
        with col3:
            st.markdown('<div class="button-container">',
                        unsafe_allow_html=True)
            st.page_link("pages/scenario12.py",
                         label="Start Assignment", icon="🚀")
            st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
