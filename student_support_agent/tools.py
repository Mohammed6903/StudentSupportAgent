"""
Tools and functions for the Student Support Agent
Provides various capabilities for answering student queries
"""

from typing import Dict, List, Any, Optional
import json
from datetime import datetime, timedelta
from .knowledge_base import KnowledgeBase, Course, PolicyInfo

# Initialize knowledge base
kb = KnowledgeBase()

def get_course_information(query: str) -> Dict[str, Any]:
    """
    Retrieves detailed information about courses based on student query.
    
    Args:
        query (str): Student's query about a course (can include course name, ID, or general topic)
        
    Returns:
        Dict[str, Any]: Course information including details, pricing, schedule, etc.
    """
    
    # Try to find course by ID first
    course = kb.get_course_by_id(query)
    
    # If not found, try by name
    if not course:
        course = kb.get_course_by_name(query)
    
    # If still not found, return all courses
    if not course:
        courses = kb.get_all_courses()
        return {
            "status": "multiple_courses",
            "message": f"I found multiple courses that might interest you. Here are all available courses:",
            "courses": [
                {
                    "id": c.id,
                    "name": c.name,
                    "duration": f"{c.duration_weeks} weeks",
                    "price": f"${c.price}",
                    "instructor": c.instructor,
                    "description": c.description,
                    "start_dates": c.start_dates
                }
                for c in courses
            ]
        }
    
    return {
        "status": "success",
        "course": {
            "id": course.id,
            "name": course.name,
            "duration": f"{course.duration_weeks} weeks",
            "price": f"${course.price}",
            "instructor": course.instructor,
            "description": course.description,
            "prerequisites": course.prerequisites if course.prerequisites else ["None"],
            "modules": course.modules,
            "start_dates": course.start_dates
        }
    }

def get_schedule_and_timing(course_query: str = "") -> Dict[str, Any]:
    """
    Provides information about course schedules, timing, and upcoming start dates.
    
    Args:
        course_query (str): Optional specific course to get schedule for
        
    Returns:
        Dict[str, Any]: Schedule information and upcoming dates
    """
    
    if course_query:
        course = kb.get_course_by_id(course_query) or kb.get_course_by_name(course_query)
        if course:
            return {
                "status": "success",
                "course_name": course.name,
                "duration": f"{course.duration_weeks} weeks",
                "upcoming_start_dates": course.start_dates,
                "schedule_details": "Classes are held twice weekly (2 hours each), with both live and recorded sessions available."
            }
    
    # Return general schedule information
    schedule_policy = kb.get_policy("schedule")
    upcoming_dates = kb.get_upcoming_start_dates()
    
    return {
        "status": "success",
        "general_schedule": schedule_policy.details,
        "upcoming_courses": upcoming_dates,
        "note": "All times are flexible with recorded sessions available 24/7"
    }

def get_payment_information(course_query: str = "") -> Dict[str, Any]:
    """
    Provides payment options, pricing, and financial policies.
    
    Args:
        course_query (str): Optional specific course to get pricing for
        
    Returns:
        Dict[str, Any]: Payment and pricing information
    """
    
    payment_policy = kb.get_policy("payment")
    
    result = {
        "status": "success",
        "payment_options": payment_policy.details,
        "payment_methods": ["Credit Card", "PayPal", "Bank Transfer"],
        "discounts": {
            "full_payment": "10% discount for full upfront payment",
            "early_bird": "5% discount for enrollment 30 days before start date"
        }
    }
    
    if course_query:
        course = kb.get_course_by_id(course_query) or kb.get_course_by_name(course_query)
        if course:
            installment_available = course.price > 300
            result["course_pricing"] = {
                "course_name": course.name,
                "full_price": f"${course.price}",
                "discounted_price": f"${course.price * 0.9:.2f}",
                "installment_available": installment_available,
                "monthly_payment": f"${course.price / 3:.2f} (3 months)" if installment_available else "Not available"
            }
    
    return result

def get_support_services() -> Dict[str, Any]:
    """
    Provides information about available student support services.
    
    Returns:
        Dict[str, Any]: Details about support services available to students
    """
    
    support_policy = kb.get_policy("support")
    technical_policy = kb.get_policy("technical")
    
    return {
        "status": "success",
        "support_services": support_policy.details,
        "technical_requirements": technical_policy.details,
        "contact_methods": {
            "chat": "24/7 live chat support",
            "email": "support@scoreazy.edu",
            "phone": "1-800-SCOREAZY",
            "office_hours": "Weekly with instructors"
        }
    }

