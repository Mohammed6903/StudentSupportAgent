#!/usr/bin/env python3
"""
Setup script for the Student Support Agent
Helps configure API keys and validate the environment
"""

import os
import sys
from pathlib import Path

def setup_environment():
    """Setup the agent environment"""
    print("🎓 Student Support Agent Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("student_support_agent").exists():
        print("❌ Please run this script from the project root directory")
        return False
    
    env_file = Path("student_support_agent/.env")
    
    print("\n📋 Current Configuration:")
    if env_file.exists():
        print("✅ .env file found")
        
        # Read current configuration
        with open(env_file, 'r') as f:
            content = f.read()
            
        # Check for API keys
        has_gemini = "GOOGLE_API_KEY=your_" not in content and "GOOGLE_API_KEY=" in content
        has_openai = "OPENAI_API_KEY=your_" not in content and "OPENAI_API_KEY=" in content  
        has_anthropic = "ANTHROPIC_API_KEY=your_" not in content and "ANTHROPIC_API_KEY=" in content
        
        print(f"{'✅' if has_gemini else '❌'} Gemini API Key")
        print(f"{'✅' if has_openai else '❌'} OpenAI API Key") 
        print(f"{'✅' if has_anthropic else '❌'} Anthropic API Key")
        
        if not (has_gemini or has_openai or has_anthropic):
            print("\n⚠️  No API keys configured!")
            print("\nTo get API keys:")
            print("🔹 Gemini (Recommended): https://aistudio.google.com/apikey")
            print("🔹 OpenAI: https://platform.openai.com/api-keys")
            print("🔹 Anthropic: https://console.anthropic.com/")
            
            setup_keys = input("\nWould you like to configure API keys now? (y/n): ").strip().lower()
            if setup_keys in ['y', 'yes']:
                configure_api_keys(env_file)
        
    else:
        print("❌ .env file not found")
        print("Creating .env file...")
        configure_api_keys(env_file)
    
    print("\n🧪 Running Tests...")
    test_result = run_tests()
    
    if test_result:
        print("\n🚀 Setup Complete!")
        print("\nYou can now run the agent using:")
        print("  • adk web (Web interface)")
        print("  • python demo.py (Demo script)")
        print("  • python demo.py interactive (Interactive mode)")
    else:
        print("\n❌ Setup incomplete. Please check the errors above.")
    
    return test_result

def configure_api_keys(env_file):
    """Configure API keys interactively"""
    print("\n🔑 API Key Configuration")
    print("-" * 30)
    
    # Read existing file if it exists
    existing_content = ""
    if env_file.exists():
        with open(env_file, 'r') as f:
            existing_content = f.read()
    
    # Configure Gemini (recommended)
    print("\n🎯 Gemini API Key (Recommended - Free tier available)")
    print("Get your key at: https://aistudio.google.com/apikey")
    gemini_key = input("Enter Gemini API key (or press Enter to skip): ").strip()
    
    # Configure OpenAI (optional)
    print("\n🤖 OpenAI API Key (Optional)")
    print("Get your key at: https://platform.openai.com/api-keys")
    openai_key = input("Enter OpenAI API key (or press Enter to skip): ").strip()
    
    # Configure Anthropic (optional)
    print("\n🧠 Anthropic API Key (Optional)")
    print("Get your key at: https://console.anthropic.com/")
    anthropic_key = input("Enter Anthropic API key (or press Enter to skip): ").strip()
    
    # Create .env content
    env_content = f"""# Model Configuration
# Set your preferred model provider and API keys

# Gemini (Default) - Google AI Studio
GOOGLE_API_KEY={gemini_key if gemini_key else 'your_gemini_api_key_here'}
GOOGLE_GENAI_USE_VERTEXAI=FALSE

# OpenAI (Optional)
OPENAI_API_KEY={openai_key if openai_key else 'your_openai_api_key_here'}

# Anthropic (Optional)
ANTHROPIC_API_KEY={anthropic_key if anthropic_key else 'your_anthropic_api_key_here'}

# Default model selection (gemini, openai, or anthropic)
DEFAULT_MODEL=gemini"""
    
    # Write to file
    with open(env_file, 'w') as f:
        f.write(env_content)
    
    print(f"\n✅ Configuration saved to {env_file}")
    
    if not any([gemini_key, openai_key, anthropic_key]):
        print("\n⚠️  No API keys provided. You'll need to edit the .env file manually.")

def run_tests():
    """Run basic tests to validate setup"""
    try:
        # Test imports
        from student_support_agent.tools import get_course_information
        from student_support_agent.config import Config
        
        # Test basic functionality
        result = get_course_information("python")
        if result.get("status") != "success":
            print("❌ Tool test failed")
            return False
        
        # Test configuration
        config = Config()
        available_models = config.get_available_models()
        
        if not available_models:
            print("❌ No models available - please configure API keys")
            return False
        
        print(f"✅ Available models: {', '.join(available_models)}")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main setup function"""
    try:
        success = setup_environment()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        sys.exit(1)

if __name__ == "__main__":
    main()
