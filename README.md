# Student Support Agent - Scoreazy Assignment

A comprehensive AI agent built with Google ADK to handle student inquiries about online courses, providing support for enrollment, schedules, payments, and general assistance.

## 🎯 Agent Objective

Create an intelligent Student Support Agent that can:
- Answer questions about course catalog, pricing, and schedules
- Provide enrollment guidance and prerequisites information
- Explain payment options and policies
- Offer information about support services and certification
- Handle FAQs and redirect complex queries appropriately

## 📋 Features

### Multi-Model Support
- **Gemini** (Default): Google's latest AI model via Google AI Studio
- **OpenAI**: GPT-4o via OpenAI API  
- **Anthropic**: Claude 3.5 Sonnet via Anthropic API
- Automatic fallback to available models

### Comprehensive Knowledge Base
- Course catalog with detailed information
- Policy database (payment, schedules, support, certification)
- Frequently Asked Questions
- Prerequisites and enrollment requirements

### Professional Architecture
- Modular design with clear separation of concerns
- Configuration management with environment variables
- Comprehensive error handling and logging
- Extensive test suite
- Type hints and documentation

## 🚀 Input

The agent accepts natural language queries from students, such as:
- "What courses do you offer?"
- "Tell me about the Python programming course"
- "What are the payment options for the AI course?"
- "When does the next Data Science course start?"
- "What are the prerequisites for the AI course?"
- "How do I get certified?"
- "Can I get a refund?"

## 🔄 Workflow

### Agent Initialization
1. **Environment Setup**: Load API keys and configuration
2. **Model Selection**: Choose available model (Gemini → OpenAI → Anthropic)
3. **Knowledge Base**: Initialize course catalog and policies
4. **Tool Registration**: Set up function tools for data retrieval
5. **Agent Creation**: Configure ADK agent with instructions and tools

### Query Processing
1. **Input Reception**: Receive student question
2. **Intent Analysis**: AI determines what information is needed
3. **Tool Selection**: Choose appropriate tools (course info, payment, etc.)
4. **Data Retrieval**: Execute tools to get relevant information
5. **Response Generation**: Create comprehensive, helpful response
6. **Error Handling**: Graceful fallback for edge cases

### Available Tools
- `get_course_information()`: Course details, pricing, descriptions
- `get_schedule_and_timing()`: Class schedules and start dates
- `get_payment_information()`: Payment options and policies
- `get_support_services()`: Available support channels
- `get_certification_info()`: Certificate and completion requirements
- `search_faqs()`: Search frequently asked questions
- `get_enrollment_process()`: Step-by-step enrollment guide
- `check_prerequisites()`: Prerequisite validation and recommendations

## 💻 Installation & Setup

### Prerequisites
- Python 3.9+
- Conda environment named 'adk'
- At least one API key (Gemini recommended)

### Setup Instructions

1. **Environment Setup**
```bash
# Activate the ADK conda environment
conda activate adk

# Navigate to project directory
cd /home/mohammed/dev/Assignments/Scoreazy
```

2. **Install Dependencies**
```bash
# Install required packages
pip install google-adk litellm openai anthropic python-dotenv
```

3. **Configure API Keys**
Edit `student_support_agent/.env`:
```env
# Gemini (Recommended - Free tier available)
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE

# OpenAI (Optional)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic (Optional) 
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Default model
DEFAULT_MODEL=gemini
```

## 🏃‍♂️ Running the Agent

### Method 1: ADK Web Interface (Recommended)
```bash
# Run the interactive web interface
adk web
```
- Open http://localhost:8000 in your browser
- Select "student_support_agent" from the dropdown
- Start chatting with the agent

### Method 2: Demo Script
```bash
# Run sample conversations
python demo.py

# Run interactive mode
python demo.py interactive
```

### Method 3: Python API
```python
from student_support_agent.agent import create_agent

# Create agent
agent = create_agent()

# Chat with agent
response = agent.chat("What courses do you offer?")
print(response)
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
python tests.py
```

Tests cover:
- Knowledge base functionality
- Tool operations
- Configuration management  
- Integration scenarios
- Error handling

## 📊 Sample Prompts

### Course Information
```
"Tell me about your programming courses"
"What's included in the AI course?"
"How long is the Data Science program?"
```

