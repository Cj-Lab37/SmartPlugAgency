import json
from datetime import datetime

# Placeholder for actual data
Actual_Data = {}
Actual_General_Data = {}

# gather_inputs function to collect user inputs from either direct_input, indirect_input or external_data_input
def gather_inputs():
    # Direct Input plat
    direct_input = {
        "Search link(s)": input("Enter Link(s) (comma-separated): "),
        "link(s) for": input("Enter the platform (e.g., Youtube, Instagram, Website, etc.): "),
        "Topic(s)": input("Enter topics of interest: "),
        "Keyword(s)": input("Enter relevant keywords (comma-separated): "),
        "Hashtag(s)": input("Enter relevant hashtags (comma-separated): "),
        "Video Length Preference": input("Enter video length preference (short, medium, long): "),
        "Language": input("Enter language of videos: "),
        "Upload Date Range": input("Enter upload date range (YYYY-MM-DD to YYYY-MM-DD): "),
        "Region/Country": input("Enter region/country: "),
        "Channel Category": input("Enter channel category: ")
    }

    # Indirect Input
    indirect_input = {
        "Keyword(s)": input("Enter general keywords (comma-separated): "),
        "Hashtag(s)": input("Enter hashtags (comma-separated): "),
        "Target Audience(s)": input("Enter target audience demographics (comma-separated): "),
        "Type of Content": input("Enter content type: "),
        "Whom is it for": input("Specify the audience or user preferences: "),
        "Audience Preferences": input("Enter audience preferences: "),
        "User Preferences": input("Enter additional preferences: "),
        "Content Format": input("Specify content format: "),
        "Engagement Metrics Preference": input("Enter preferred engagement metrics: "),
        "Content Frequency": input("Indicate content update frequency: "),
        "Content Tone/Style": input("Specify preferred tone/style: "),
        "Competitor Analysis": input("Enter competitor channels or content: ")
    }
    # External data input
    external_data_input = {
        "projects": [
            {
                "type_of_project": "",  # project_made_by_this_agency (or) project_made_by_another_agency
                "purpose": "",  # refinement (or) analysis (or) update (or) failure_analysis
                "source": "",  # our_own_data (or) new_client (or) other_entity_data (or) feedback
                "file_format": "",  # json (or) csv (or) txt
                "description": "",  # Further description of the project [type_of_project, purpose, source, etc.], plus any additional details like sentiments, goals, personal impressions of the data provided by the client or us or other entity.
                "upload_date": datetime.now().strftime("%Y-%m-%d"),  # Current date
                "user_context": {
                    "project_name": "",  # Name of the project "preferable to be expressive of the project purpose", if it's a project made by us, then it should be the name of the project we gave it "preferably".
                    "description": ""  # Data for analysis and integration into the knowledge base.
                },
                "if_to_audience": {
                    "tone": "",  # The overall tone of the content (e.g., humorous, serious, informative)
                    "sentiment": "",  # The sentiment conveyed by the content (e.g., positive, negative, neutral)
                    "target_audience": "",  # The specific audience the content is intended for (e.g., teenagers, professionals, parents)
                    "engagement_style": "",  # The style of engagement expected (e.g., interactive, passive, call-to-action)
                    "content_format": "",  # The format of the content (e.g., video, article, infographic)
                    "language": "",  # The language in which the content should be presented
                    "cultural_context": "",  # Any cultural considerations or context that should be taken into account
                    "distribution_channel": "",  # The channels through which the content will be distributed (e.g., social media, email, website)
                    "visual_style": "",  # The visual style of the content (e.g., minimalist, vibrant, professional)
                    "platform_specific_requirements": "",  # Any specific requirements or guidelines for the platform where the content will be published (e.g., Instagram, YouTube, LinkedIn)
                    "call_to_action": "",  # Specific calls to action that should be included in the content (e.g., subscribe, follow, buy now)
                    "content_frequency": "",  # How often the content should be updated or posted (e.g., daily, weekly, monthly)
                    "performance_metrics": "",  # Key performance indicators to measure the success of the content (e.g., engagement rate, click-through rate, conversion rate)
                    "accessibility_features": "",  # Any accessibility features that should be included (e.g., captions, alt text, audio descriptions)
                    "legal_compliance": "",  # Any legal or compliance requirements that need to be considered (e.g., GDPR, COPPA)
                    "brand_guidelines": ""  # Specific brand guidelines that need to be followed (e.g., color schemes, logos, fonts)
                },
                "data": Actual_Data
            }
        ],
        "general_data": [
            {
                "type_of_data": "",  # insights about influencers, product, service, viral events or trend, etc.
                "purpose": "",  # knowledge_base, analysis, update, etc.
                "source": "",  # from where this data is collected: enitiyBrandName_or_enitityName, web_scraping, our_own_data, bought_data, feedback, etc.
                "file_format": "",  # csv (or) txt (or) json
                "description": "",  # Description of the data purpose, source, content, goals, etc. this is where you can provide more details about the data.
                "upload_date": datetime.now().strftime("%Y-%m-%d"),  # Current date
                "entity_context": {
                    "entity": "",  # Influencer, Product, Service, Viral Event, Trend, etc.
                    "description": ""  # Here you can provide more details about the entity. Example: Data to improve knowledge base about influencer trends or Data to analyze and understand viral events.
                },
                "if_to_audience": {
                    "tone": "",  # The overall tone of the content (e.g., humorous, serious, informative)
                    "sentiment": "",  # The sentiment conveyed by the content (e.g., positive, negative, neutral)
                    "target_audience": "",  # The specific audience the content is intended for (e.g., teenagers, professionals, parents)
                    "engagement_style": "",  # The style of engagement expected (e.g., interactive, passive, call-to-action)
                    "content_format": "",  # The format of the content (e.g., video, article, infographic)
                    "language": "",  # The language in which the content should be presented
                    "cultural_context": "",  # Any cultural considerations or context that should be taken into account
                    "distribution_channel": "",  # The channels through which the content will be distributed (e.g., social media, email, website)
                    "visual_style": "",  # The visual style of the content (e.g., minimalist, vibrant, professional)
                    "platform_specific_requirements": "",  # Any specific requirements or guidelines for the platform where the content will be published (e.g., Instagram, YouTube, LinkedIn)
                    "call_to_action": "",  # Specific calls to action that should be included in the content (e.g., subscribe, follow, buy now)
                    "content_frequency": "",  # How often the content should be updated or posted (e.g., daily, weekly, monthly)
                    "performance_metrics": "",  # Key performance indicators to measure the success of the content (e.g., engagement rate, click-through rate, conversion rate)
                    "accessibility_features": "",  # Any accessibility features that should be included (e.g., captions, alt text, audio descriptions)
                    "legal_compliance": "",  # Any legal or compliance requirements that need to be considered (e.g., GDPR, COPPA)
                    "brand_guidelines": ""  # Specific brand guidelines that need to be followed (e.g., color schemes, logos, fonts)
                },
                "data": Actual_General_Data
            }
        ]
    }


# process_inputs function to process the gathered inputs
    

    # Validate if all required fields are filled

    # Initiate "metadata.json" file and write the gathered verified inputs to it, add the mudule report and process completed, check the metadata.json model here "templates\json\metadata.json"

    #save a copy to knowledge_base/Project_life_span_memory/ 