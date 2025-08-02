"""
Knowledge base for the Student Support Agent
Contains course information, policies, and FAQs
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Course:
    """Course information structure"""
    id: str
    name: str
    duration_weeks: int
    price: float
    instructor: str
    description: str
    prerequisites: List[str]
    modules: List[str]
    start_dates: List[str]
    
@dataclass
class PolicyInfo:
    """Policy information structure"""
    title: str
    description: str
    details: str

class KnowledgeBase:
    """Knowledge base containing all course and policy information"""
    
    def __init__(self):
        self.courses = self._initialize_courses()
        self.policies = self._initialize_policies()
        self.faqs = self._initialize_faqs()
        
    def _initialize_courses(self) -> Dict[str, Course]:
        """Initialize course catalog"""
        return {
            "py101": Course(
                id="py101",
                name="Python Programming Fundamentals",
                duration_weeks=8,
                price=299.99,
                instructor="Dr. Sarah Chen",
                description="Learn Python programming from scratch with hands-on projects",
                prerequisites=[],
                modules=[
                    "Introduction to Programming",
                    "Variables and Data Types",
                    "Control Structures",
                    "Functions and Modules",
                    "Object-Oriented Programming",
                    "File Handling",
                    "Error Handling",
                    "Final Project"
                ],
                start_dates=["2025-02-15", "2025-03-15", "2025-04-15"]
            ),
            "ai101": Course(
                id="ai101", 
                name="Introduction to Artificial Intelligence",
                duration_weeks=12,
                price=599.99,
                instructor="Prof. Michael Rodriguez",
                description="Comprehensive introduction to AI concepts and practical applications",
                prerequisites=["Basic Python knowledge"],
                modules=[
                    "AI History and Fundamentals",
                    "Machine Learning Basics",
                    "Neural Networks",
                    "Natural Language Processing",
                    "Computer Vision",
                    "Ethics in AI",
                    "AI Project Development",
                    "Industry Applications"
                ],
                start_dates=["2025-02-20", "2025-04-01", "2025-05-15"]
            ),
            "ds201": Course(
                id="ds201",
                name="Data Science and Analytics",
                duration_weeks=10,
                price=449.99,
                instructor="Dr. Emily Johnson",
                description="Master data analysis, visualization, and statistical modeling",
                prerequisites=["Python Programming Fundamentals"],
                modules=[
                    "Data Collection and Cleaning",
                    "Exploratory Data Analysis",
                    "Statistical Analysis",
                    "Data Visualization",
                    "Machine Learning for Data Science",
                    "Time Series Analysis",
                    "Big Data Tools",
                    "Capstone Project"
                ],
                start_dates=["2025-03-01", "2025-04-15", "2025-06-01"]
            )
        }
    
    def _initialize_policies(self) -> Dict[str, PolicyInfo]:
        """Initialize policy information"""
        return {
            "payment": PolicyInfo(
                title="Payment Policy",
                description="Flexible payment options available",
                details="""
                - Full payment: Get 10% discount
                - Monthly installments: Available for courses over $300
                - Refund policy: 30-day money-back guarantee
                - Payment methods: Credit card, PayPal, bank transfer
                - Late payment: 7-day grace period, then $25 fee
                """
            ),
            "schedule": PolicyInfo(
                title="Class Schedule and Attendance",
                description="Flexible learning with live and recorded sessions",
                details="""
                - Live sessions: 2 times per week, 2 hours each
                - Recorded sessions: Available 24/7 for enrolled students
                - Attendance: Not mandatory but recommended for live sessions
                - Makeup sessions: Available for missed live classes
                - Time zones: Sessions offered in EST, PST, and GMT
                """
            ),
            "support": PolicyInfo(
                title="Student Support Services",
                description="Comprehensive support throughout your learning journey",
                details="""
                - 24/7 chat support for technical issues
                - Weekly office hours with instructors
                - Peer study groups and forums
                - Career counseling and job placement assistance
                - Learning disability accommodations available
                """
            ),
            "certification": PolicyInfo(
                title="Certification and Credits",
                description="Industry-recognized certificates upon completion",
                details="""
                - Certificate of completion for all finished courses
                - Digital badges for skill verification
                - Transcript available upon request
                - Credit transfer: Partnerships with select universities
                - Continuing education units (CEUs) provided
                """
            ),
            "technical": PolicyInfo(
                title="Technical Requirements",
                description="System requirements for optimal learning experience",
                details="""
                - Computer: Windows 10+, macOS 10.14+, or Linux
                - Internet: Stable broadband connection (5+ Mbps)
                - Browser: Chrome, Firefox, Safari, or Edge (latest versions)
                - Software: Provided free for enrolled students
                - Mobile: iOS/Android apps available for supplementary learning
                """
            )
        }
    
    def _initialize_faqs(self) -> List[Dict[str, str]]:
        """Initialize frequently asked questions"""
        return [
            {
                "question": "How do I access course materials?",
                "answer": "Course materials are available through our learning management system. You'll receive login credentials via email after enrollment."
            },
            {
                "question": "Can I switch between courses?",
                "answer": "Course switches are allowed within the first two weeks of enrollment. Contact support for assistance with the transfer process."
            },
            {
                "question": "What if I fall behind in coursework?",
                "answer": "We offer flexible pacing options. You can extend your course duration by up to 4 weeks at no additional cost. Additional extensions are available for a small fee."
            },
            {
                "question": "Are there group projects?",
                "answer": "Most courses include collaborative projects to enhance learning. You'll be matched with peers based on timezone and availability preferences."
            },
            {
                "question": "How do I contact my instructor?",
                "answer": "Instructors are available through course forums, weekly office hours, and email. Response time is typically within 24 hours on weekdays."
            },
            {
                "question": "Is financial aid available?",
                "answer": "We offer need-based scholarships and payment plans. Contact our financial aid office to discuss available options."
            },
            {
                "question": "Can I get a refund?",
                "answer": "Full refunds are available within 30 days of enrollment if you've completed less than 25% of the course content."
            },
            {
                "question": "What happens after course completion?",
                "answer": "You'll receive a certificate, have lifetime access to course materials, and get invitations to alumni networking events and advanced courses."
            }
        ]
    
    def get_course_by_id(self, course_id: str) -> Course:
        """Get course information by ID"""
        return self.courses.get(course_id.lower())
    
    def get_course_by_name(self, course_name: str) -> Course:
        """Get course information by name (fuzzy matching)"""
        course_name_lower = course_name.lower()
        for course in self.courses.values():
            if course_name_lower in course.name.lower():
                return course
        return None
    
    def get_all_courses(self) -> List[Course]:
        """Get all available courses"""
        return list(self.courses.values())
    
    def get_policy(self, policy_type: str) -> PolicyInfo:
        """Get policy information by type"""
        return self.policies.get(policy_type.lower())
    
    def get_all_policies(self) -> List[PolicyInfo]:
        """Get all policy information"""
        return list(self.policies.values())
    
    def search_faqs(self, query: str) -> List[Dict[str, str]]:
        """Search FAQs by query"""
        query_lower = query.lower()
        matching_faqs = []
        
        for faq in self.faqs:
            if (query_lower in faq["question"].lower() or 
                query_lower in faq["answer"].lower()):
                matching_faqs.append(faq)
        
        return matching_faqs
    
    def get_upcoming_start_dates(self, course_id: str = None) -> Dict[str, List[str]]:
        """Get upcoming course start dates"""
        if course_id:
            course = self.get_course_by_id(course_id)
            return {course.name: course.start_dates} if course else {}
        
        return {course.name: course.start_dates for course in self.courses.values()}
