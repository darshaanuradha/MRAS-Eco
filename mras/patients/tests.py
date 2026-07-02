from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from patients.models import Patient 

class PatientViewTests(TestCase):
    def setUp(self):
        # Create a test user and log them in since all views are @login_required
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create a sample patient
        self.patient = Patient.objects.create(
            full_name='Test Patient',
            gender='Male',
            phone_number='1234567890',
            email='test@example.com'
        )

    def test_patient_list_view(self):
        response = self.client.get(reverse('patients:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/patient_list.html')
        self.assertContains(response, 'Test Patient')

    def test_patient_create_view(self):
        data = {
            'full_name': 'New Patient',
            'gender': 'Female',
            'is_active': True
        }
        response = self.client.post(reverse('patients:create'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        self.assertTrue(Patient.objects.filter(full_name='New Patient').exists())

    def test_patient_update_view(self):
        data = {
            'full_name': 'Updated Patient',
            'gender': 'Male',
            'is_active': True
        }
        response = self.client.post(reverse('patients:edit', args=[self.patient.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.full_name, 'Updated Patient')

    def test_patient_delete_view(self):
        response = self.client.post(reverse('patients:delete', args=[self.patient.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Patient.objects.filter(pk=self.patient.pk).exists())

