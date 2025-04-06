"""
Utility functions for the chatbot module.
Contains the AgricultureResponseGenerator class for generating responses to agriculture-related queries.
"""

class AgricultureResponseGenerator:
    """
    A class for generating responses to agriculture-related queries.
    """
    
    @staticmethod
    def generate_response(user_input, conversation_history=None):
        """
        Generate a response to the user's agriculture-related query.
        
        Args:
            user_input (str): The user's question or message
            conversation_history (list, optional): List of previous messages for context
            
        Returns:
            str: A response to the user's query
        """
        # Convert user input to lowercase for easier matching
        user_input_lower = user_input.lower()
        
        # Extract previous messages for context if available
        previous_messages = []
        if conversation_history:
            for message in conversation_history:
                if 'user_input' in message and message['user_input']:
                    previous_messages.append(message['user_input'])
        
        # Basic response logic based on keywords
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return "Hello! I'm your agricultural assistant. How can I help you today?"
            
        elif any(word in user_input_lower for word in ['crop disease', 'plant disease', 'disease']):
            return "Crop diseases can significantly impact yield. Common diseases include fungal infections like powdery mildew, bacterial infections, and viral diseases. Regular monitoring, proper spacing, and appropriate fungicides can help manage crop diseases. Would you like information about a specific crop disease?"
            
        elif any(word in user_input_lower for word in ['fertilizer', 'nutrient', 'soil health']):
            return "Fertilizers provide essential nutrients for plant growth. The three main nutrients are Nitrogen (N), Phosphorus (P), and Potassium (K). Organic fertilizers like compost and manure improve soil health over time, while chemical fertilizers provide immediate nutrients. Soil testing can help determine the specific needs of your soil."
            
        elif any(word in user_input_lower for word in ['irrigation', 'water', 'watering']):
            return "Proper irrigation is crucial for crop health. Drip irrigation and sprinkler systems are efficient methods. The water needs vary by crop type, growth stage, soil type, and climate. Overwatering can lead to root diseases, while underwatering causes stress and reduced yield."
            
        elif any(word in user_input_lower for word in ['pest', 'insect', 'bug']):
            return "Pest management is essential for crop protection. Integrated Pest Management (IPM) combines biological controls, habitat manipulation, and resistant crop varieties with judicious pesticide use. Beneficial insects like ladybugs and praying mantises can help control harmful pests naturally."
            
        elif any(word in user_input_lower for word in ['organic', 'natural', 'chemical free']):
            return "Organic farming avoids synthetic fertilizers and pesticides, focusing on crop rotation, green manure, compost, and biological pest control. It promotes biodiversity and sustainable soil health. Organic certification requires following specific standards and practices."
            
        elif any(word in user_input_lower for word in ['weather', 'climate', 'rain', 'temperature']):
            return "Weather conditions significantly impact agriculture. Monitoring forecasts helps in planning planting, irrigation, and harvesting. Climate change is affecting growing seasons and increasing extreme weather events, requiring adaptation strategies like drought-resistant crops and improved water management."
            
        elif any(word in user_input_lower for word in ['harvest', 'harvesting', 'yield']):
            return "Harvesting at the right time maximizes yield and quality. Signs of readiness vary by crop but often include color changes, size, and firmness. Proper harvesting techniques and equipment reduce damage and post-harvest losses."
            
        elif any(word in user_input_lower for word in ['seed', 'planting', 'sowing']):
            return "Seed selection is crucial for successful farming. Consider factors like climate suitability, disease resistance, yield potential, and market demand. Proper seed spacing and planting depth vary by crop type and should be followed for optimal germination and growth."
            
        elif any(word in user_input_lower for word in ['soil', 'land', 'earth']):
            return "Soil health is the foundation of agriculture. Good soil contains a balance of minerals, organic matter, air, and water. Regular testing helps monitor pH and nutrient levels. Practices like crop rotation, cover cropping, and minimal tillage improve soil structure and fertility over time."
            
        # Default response if no keywords match
        else:
            return "I'm here to help with agricultural questions. You can ask about crop diseases, fertilizers, irrigation, pest management, organic farming, weather impacts, harvesting, seed selection, or soil health. How can I assist you today?"
