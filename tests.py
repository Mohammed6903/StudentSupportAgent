"""
Test suite for the Student Support Agent
Tests functionality, tools, and different scenarios
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student_support_agent.config import Config
from student_support_agent.knowledge_base import KnowledgeBase
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

class TestKnowledgeBase(unittest.TestCase):
    """Test the knowledge base functionality"""
    
    def setUp(self):
        self.kb = KnowledgeBase()
    
    def test_get_course_by_id(self):
        """Test retrieving course by ID"""
        course = self.kb.get_course_by_id("py101")
        self.assertIsNotNone(course)
        self.assertEqual(course.name, "Python Programming Fundamentals")
        self.assertEqual(course.price, 299.99)
    
    def test_get_course_by_name(self):
        """Test retrieving course by name"""
        course = self.kb.get_course_by_name("Python")
        self.assertIsNotNone(course)
        self.assertEqual(course.id, "py101")
    
    def test_get_all_courses(self):
        """Test retrieving all courses"""
        courses = self.kb.get_all_courses()
        self.assertEqual(len(courses), 3)
        course_ids = [course.id for course in courses]
        self.assertIn("py101", course_ids)
        self.assertIn("ai101", course_ids)
        self.assertIn("ds201", course_ids)
    
    def test_get_policy(self):
        """Test retrieving policy information"""
        policy = self.kb.get_policy("payment")
        self.assertIsNotNone(policy)
        self.assertEqual(policy.title, "Payment Policy")
    
    def test_search_faqs(self):
        """Test FAQ search functionality"""
        faqs = self.kb.search_faqs("refund")
        self.assertTrue(len(faqs) > 0)
        # Should find the refund-related FAQ
        refund_found = any("refund" in faq["answer"].lower() for faq in faqs)
        self.assertTrue(refund_found)

class TestTools(unittest.TestCase):
    """Test the agent tools functionality"""
    
    def test_get_course_information_by_id(self):
        """Test getting course information by ID"""
        result = get_course_information("py101")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["course"]["name"], "Python Programming Fundamentals")
        self.assertIn("modules", result["course"])
    
    def test_get_course_information_by_name(self):
        """Test getting course information by name"""
        result = get_course_information("Python")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["course"]["id"], "py101")
    
    def test_get_course_information_not_found(self):
        """Test getting course information for non-existent course"""
        result = get_course_information("nonexistent")
        self.assertEqual(result["status"], "multiple_courses")
        self.assertIn("courses", result)
    
    def test_get_schedule_and_timing_specific_course(self):
        """Test getting schedule for specific course"""
        result = get_schedule_and_timing("py101")
        self.assertEqual(result["status"], "success")
        self.assertIn("upcoming_start_dates", result)
        self.assertIn("duration", result)
    
    def test_get_schedule_and_timing_general(self):
        """Test getting general schedule information"""
        result = get_schedule_and_timing("")
        self.assertEqual(result["status"], "success")
        self.assertIn("general_schedule", result)
        self.assertIn("upcoming_courses", result)
    
    def test_get_payment_information_specific_course(self):
        """Test getting payment information for specific course"""
        result = get_payment_information("ai101")
        self.assertEqual(result["status"], "success")
        self.assertIn("course_pricing", result)
        self.assertIn("payment_options", result)
    
    def test_get_payment_information_general(self):
        """Test getting general payment information"""
        result = get_payment_information("")
        self.assertEqual(result["status"], "success")
        self.assertIn("payment_options", result)
        self.assertIn("discounts", result)
    
    def test_get_support_services(self):
        """Test getting support services information"""
        result = get_support_services()
        self.assertEqual(result["status"], "success")
        self.assertIn("support_services", result)
        self.assertIn("contact_methods", result)
    
    def test_get_certification_info(self):
        """Test getting certification information"""
        result = get_certification_info()
        self.assertEqual(result["status"], "success")
        self.assertIn("certification_details", result)
        self.assertIn("completion_requirements", result)
    
    def test_search_faqs_found(self):
        """Test FAQ search with matches"""
        result = search_faqs("refund")
        self.assertEqual(result["status"], "success")
        self.assertIn("matching_faqs", result)
        self.assertTrue(result["count"] > 0)
    
    def test_search_faqs_not_found(self):
        """Test FAQ search with no matches"""
        result = search_faqs("nonexistentquery12345")
        self.assertEqual(result["status"], "no_matches")
        self.assertIn("message", result)
    
    def test_get_enrollment_process_specific_course(self):
        """Test getting enrollment process for specific course"""
        result = get_enrollment_process("py101")
        self.assertEqual(result["status"], "success")
        self.assertIn("enrollment_steps", result)
        self.assertIn("course_specific", result)
    
    def test_get_enrollment_process_general(self):
        """Test getting general enrollment process"""
        result = get_enrollment_process("")
        self.assertEqual(result["status"], "success")
        self.assertIn("enrollment_steps", result)
        self.assertIn("required_information", result)
    
    def test_check_prerequisites_existing_course(self):
        """Test checking prerequisites for existing course"""
        result = check_prerequisites("ai101")
        self.assertEqual(result["status"], "success")
        self.assertIn("prerequisites", result)
        self.assertIn("recommendations", result)
    
    def test_check_prerequisites_nonexistent_course(self):
        """Test checking prerequisites for non-existent course"""
        result = check_prerequisites("nonexistent")
        self.assertEqual(result["status"], "course_not_found")
        self.assertIn("message", result)

class TestConfig(unittest.TestCase):
    """Test the configuration module"""
    
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'})
    def test_config_with_api_key(self):
        """Test configuration with API key set"""
        config = Config()
        available_models = config.get_available_models()
        self.assertIn("gemini", available_models)
    
    def test_model_config_structure(self):
        """Test model configuration structure"""
        config = Config()
        for model_provider in ["gemini", "openai", "anthropic"]:
            model_config = config.MODEL_CONFIGS[model_provider]
            self.assertIn("model_id", model_config)
            self.assertIn("max_tokens", model_config)
            self.assertIn("temperature", model_config)
    
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}, clear=True)
    def test_validate_model(self):
        """Test model validation"""
        config = Config()
        self.assertTrue(config.validate_model("gemini"))
        # Without other API keys, these should fail
        self.assertFalse(config.validate_model("openai"))
        self.assertFalse(config.validate_model("anthropic"))

class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_course_information_flow(self):
        """Test complete flow of getting course information"""
        # Test getting course info
        course_result = get_course_information("py101")
        self.assertEqual(course_result["status"], "success")
        
        # Test getting payment info for the same course
        payment_result = get_payment_information("py101")
        self.assertEqual(payment_result["status"], "success")
        self.assertIn("course_pricing", payment_result)
        
        # Test getting schedule info
        schedule_result = get_schedule_and_timing("py101")
        self.assertEqual(schedule_result["status"], "success")
    
    def test_prerequisites_and_enrollment_flow(self):
        """Test prerequisite checking and enrollment flow"""
        # Check prerequisites for advanced course
        prereq_result = check_prerequisites("ai101")
        self.assertEqual(prereq_result["status"], "success")
        self.assertTrue(len(prereq_result["prerequisites"]) > 0)
        
        # Get enrollment process
        enrollment_result = get_enrollment_process("ai101")
        self.assertEqual(enrollment_result["status"], "success")
        self.assertIn("course_specific", enrollment_result)

def run_tests():
    """Run all tests"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestKnowledgeBase,
        TestTools,
        TestConfig,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)
