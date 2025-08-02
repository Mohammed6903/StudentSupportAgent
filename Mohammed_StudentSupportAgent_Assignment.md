# Mohammed_StudentSupportAgent_Assignment

## Agent Objective

Create an intelligent Student Support Agent that acts as the first point of contact for students seeking information about online courses. The agent should provide comprehensive assistance with course inquiries, enrollment guidance, payment options, scheduling information, and general support services, delivering a seamless and helpful experience that guides students through their educational journey.

## Input

The agent accepts natural language queries from students covering various aspects of their educational needs:

### Course Information Queries
- "What courses do you offer?"
- "Tell me about the Python programming course"
- "What's included in the AI course curriculum?"
- "How long is the Data Science program?"

### Enrollment & Prerequisites
- "How do I enroll in the Python course?"
- "What are the prerequisites for the AI course?"
- "Can I switch between courses after enrollment?"

### Scheduling & Timing
- "When does the next Data Science course start?"
- "What are the class schedules like?"
- "Are classes recorded?"

### Payment & Financial
- "What are the payment options?"
- "Do you offer payment plans?"
- "What's your refund policy?"
- "Is financial aid available?"

### Support & Certification
- "What support services are available?"
- "How do I get certified after completing a course?"
- "What are the technical requirements?"

## Workflow

### 1. Agent Initialization
**Environment Setup**
- Load configuration from environment variables
- Validate API keys for available AI models (Gemini, OpenAI, Anthropic)
- Initialize knowledge base with course catalog and policies

**Model Selection Process**
- Primary: Gemini (Google AI Studio) - Default choice
- Secondary: OpenAI GPT-4o (if API key available)
- Tertiary: Anthropic Claude 3.5 Sonnet (if API key available)
- Automatic fallback to first available model

**Knowledge Base Loading**
- Course catalog (Python, AI, Data Science courses)
- Policy database (payment, schedules, support, certification)
- FAQ repository with common student questions
- Prerequisites and enrollment requirements

### 2. Query Processing Pipeline
**Input Reception & Analysis**
- Receive student's natural language query
- AI model analyzes intent and determines required information
- Context awareness for follow-up questions

**Tool Selection & Execution**
The agent has access to 8 specialized tools:
- `get_course_information()`: Detailed course data and descriptions
- `get_schedule_and_timing()`: Class schedules and start dates
- `get_payment_information()`: Payment options and pricing
- `get_support_services()`: Available support channels
- `get_certification_info()`: Certificate requirements
- `search_faqs()`: Search frequently asked questions
- `get_enrollment_process()`: Step-by-step enrollment guide
- `check_prerequisites()`: Prerequisite validation

**Response Generation**
- Synthesize information from multiple tools if needed
- Create comprehensive, structured responses
- Include relevant follow-up suggestions
- Maintain friendly, professional tone

### 3. Error Handling & Fallbacks
- Graceful handling of unknown queries
- Redirection to human support when appropriate
- Comprehensive logging for debugging and improvement

### Technology Stack
- **Framework**: Google Agent Development Kit (ADK)
- **AI Models**: Multi-provider support (Gemini, OpenAI, Anthropic)
- **Architecture**: Modular Python design with type hints
- **Testing**: Comprehensive test suite with unit and integration tests
- **Configuration**: Environment-based configuration management

## Sample Prompt(s)

### Prompt 1: Course Inquiry
**Student Query**: "I'm interested in learning programming but I'm a complete beginner. What course would you recommend and how much does it cost?"

### Prompt 2: Enrollment Process
**Student Query**: "I want to enroll in the AI course. What are the prerequisites and when can I start?"

### Prompt 3: Payment & Support
**Student Query**: "Do you offer payment plans for the Data Science course? Also, what kind of support do you provide during the course?"

## Sample Output

### Response to Course Inquiry Prompt

**Agent Response**:

"Perfect! For complete beginners, I highly recommend our **Python Programming Fundamentals** course. It's specifically designed for people with no prior programming experience.

**Course Details:**
- **Course ID**: py101
- **Duration**: 8 weeks  
- **Price**: $299.99 (or $269.99 with 10% full payment discount)
- **Instructor**: Dr. Sarah Chen
- **Prerequisites**: None - completely beginner-friendly!

**What You'll Learn:**
✓ Introduction to Programming concepts
✓ Variables and Data Types
✓ Control Structures (loops, conditions)
✓ Functions and Modules
✓ Object-Oriented Programming basics
✓ File Handling
✓ Error Handling
✓ Final hands-on project

**Upcoming Start Dates:**
- February 15, 2025
- March 15, 2025
- April 15, 2025

**Flexible Schedule:**
- Live sessions: 2 times per week (2 hours each)
- All sessions are recorded for 24/7 access
- Multiple timezone options available

**Payment Options:**
- Full payment: $269.99 (10% discount)
- 3-month installment plan: $100/month
- 30-day money-back guarantee

This course will give you a solid foundation in programming and prepare you for more advanced courses like our AI or Data Science programs. 

Would you like me to help you with the enrollment process, or do you have any other questions about the course?"

### Response to Enrollment Process Prompt

**Agent Response**:

"Great choice! The **Introduction to Artificial Intelligence** course is very popular. Let me help you with the enrollment details.

**Prerequisites Check:**
⚠️ This course requires: **Basic Python knowledge**

Since you're interested in the AI course, I recommend:
1. Complete our Python Programming Fundamentals first, OR
2. Demonstrate Python proficiency through our quick assessment

**Enrollment Process:**
1. **Course Selection**: AI course (ai101) ✓
2. **Prerequisites**: Verify Python knowledge
3. **Choose Start Date**: 
   - February 20, 2025
   - April 1, 2025  
   - May 15, 2025
4. **Complete Application**: Online form with educational background
5. **Payment**: Select from available options
6. **Confirmation**: Receive access credentials via email
7. **Orientation**: Join pre-course session
8. **Start Learning**: Begin your AI journey!

**Course Investment:**
- **Price**: $599.99
- **Duration**: 12 weeks
- **Instructor**: Prof. Michael Rodriguez
- **Includes**: All software, materials, and certification

**Quick Enrollment Options:**
- **Option A**: Enroll in Python course first (8 weeks), then AI course
- **Option B**: Take our Python assessment for direct AI course entry

**Processing Time**: 24-48 hours for prerequisite verification

Would you like me to check if you're ready for the AI course directly, or would you prefer to start with Python fundamentals? I can also explain our assessment process!"

---

**Technologies Used**: Google ADK, Python, Multi-AI Model Support (Gemini/OpenAI/Anthropic)
**Architecture**: Professional modular design with comprehensive testing
**Estimated Development Time**: 3 hours
