"""
Student Support Agent using Google ADK
A comprehensive AI agent to handle student inquiries about online courses
"""

import os
import logging
from typing import Optional, Dict, Any
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .config import Config, ModelProvider
from .tools import (
    get_course_information,
    get_schedule_and_timing,
    get_payment_information,
    get_support_services,
    get_certification_info,
    search_faqs,
    get_enrollment_process,
    check_prerequisites
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StudentSupportAgent:
    """
    Main Student Support Agent class that handles model selection and configuration
    """
    
    def __init__(self, model_provider: Optional[ModelProvider] = None):
        """
        Initialize the Student Support Agent
        
        Args:
            model_provider: Preferred model provider (gemini, openai, or anthropic)
                          If None, uses default from config
        """
        self.config = Config()
        self.model_provider = model_provider or self.config.DEFAULT_MODEL
        
        # Validate model availability
        if not self.config.validate_model(self.model_provider):
            available_models = self.config.get_available_models()
            if available_models:
                self.model_provider = available_models[0]
                logger.warning(f"Requested model not available. Using {self.model_provider} instead.")
            else:
                raise ValueError("No API keys configured. Please set at least one API key in .env file.")
        
        self.agent = self._create_agent()
        logger.info(f"Student Support Agent initialized with {self.model_provider} model")
    
    def _create_agent(self) -> Agent:
        """Create and configure the ADK agent"""
        
        # Get model configuration
        model_config = self.config.get_model_config(self.model_provider)
        
        # Create model instance based on provider
        if self.model_provider == "gemini":
            model = model_config["model_id"]  # Direct string for Gemini
        else:
            # Use LiteLLM for OpenAI and Anthropic
            model = LiteLlm(
                model=model_config["model_id"],
                temperature=model_config["temperature"],
                max_tokens=model_config["max_tokens"]
            )
        
        # Agent instructions
        instruction = """
        You are a friendly and knowledgeable Student Support Agent for Scoreazy, an online education platform. 
        Your role is to help prospective and current students with their questions about courses, enrollment, 
        schedules, payments, and general support.
        
        Key guidelines:
        1. Always be helpful, professional, and empathetic
        2. Use the available tools to provide accurate, up-to-date information
        3. If you don't have specific information, direct students to appropriate support channels
        4. Personalize responses when possible based on the student's specific situation
        5. Always encourage learning and help students find the right educational path
        6. Be concise but comprehensive in your responses
        7. If a student asks about something outside your knowledge base, politely explain your limitations
        
        You have access to comprehensive information about:
        - Course catalog, descriptions, and prerequisites
        - Schedules and timing information
        - Payment options and financial policies
        - Student support services
        - Certification and completion requirements
        - Frequently asked questions
        - Enrollment processes and requirements
        
        Remember: Your goal is to make the student's educational journey as smooth and successful as possible!
        """
        
        # Create agent with tools
        agent = Agent(
            name="student_support_agent",
            model=model,
            description="AI agent to help students with course-related inquiries and support",
            instruction=instruction,
            tools=[
                get_course_information,
                get_schedule_and_timing,
                get_payment_information,
                get_support_services,
                get_certification_info,
                search_faqs,
                get_enrollment_process,
                check_prerequisites
            ]
        )
        
        return agent
    
    def chat(self, message: str) -> str:
        """
        Process a student message and return response
        
        Args:
            message: Student's question or message
            
        Returns:
            Agent's response as a string
        """
        try:
            response = self.agent.run(message)
            return response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return "I apologize, but I'm experiencing some technical difficulties. Please try again or contact our support team directly."
    
    def get_agent_info(self) -> Dict[str, Any]:
        """Get information about the agent configuration"""
        return {
            "model_provider": self.model_provider,
            "model_config": self.config.get_model_config(self.model_provider),
            "available_models": self.config.get_available_models(),
            "tools_available": len(self.agent.tools),
            "agent_name": self.agent.name
        }

def create_agent(model_provider: Optional[ModelProvider] = None) -> StudentSupportAgent:
    """
    Factory function to create a Student Support Agent
    
    Args:
        model_provider: Preferred model provider
        
    Returns:
        Configured StudentSupportAgent instance
    """
    return StudentSupportAgent(model_provider)

# Create default agent instance for ADK
try:
    # This will be the main agent that ADK discovers
    root_agent = create_agent().agent
    logger.info("Root agent created successfully")
except Exception as e:
    logger.error(f"Failed to create root agent: {e}")
    # Create a minimal fallback agent if configuration fails
    root_agent = Agent(
        name="student_support_fallback",
        model="gemini-2.0-flash",  # Fallback to default Gemini
        description="Fallback student support agent",
        instruction="I'm a basic student support agent. Please configure your API keys properly for full functionality.",
        tools=[]
    )
