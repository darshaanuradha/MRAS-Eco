from django.test import TestCase
from .models import Patient
from doctors.models import Doctor
from consultation.models import Consultation

class PatientModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            contact="1234567890",
            address="123 Street"
        )
        self.doctor = Doctor.objects.create(
            full_name="Dr. Smith",
            specialization="General Practitioner",
            phone_number="0987654321",
            email="smith@example.com"
        )

    def test_patient_properties(self):
        self.assertEqual(self.patient.full_name, "John Doe")
        self.assertEqual(str(self.patient), "John Doe")

    def test_consultation_str(self):
        consultation = Consultation.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            diagnosis="Flu",
            notes="Rest and fluids."
        )
        self.assertIn("John Doe", str(consultation))
