"""
Offline demonstration of the Student Support Agent
Shows agent capabilities without requiring API keys
"""

import json
from student_support_agent.tools import (
    get_course_information,
    get_schedule_and_timing,
    get_payment_information,
    get_support_services,
    get_certification_info,
    search_faqs,
    get_enrollment_process,
    check_prerequisites
)

def demo_agent_tools():
    """Demonstrate all agent tools with sample queries"""
    
    print("🎓 Student Support Agent - Tool Demonstration")
    print("=" * 60)
    
    demos = [
        {
            "title": "Course Information Query",
            "description": "Student asks: 'Tell me about the Python course'",
            "tool": get_course_information,
            "input": "python"
        },
        {
            "title": "Schedule and Timing Query", 
            "description": "Student asks: 'When does the AI course start?'",
            "tool": get_schedule_and_timing,
            "input": "ai101"
        },
        {
            "title": "Payment Information Query",
            "description": "Student asks: 'What are the payment options for Data Science?'",
            "tool": get_payment_information,
            "input": "ds201"
        },
        {
            "title": "Support Services Query",
            "description": "Student asks: 'What support is available?'",
            "tool": get_support_services,
            "input": None
        },
        {
            "title": "Certification Information",
            "description": "Student asks: 'How do I get certified?'",
            "tool": get_certification_info,
            "input": None
        },
        {
            "title": "FAQ Search",
            "description": "Student asks: 'Can I get a refund?'",
            "tool": search_faqs,
            "input": "refund"
        },
        {
            "title": "Enrollment Process",
            "description": "Student asks: 'How do I enroll in the Python course?'",
            "tool": get_enrollment_process,
            "input": "py101"
        },
        {
            "title": "Prerequisites Check",
            "description": "Student asks: 'What are the prerequisites for AI course?'",
            "tool": check_prerequisites,
            "input": "ai101"
        }
    ]
    
    for i, demo in enumerate(demos, 1):
        print(f"\n{i}. {demo['title']}")
        print(f"   {demo['description']}")
        print("   " + "-" * 50)
        
        try:
            if demo['input'] is not None:
                result = demo['tool'](demo['input'])
            else:
                result = demo['tool']()
            
            # Format and display result
            formatted_result = format_tool_output(result)
            print(f"   🤖 Agent Response:\n{formatted_result}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print("   " + "=" * 50)

def format_tool_output(result):
    """Format tool output for better readability"""
    if not isinstance(result, dict):
        return str(result)
    
    formatted_lines = []
    indent = "      "
    
    if result.get("status") == "success":
        if "course" in result:
            course = result["course"]
            formatted_lines.append(f"{indent}📚 Course: {course['name']}")
            formatted_lines.append(f"{indent}💰 Price: {course['price']}")
            formatted_lines.append(f"{indent}⏱️  Duration: {course['duration']}")
            formatted_lines.append(f"{indent}👨‍🏫 Instructor: {course['instructor']}")
            formatted_lines.append(f"{indent}📅 Start Dates: {', '.join(course['start_dates'])}")
            
        elif "courses" in result:
            formatted_lines.append(f"{indent}📚 Available Courses:")
            for course in result["courses"][:2]:  # Show first 2 courses
                formatted_lines.append(f"{indent}  • {course['name']} - {course['price']}")
            if len(result["courses"]) > 2:
                formatted_lines.append(f"{indent}  ... and {len(result['courses']) - 2} more")
                
        elif "payment_options" in result:
            formatted_lines.append(f"{indent}💳 Payment options available")
            if "course_pricing" in result:
                pricing = result["course_pricing"]
                formatted_lines.append(f"{indent}📚 Course: {pricing['course_name']}")
                formatted_lines.append(f"{indent}💰 Price: {pricing['full_price']} (or {pricing['discounted_price']} with discount)")
                
        elif "support_services" in result:
            formatted_lines.append(f"{indent}🎧 24/7 Support Available")
            formatted_lines.append(f"{indent}📞 Multiple contact methods")
            formatted_lines.append(f"{indent}👨‍🏫 Weekly instructor office hours")
            
        elif "certification_details" in result:
            formatted_lines.append(f"{indent}🏆 Industry-recognized certificates")
            formatted_lines.append(f"{indent}📜 Digital badges for portfolios")
            formatted_lines.append(f"{indent}🎓 University credit transfer available")
            
        elif "matching_faqs" in result:
            formatted_lines.append(f"{indent}❓ Found {result['count']} relevant FAQ(s):")
            for faq in result["matching_faqs"][:1]:  # Show first FAQ
                formatted_lines.append(f"{indent}Q: {faq['question']}")
                formatted_lines.append(f"{indent}A: {faq['answer'][:100]}...")
                
        elif "enrollment_steps" in result:
            formatted_lines.append(f"{indent}📝 Enrollment Process:")
            for step in result["enrollment_steps"][:3]:  # Show first 3 steps
                formatted_lines.append(f"{indent}  {step}")
            formatted_lines.append(f"{indent}  ... and {len(result['enrollment_steps']) - 3} more steps")
            
        elif "prerequisites" in result:
            formatted_lines.append(f"{indent}📋 Prerequisites: {', '.join(result['prerequisites'])}")
            if result["recommendations"]:
                formatted_lines.append(f"{indent}💡 Recommendation: {result['recommendations'][0]}")
                
    else:
        formatted_lines.append(f"{indent}{result.get('message', 'Information processed successfully')}")
    
    return "\n".join(formatted_lines)

def show_agent_architecture():
    """Show the agent's architecture and capabilities"""
    
    print("\n🏗️  Agent Architecture Overview")
    print("=" * 60)
    
    print("""
    Student Support Agent
    ├── 🧠 Multi-Model AI Support
    │   ├── Gemini (Google AI Studio) - Default
    │   ├── OpenAI GPT-4o - Optional
    │   └── Anthropic Claude 3.5 - Optional
    │
    ├── 📚 Knowledge Base
    │   ├── Course Catalog (3 courses)
    │   ├── Policy Database (5 policies)
    │   ├── FAQ Repository (8 common questions)
    │   └── Prerequisites & Requirements
    │
    ├── 🛠️  Function Tools (8 tools)
    │   ├── get_course_information()
    │   ├── get_schedule_and_timing()
    │   ├── get_payment_information()
    │   ├── get_support_services()
    │   ├── get_certification_info()
    │   ├── search_faqs()
    │   ├── get_enrollment_process()
    │   └── check_prerequisites()
    │
    └── 🎯 Capabilities
        ├── Natural language understanding
        ├── Context-aware responses
        ├── Multi-turn conversations
        ├── Error handling & fallbacks
        └── Professional, helpful communication
    """)

def main():
    """Main demo function"""
    print("🚀 Starting Student Support Agent Demonstration")
    print("This demo shows the agent's capabilities without requiring API keys")
    
    # Show architecture
    show_agent_architecture()
    
    # Demo tools
    demo_agent_tools()
    
    print("\n✨ Demonstration Complete!")
    print("\nTo interact with the full AI agent:")
    print("1. Configure API keys in student_support_agent/.env")
    print("2. Run: adk web")
    print("3. Select 'student_support_agent' and start chatting!")

if __name__ == "__main__":
    main()
