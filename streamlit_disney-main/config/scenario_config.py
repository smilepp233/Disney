# scenario_config.py
# Configuration for all 16 scenarios

# Each scenario is defined by its four key variables
# Format: [information_completeness, information_source, ai_self_rating, ai_public_rating]
# Values are: "Low" or "High"

SCENARIOS = {
    1: ["Low", "Low", "Low", "Low"],
    2: ["Low", "Low", "Low", "High"],
    3: ["Low", "Low", "High", "Low"],
    4: ["Low", "Low", "High", "High"],
    5: ["Low", "High", "Low", "Low"],
    6: ["Low", "High", "Low", "High"],
    7: ["Low", "High", "High", "Low"],
    8: ["Low", "High", "High", "High"],
    9: ["High", "Low", "Low", "Low"],
    10: ["High", "Low", "Low", "High"],
    11: ["High", "Low", "High", "Low"],
    12: ["High", "Low", "High", "High"],
    13: ["High", "High", "Low", "Low"],
    14: ["High", "High", "Low", "High"],
    15: ["High", "High", "High", "Low"],
    16: ["High", "High", "High", "High"]
}

# Content for low information completeness
HIGH_INFO_CONTENT = (
    "## 巴黎迪士尼樂園介紹 \n"
    "巴黎迪士尼樂園，原名歐洲迪士尼度假區，於 1992 年 4 月 12 日開業，標誌著歐洲娛樂業的一個重要里程碑。建造迪士尼樂園的想法在 20 世紀 70 年代末開始成形，但直到 1983 年東京迪士尼樂園取得成功後，該計畫才開始獲得發展動力。 1987 年與法國當局簽署協議，並於 1988 年開始建造。度假村自此成為歐洲主要的旅遊目的地 [1]。\n\n"
    "## 設施 \n"
    "巴黎迪士尼樂園由兩個主題樂園組成：迪士尼樂園和華特迪士尼影城。迪士尼樂園設有美國小鎮大街、探險世界、邊域世界等主題區，提供巨雷山、加勒比海盜等各種景點。華特迪士尼影城於 2002 年開業，專注於電影主題體驗，包括「料理鼠王：冒險之旅」和「星際大戰：銀河邊緣」等景點。度假村還包括幾家酒店和迪士尼村，提供購物和餐飲，提供卓越而難忘的旅行體驗 [2]。\n\n"
    "## 訪客數量 \n"
    "近年來，巴黎迪士尼樂園的遊客數量大幅增加。 2023年，該度假區共接待遊客1,610萬人次，略微打破了先前的遊客人數紀錄。迪士尼樂園吸引了 1,040 萬遊客，而華特迪士尼影城則吸引了 570 萬遊客，比前一年增加了 6.7%。巴黎迪士尼樂園自開幕以來已接待了超過 3.75 億遊客 [3]。\n\n"
    "## 近期值得關注的事件 \n"
    "最近值得關注的活動包括 2022 年慶祝巴黎迪士尼樂園成立 30 週年。該度假村也因其創新的體驗和故事敘述而獲得認可。此外，巴黎迪士尼樂園還擴大了其服務範圍，增加了新的景點和主題區域，例如將於 2022 年開放的漫威復仇者聯盟園區。這些發展幫助該度假村維持了歐洲領先旅遊目的地的地位 [4]。\n\n"
)

# Content for high information completeness
LOW_INFO_CONTENT = (
    "## 巴黎迪士尼樂園介紹 \n"
    "巴黎迪士尼樂園，前身為歐洲迪士尼，於 1992 年開幕。這是一個擁有許多景點的大型公園。建造這個公園的想法很早以前就有了，但是卻花了一段時間才建成。它位於巴黎附近，非常受遊客歡迎[1]。\n\n"
    "## 設施 \n"
    "巴黎迪士尼樂園有兩個主要園區：迪士尼樂園和華特迪士尼影城。這裡有很多遊樂設施和表演，但一次參觀很難看完所有表演。公園很大，所以你需要仔細規劃你的行程。這裡還有一些飯店和一個名為迪士尼村的購物區。這是一個有趣的地方，特別是如果你喜歡迪士尼電影 [2]。\n\n"
    "## 訪客數量 \n"
    "每年都有很多人參觀巴黎迪士尼樂園。近年來，這裡非常繁忙，來自世界各地的遊客多達數百萬。確切的數字令人印象深刻，但很明顯，該公園是歐洲最受歡迎的旅遊景點之一。在假日和夏季，公園似乎會變得更加繁忙 [3]。\n\n"
    "## 近期值得關注的事件 \n"
    "巴黎迪士尼樂園最近舉辦了一些令人興奮的活動。他們最近慶祝了一個重要的周年紀念日，這是一件大事。公園也不斷增加新的景點和區域，為遊客增添樂趣。此外，巴黎迪士尼樂園還有一個不錯的應用程序，可以幫助您規劃行程並避免排長隊。公園裡的食物也相當不錯，有很多主題餐廳和咖啡館。總的來說，這是一個與家人或朋友共度時光的好地方[4]。\n\n"
)

# References for low information source quality
LOW_SOURCE_REFS = (
    "References:\n"
    "1. Anonymous. (2008). My Trip to Disneyland Paris! Retrieved from https://n&tab=TT&sl=en&tl=zh-TW&op.com\n"
    "2. Terry, B (2004). Sharing My Trip to Disneyland Paris with You. Retrieved from https://en&tl=zh-TW&text=make%20the%20below%\n"
    "3. Anonymous. (2006). Visiting Disneyland Paris. Retrieved from https://%20uk%203%3A%0A%0A.html\n"
    "4. Wilson, K. (n.d). Experiences in Disneyland Paris. Retrieved from https://?q=21899&tip=sid&clean=0\n\n"
)

# References for high information source quality
HIGH_SOURCE_REFS = (
    "References:\n"
    "1. Disneyland Paris News. (2024). History. Retrieved from https://news.disneylandparis.com/en/history/\n"
    "2. Lambert, J. (2023). Enhancing Guest Experiences through Technology: A Case Study of Disneyland Paris. Journal of Theme Park and Attraction Management, 15(1), 12–25. Retrieved from https://www.jtpam.org/articles/technology-disneylandparis\n"
    "3. Statista. (2024). Visitation at Walt Disney Studios Park (Paris) 2023. Retrieved from https://www.statista.com/statistics/236191/attendance-at-the-disneyland-paris-walt-disney-studios-park-theme-park/\n"
    "4. Disneyland Paris Official. (2024). Disneyland Paris Recent Events. Retrieved from https://www.disneylandparis.com/en-usd/offers/\n\n"
)
