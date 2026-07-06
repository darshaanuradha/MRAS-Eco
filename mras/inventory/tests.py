from django.test import TestCase
from .models import Medicine

class MedicineModelTest(TestCase):
    
    def setUp(self):
        """
        The setUp method runs BEFORE every single test. 
        We use it to create dummy data in our temporary test database.
        """
        Medicine.objects.create(
            name="Panadol", 
            generic_name="Paracetamol", 
            min_stock_level=15
        )

    def test_medicine_was_created_correctly(self):
        """
        Test methods MUST start with the word 'test_'. 
        Here we pull the data and check if it matches what we expect.
        """
        # 1. Get the dummy record we created in setUp
        med = Medicine.objects.get(name="Panadol")
        
        # 2. Assert (verify) that the generic name matches
        self.assertEqual(med.generic_name, "Paracetamol")
        
        # 3. Assert that the default max_stock_level (500) was applied automatically
        self.assertEqual(med.max_stock_level, 500)