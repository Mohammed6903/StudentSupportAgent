"""
Configuration module for the Student Support Agent
Handles model selection, API keys, and environment setup
"""

import os
from typing import Optional, Literal, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model Types
ModelProvider = Literal["gemini", "openai", "anthropic"]

class Config:
    """Configuration class for the Student Support Agent"""
    
    # API Keys
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY") 
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    # Google AI settings
    GOOGLE_GENAI_USE_VERTEXAI: bool = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() == "TRUE"
    
    # Default model
    DEFAULT_MODEL: ModelProvider = os.getenv("DEFAULT_MODEL", "gemini")
    
    # Model configurations
    MODEL_CONFIGS: Dict[ModelProvider, Dict[str, Any]] = {
        "gemini": {
            "model_id": "gemini-2.0-flash",
            "max_tokens": 8192,
            "temperature": 0.7
        },
        "openai": {
            "model_id": "openai/gpt-4o",
            "max_tokens": 4096,
            "temperature": 0.7
        },
        "anthropic": {
            "model_id": "anthropic/claude-3-5-sonnet-20241022",
            "max_tokens": 4096,
            "temperature": 0.7
        }
    }
    
    @classmethod
    def get_available_models(cls) -> list[ModelProvider]:
        """Return list of models with valid API keys"""
        available = []
        
        if cls.GOOGLE_API_KEY:
            available.append("gemini")
        if cls.OPENAI_API_KEY:
            available.append("openai")
        if cls.ANTHROPIC_API_KEY:
            available.append("anthropic")
            
        return available
    
    @classmethod
    def validate_model(cls, model: ModelProvider) -> bool:
        """Validate if the specified model is available"""
        return model in cls.get_available_models()
    
    @classmethod
    def get_model_config(cls, model: ModelProvider) -> Dict[str, Any]:
        """Get configuration for specified model"""
        if not cls.validate_model(model):
            raise ValueError(f"Model '{model}' is not available. Check API key configuration.")
        
        return cls.MODEL_CONFIGS[model]