def get_certification_info() -> Dict[str, Any]:
    """
    Provides information about certificates, credits, and completion requirements.
    
    Returns:
        Dict[str, Any]: Certification and credit information
    """
    
    cert_policy = kb.get_policy("certification")
    
    return {
        "status": "success",
        "certification_details": cert_policy.details,
        "completion_requirements": {
            "attendance": "Complete 80% of course modules",
            "assignments": "Submit all required assignments",
            "final_project": "Complete capstone project with passing grade",
            "participation": "Active participation in discussions (recommended)"
        },
        "certificate_benefits": [
            "Industry-recognized completion certificate",
            "Digital badges for LinkedIn and portfolios",
            "Transcript available for university credit transfer",
            "Access to alumni network and job placement services"
        ]
    }

def search_faqs(question: str) -> Dict[str, Any]:
    """
    Searches frequently asked questions for relevant information.
    
    Args:
        question (str): Student's question to search for in FAQs
        
    Returns:
        Dict[str, Any]: Matching FAQ entries
    """
    
    matching_faqs = kb.search_faqs(question)
    
    if not matching_faqs:
        return {
            "status": "no_matches",
            "message": "I couldn't find specific FAQs matching your question, but I can help you with course information, schedules, payments, or support services. Please feel free to ask!"
        }
    
    return {
        "status": "success",
        "matching_faqs": matching_faqs,
        "count": len(matching_faqs)
    }

def get_enrollment_process(course_query: str = "") -> Dict[str, Any]:
    """
    Explains the enrollment process and requirements.
    
    Args:
        course_query (str): Optional specific course for enrollment info
        
    Returns:
        Dict[str, Any]: Enrollment process and requirements
    """
    
    enrollment_steps = [
        "Browse course catalog and select your desired course",
        "Check prerequisites and ensure you meet requirements", 
        "Choose your preferred start date",
        "Complete the online enrollment form",
        "Select payment option and complete payment",
        "Receive confirmation email with access credentials",
        "Join the pre-course orientation session",
        "Begin your learning journey!"
    ]
    
    result = {
        "status": "success",
        "enrollment_steps": enrollment_steps,
        "required_information": [
            "Full name and contact details",
            "Educational background",
            "Payment information",
            "Learning goals and expectations"
        ],
        "processing_time": "Instant approval for most courses, 24-48 hours for courses with prerequisites"
    }
    
    if course_query:
        course = kb.get_course_by_id(course_query) or kb.get_course_by_name(course_query)
        if course:
            result["course_specific"] = {
                "course_name": course.name,
                "prerequisites": course.prerequisites if course.prerequisites else ["None"],
                "next_start_dates": course.start_dates,
                "price": f"${course.price}",
                "enrollment_deadline": "1 week before start date"
            }
    
    return result

def check_prerequisites(course_query: str, student_background: str = "") -> Dict[str, Any]:
    """
    Checks course prerequisites and provides guidance.
    
    Args:
        course_query (str): Course to check prerequisites for
        student_background (str): Optional student's educational background
        
    Returns:
        Dict[str, Any]: Prerequisites information and recommendations
    """
    
    course = kb.get_course_by_id(course_query) or kb.get_course_by_name(course_query)
    
    if not course:
        return {
            "status": "course_not_found",
            "message": f"I couldn't find a course matching '{course_query}'. Please check the course name or ID."
        }
    
    result = {
        "status": "success",
        "course_name": course.name,
        "prerequisites": course.prerequisites if course.prerequisites else ["None - This is a beginner-friendly course"],
        "recommendations": []
    }
    
    # Add recommendations based on prerequisites
    if course.prerequisites:
        if "Python" in course.prerequisites[0]:
            result["recommendations"].append("Consider taking 'Python Programming Fundamentals' first if you're new to programming")
        result["recommendations"].append("Review prerequisite topics before starting the course")
        result["recommendations"].append("Contact support if you're unsure about your readiness")
    else:
        result["recommendations"].append("This course is designed for beginners - no prior experience required!")
    
    return result
