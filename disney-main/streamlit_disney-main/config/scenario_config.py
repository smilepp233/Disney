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
LOW_INFO_CONTENT = (
    "## Introduction to Disneyland Paris \n"
    "Disneyland Paris, previously known as Euro Disney, opened in 1992. It's a big park with lots of attractions. The idea for the park started a long time ago, but it took a while to get built. It's located near Paris and is very popular among tourists [1].\n\n"
    "## Facilities \n"
    "Disneyland Paris has two main parks: Disneyland Park and Walt Disney Studios Park. There are lots of rides and shows, but it's hard to see everything in one visit. The park is big, so you need to plan your day carefully. There are also some hotels and a shopping area called Disney Village. It's a fun place to visit, especially if you like Disney movies [2].\n\n"
    "## Visitor Numbers \n"
    "A lot of people visit Disneyland Paris every year. In recent years, it has been very busy, with millions of visitors coming from all over the world. The exact numbers are impressive, but it's clear that the park is one of the most popular tourist spots in Europe. The park seems to get busier during holidays and summer months [3].\n\n"
    "## Notable Recent Events \n"
    "Disneyland Paris has had some exciting events lately. They celebrated a big anniversary recently, which was a big deal. The park also keeps adding new attractions and areas, which makes it interesting for visitors. Additionally, Disneyland Paris has a nice app that helps you plan your visit and avoid long lines. The park's food is also quite good, with lots of themed restaurants and cafes. Overall, it's a great place to spend time with family or friends [4].\n\n"
)

# Content for high information completeness
HIGH_INFO_CONTENT = (
    "## Introduction to Disneyland Paris \n"
    "Disneyland Paris, originally known as Euro Disney Resort, opened on April 12, 1992, marking a significant milestone in European entertainment. The idea for the park began to take shape in the late 1970s, but it wasn't until the success of Tokyo Disneyland in 1983 that the project gained momentum. An agreement with French authorities was signed in 1987, and construction started in 1988. The resort has since become a major tourist destination in Europe [1].\n\n"
    "## Facilities \n"
    "Disneyland Paris comprises two theme parks: Disneyland Park and Walt Disney Studios Park. Disneyland Park features themed areas like Main Street USA, Adventureland, and Frontierland, offering a wide range of attractions such as Big Thunder Mountain and Pirates of the Caribbean. Walt Disney Studios Park, opened in 2002, focuses on movie-themed experiences with attractions like Ratatouille: The Adventure and Star Wars: Galaxy's Edge. The resort also includes several hotels and Disney Village for shopping and dining, offering excellent and unforgettable travel experience [2].\n\n"
    "## Visitor Numbers \n"
    "In recent years, Disneyland Paris has seen significant visitor numbers. In 2023, the resort welcomed a total of 16.1 million visitors, narrowly beating its previous attendance record. Disneyland Park attracted 10.4 million visitors, while Walt Disney Studios Park saw 5.7 million, marking a 6.7% increase from the previous year. Over its lifetime, Disneyland Paris has hosted more than 375 million visitors [3].\n\n"
    "## Notable Recent Events \n"
    "Notable recent events include the celebration of Disneyland Paris's 30th anniversary in 2022. The resort has also been recognized for its innovative experiences and storytelling. In addition, Disneyland Paris has expanded its offerings with new attractions and themed areas, such as the Marvel Avengers Campus, which opened in 2022. These developments have helped maintain the resort's position as a leading European tourist destination [4].\n\n"
)

# References for low information source quality
LOW_SOURCE_REFS = (
    "References:\n"
    "1. Johnson, A. (2024). My Magical Adventure at Disneyland Paris! Retrieved from https://disneyfanblog.com\n"
    "2. Terry, B. (2024). Top Tips for Visiting Disneyland Paris. Retrieved from https://travel/%22z5few6y5%.com\n"
    "3. Johnson, K. (2023). Top 5 Attractions at Disneyland Paris [Video]. YouTube. Retrieved from https://www.youtube.com/watch?v=disneylandparisvideo\n"
    "4. Smith, S. (2024). My Family's Fun Day at Disneyland Paris. Retrieved from https://familytravelblog.net/disneylandparisreview\n\n"
)

# References for high information source quality
HIGH_SOURCE_REFS = (
    "References:\n"
    "1. Disneyland Paris News. (2024). History. Retrieved from https://news.disneylandparis.com/en/history/\n"
    "2. Lambert, J. (2023). Enhancing Guest Experiences through Technology: A Case Study of Disneyland Paris. Journal of Theme Park and Attraction Management, 15(1), 12–25. Retrieved from https://www.jtpam.org/articles/technology-disneylandparis\n"
    "3. Statista. (2024). Visitation at Walt Disney Studios Park (Paris) 2023. Retrieved from https://www.statista.com/statistics/236191/attendance-at-the-disneyland-paris-walt-disney-studios-park-theme-park/\n"
    "4. Disneyland Paris Official. (2024). Disneyland Paris Recent Events. Retrieved from https://www.disneylandparis.com/en-usd/offers/\n\n"
)