### Enrollment & Prerequisites  
```
"How do I enroll in the Python course?"
"What are the prerequisites for AI course?"
"When can I start the Data Science program?"
```

### Payment & Policies
```
"What are the payment options?"
"Do you offer payment plans?"
"What's your refund policy?"
```

### Support & Certification
```
"What support is available for students?"
"How do I get certified?"
"What are the technical requirements?"
```

## 📝 Sample Output

**User**: "Tell me about the Python course"

**Agent**: "I'd be happy to tell you about our Python Programming Fundamentals course!

**Course Details:**
- **Course ID**: py101
- **Duration**: 8 weeks
- **Price**: $299.99 (or $269.99 with full payment discount)
- **Instructor**: Dr. Sarah Chen
- **Prerequisites**: None - perfect for beginners!

**What You'll Learn:**
- Introduction to Programming
- Variables and Data Types  
- Control Structures
- Functions and Modules
- Object-Oriented Programming
- File Handling
- Error Handling
- Final Project

**Upcoming Start Dates:**
- February 15, 2025
- March 15, 2025  
- April 15, 2025

**Schedule**: Classes are held twice weekly (2 hours each) with both live and recorded sessions available for flexibility.

Would you like information about enrollment, payment options, or have any other questions about this course?"

## 🏗️ Architecture

```
student_support_agent/
├── __init__.py              # Package initialization
├── agent.py                 # Main agent class and ADK integration
├── config.py                # Configuration and model management
├── knowledge_base.py        # Course catalog and policies
├── tools.py                 # Agent function tools
└── .env                     # Environment variables

Root Files:
├── demo.py                  # Demonstration script
├── tests.py                 # Comprehensive test suite
└── assignment.txt           # Original assignment requirements
```

## 🔧 Configuration

### Model Selection Priority
1. Specified model parameter
2. DEFAULT_MODEL environment variable
3. First available model based on API keys
4. Fallback to basic Gemini model

### Environment Variables
- `GOOGLE_API_KEY`: Gemini API key from Google AI Studio
- `OPENAI_API_KEY`: OpenAI API key  
- `ANTHROPIC_API_KEY`: Anthropic API key
- `DEFAULT_MODEL`: Preferred model (gemini/openai/anthropic)
- `GOOGLE_GENAI_USE_VERTEXAI`: Use Vertex AI instead of AI Studio

## 🎯 Assignment Requirements Met

✅ **Agent Objective**: Clear student support role with comprehensive assistance

✅ **Input**: Natural language queries from students about courses and services  

✅ **Workflow**: 
- Model selection and configuration
- Query processing with tool selection
- Data retrieval from knowledge base
- Response generation with error handling

✅ **Sample Prompts**: Multiple examples covering all major use cases

✅ **Sample Output**: Detailed, helpful responses with structured information

## 🚀 Advanced Features

### Professional Code Quality
- Type hints throughout codebase
- Comprehensive error handling
- Logging and debugging support
- Modular, maintainable architecture

### Testing & Validation
- Unit tests for all components
- Integration tests for workflows
- Mock testing for external dependencies
- Automated test suite execution

### Multi-Model Support
- Seamless switching between AI providers
- Fallback mechanisms for reliability
- Provider-specific optimizations
- Cost-effective model selection

### Production Ready
- Environment-based configuration
- Secure API key management  
- Scalable architecture
- Comprehensive documentation

## 📈 Estimated Effort

**Total Time**: ~3 hours

**Breakdown**:
- Research & Planning: 30 minutes
- Architecture Design: 30 minutes  
- Implementation: 90 minutes
- Testing & Documentation: 30 minutes

## 🛠️ Troubleshooting

### Common Issues

1. **"No API keys configured"**
   - Add at least one API key to `.env` file
   - Ensure environment variables are loaded correctly

2. **"Agent not found in dropdown"**  
   - Run `adk web` from the project root directory
   - Check that `__init__.py` properly imports the agent

3. **"Model not available"**
   - Verify API key is valid and has quota
   - Check internet connection
   - Try switching to different model provider

### Getting Help
- Check the test suite output for detailed error information
- Review logs for debugging information
- Ensure all dependencies are properly installed
- Verify conda environment is activated

## 📄 License

This project is created as part of the Scoreazy internship assignment.

---

**Built with ❤️ using Google ADK, supporting multiple AI providers for maximum flexibility and reliability.**
