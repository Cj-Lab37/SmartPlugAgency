# Module_Description of external_data_for_input.py:
# Purpose: This script handles the collection, validation, and processing of external data inputs before pasring it to input.py to be initialed as intial input and start of metadata json as a new project for SMARTPLUGAGENCY.
# Functionality: 
# - Defines a JSON template for external data input, including projects and general data.
# - Validates the required fields in the external data to ensure completeness and correctness.
# - Processes the external data and saves it in a JSON file to be parsed to input.py.
# Interactions: 
# - Interacts with `input.py` to provide processed external data for integration as manual inputs for the project in input.py.
# - Ensures that the external data is formatted and validated before being passed to the next stages of the project "input.py".
# Reason: 
# - Centralizes the handling of external data inputs, making the code more manageable and maintainable.
# - Enhances data integrity and reduces the risk of errors by validating inputs before processing.








# --------------------------------------------------------------------------------------------------------------------------------------------------


# JSON template for external data input
external_data_template = {
    "projects": [
        {
            "type_of_project": "",  # project_made_by_this_agency (or) project_made_by_another_agency
            "purpose": "",  # refinement (or) analysis (or) update (or) failure_analysis
            "source": "",  # our_own_data (or) new_client (or) other_entity_data (or) feedback
            "file_format": "",  # json (or) csv (or) txt
            "description": "",  # Further description of the project [type_of_project, purpose, source, etc.], plus any additional details like sentiments , goals, personal impressions of the data provided by the client or us or other entity.
            "upload_date": datetime.now().strftime("%Y-%m-%d"),  # Current date
            "user_context": {
                "project_name": "",  # Name of the project "preferable to be expressive of the project purpose", if its a project made by us, then it should be the name of the project we gave it"preferably".
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
                }
,
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

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Function to validate and process external data
def process_external_data(external_data):
    # Validate that at least one section (projects or general_data) has data
    projects = external_data.get("projects", [])
    general_data = external_data.get("general_data", [])
    
    if not projects and not general_data:
        raise ValueError("Error: Both 'projects' and 'general_data' sections are empty. At least one section must contain data.")

    # Function to check if_to_audience fields and report status
    def check_audience_fields(audience_data):
        if not audience_data:
            return "if_to_audience section is completely empty"
        
        audience_fields = [
            "tone", "sentiment", "target_audience", "engagement_style", 
            "content_format", "language", "cultural_context", "distribution_channel",
            "visual_style", "platform_specific_requirements", "call_to_action",
            "content_frequency", "performance_metrics", "accessibility_features",
            "legal_compliance", "brand_guidelines"
        ]
        
        filled = [field for field in audience_fields if audience_data.get(field)]
        empty = [field for field in audience_fields if not audience_data.get(field)]
        
        return {
            "filled_fields": filled if filled else "None",
            "empty_fields": empty if empty else "None"
        }

    for project in external_data.get("projects", []):
        # Check required fields
        required_fields = ["type_of_project", "purpose", "source", "file_format", 
                        "description", "upload_date", "user_context", "data"]
        missing = [field for field in required_fields if not project.get(field)]
        if missing:
            project_name = project.get('user_context', {}).get('project_name', 'Unnamed')
            raise ValueError(f"Error in project '{project_name}': Missing required fields: {missing}")
            
        # Check user_context required subfields
        if not all(key in project["user_context"] for key in ["project_name", "description"]):
            project_name = project.get('user_context', {}).get('project_name', 'Unnamed')
            raise ValueError(f"Error in project '{project_name}': Missing required fields in user_context")
            
        # Check and report if_to_audience status
        audience_status = check_audience_fields(project.get("if_to_audience", {}))
        # Check and report if_to_audience status
        audience_status = check_audience_fields(project.get("if_to_audience", {}))
        print(f"\nProject '{project.get('user_context', {}).get('project_name', 'Unnamed')}' audience fields status:")
        print(f"Filled fields: {audience_status['filled_fields']}")
        print(f"Empty fields: {audience_status['empty_fields']}")

    # Validate general data
    for general_item in general_data:
        required_fields = ["type_of_data", "purpose", "source", "file_format", 
                        "description", "upload_date", "entity_context", "data"]
        missing = [field for field in required_fields if not general_item.get(field)]
        if missing:
            entity_name = general_item.get('entity_context', {}).get('entity', 'Unnamed')
            raise ValueError(f"Error in general data for entity '{entity_name}': Missing required fields: {missing}")
        if missing:
            raise ValueError(f"Missing required fields in general data: {missing}")
            
        # Check entity_context required subfields
        if not all(key in general_data["entity_context"] for key in ["entity", "description"]):
            raise ValueError("Missing required fields in entity_context")
            
        # Check and report if_to_audience status
        audience_status = check_audience_fields(general_data.get("if_to_audience", {}))
        print(f"\nGeneral data for entity '{general_data.get('entity_context', {}).get('entity', 'Unnamed')}' audience fields status:")
        print(f"Filled fields: {audience_status['filled_fields']}")
        print(f"Empty fields: {audience_status['empty_fields']}")


# Save external data to temporary file for processing
    try:
        with open('temp_external_data.json', 'w') as file:
            json.dump(external_data, file, indent=4)

        # Import input module and attempt to process the data
        try:
            if process_input('temp_external_data.json'):
                # Success case: Reset template to default empty state
                for project in external_data["projects"]:
                    for key in project:
                        if isinstance(project[key], dict):
                            for subkey in project[key]:
                                project[key][subkey] = ""
                        elif key != "upload_date":
                            project[key] = ""
                
                for gen_data in external_data["general_data"]:
                    for key in gen_data:
                        if isinstance(gen_data[key], dict):
                            for subkey in gen_data[key]:
                                gen_data[key][subkey] = ""
                        elif key != "upload_date":
                            gen_data[key] = ""
                
                print("Success: Data processed and accepted by input.py. Template reset to default state.")
            else:
                raise ValueError("Data was not accepted by input.py")
        except ImportError:
            raise ImportError("Error: Could not import input.py module. Please ensure it exists in the correct location.")
        except Exception as e:
            raise Exception(f"Error in input.py processing: {str(e)}")
        finally:
            # Clean up temporary file
            if os.path.exists('temp_external_data.json'):
                os.remove('temp_external_data.json')
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Note: Template data preserved due to processing failure.")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Example usage
external_data = external_data_template
process_external_data(external_data)
