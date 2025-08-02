"""
Demonstration script for the Student Support Agent
Shows various scenarios and agent capabilities
"""

import os
import sys
from typing import List, Dict

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from student_support_agent.agent import create_agent
from student_support_agent.config import Config

class AgentDemo:
    """Demo class for the Student Support Agent"""
    
    def __init__(self):
        self.config = Config()
        print("🎓 Student Support Agent Demo")
        print("=" * 50)
        
        # Show available models
        available_models = self.config.get_available_models()
        if available_models:
            print(f"Available models: {', '.join(available_models)}")
            self.agent = create_agent()
            print(f"Using model: {self.agent.model_provider}")
            print(f"Agent info: {self.agent.get_agent_info()}")
        else:
            print("⚠️  No API keys configured. Please set up your API keys in the .env file.")
            self.agent = None
        
        print("=" * 50)
    
    def run_sample_conversations(self):
        """Run sample conversations to demonstrate agent capabilities"""
        
        if not self.agent:
            print("Cannot run demo without proper API key configuration.")
            return
        
        sample_questions = [
            "What courses do you offer?",
            "Tell me about the Python course",
            "What are the payment options?",
            "When does the AI course start?",
            "What are the prerequisites for Data Science course?",
            "How do I get a certificate?",
            "I need help with enrollment",
            "What support services are available?",
            "Can I get a refund?",
            "What are the technical requirements?"
        ]
        
        print("\n🤖 Agent Conversations Demo")
        print("-" * 40)
        
        for i, question in enumerate(sample_questions, 1):
            print(f"\n💬 Question {i}: {question}")
            print("🤖 Agent Response:")
            
            try:
                response = self.agent.chat(question)
                print(response)
            except Exception as e:
                print(f"Error: {e}")
            
            print("-" * 40)
    
    def interactive_mode(self):
        """Run interactive demo mode"""
        
        if not self.agent:
            print("Cannot run interactive mode without proper API key configuration.")
            return
        
        print("\n🎯 Interactive Mode")
        print("Type your questions (or 'quit' to exit)")
        print("-" * 40)
        
        while True:
            try:
                user_input = input("\n💬 Your question: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye! 👋")
                    break
                
                if not user_input:
                    continue
                
                print("🤖 Agent Response:")
                response = self.agent.chat(user_input)
                print(response)
                print("-" * 40)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main demo function"""
    demo = AgentDemo()
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        demo.interactive_mode()
    else:
        demo.run_sample_conversations()
        
        # Ask if user wants interactive mode
        if demo.agent:
            print("\n" + "=" * 50)
            try:
                choice = input("Would you like to try interactive mode? (y/n): ").strip().lower()
                if choice in ['y', 'yes']:
                    demo.interactive_mode()
            except KeyboardInterrupt:
                print("\nGoodbye! 👋")

if __name__ == "__main__":
    main()
