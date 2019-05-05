from rasa_core_sdk import Action
from cache_client import cache
from rasa_core_sdk.events import Restarted

class ActionGreetingIntroduction(Action):
    def name(self):
        return "action_greeting_introduction"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'https://storage.googleapis.com/bluelogic-images/RequestAppointment.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Insurance Coverage', 'description': 'Check if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/InsuranceCoverage.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/CallbackRequest.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers!", 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/PromotionsandOffers.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/VaccinationCalculators.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Share any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/MainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionRealHumanBot(Action):
    def name(self):
        return "action_real_human_bot"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionPromotionsOffersSelected(Action):
    def name(self):
        return "action_promotions_&_offers_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Woman 34 Clinic', 'description': 'Free gynaecology consultations and tailor-made packages for you.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/promotions/2.jpg', 'buttons': [{'title': 'Know More', 'payload': '/woman_thirty_four'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionLocateACentreSelected(Action):
    def name(self):
        return "action_locate_a_centre_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'AVIVO Hospitals', 'description': 'Get directions to different AVIVO Hospitals.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/AvivoHospitals/AvivoHospital.png', 'buttons': [{'title': 'AVIVO Hospitals', 'payload': '/locate1'}]}, {'label': 'AVIVO Clinics', 'description': 'Find your way to an AVIVO Clinic of your choice.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/AvivoClinics/AvivoClinics.jpg', 'buttons': [{'title': 'AVIVO Clinics', 'payload': '/locate2'}]}, {'label': 'Primacare Clinics', 'description': 'Find the closest Primacare Clinics to you!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/PrimecareClinics/PrimecareClinics.png', 'buttons': [{'title': 'Primacare Clinics', 'payload': '/locate3'}]}, {'label': 'Aesthetica Clinics', 'description': 'Take a look at the closest Aesthetica Clinics to you.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres/AestheticaClinic.jpg', 'buttons': [{'title': 'Aesthetica Clinics', 'payload': '/locate4'}]}, {'label': 'Dermalase Clinics', 'description': 'Locate the nearest Dermalase Clinics.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres/DermalaseClinic.jpg', 'buttons': [{'title': 'Dermalase Clinics', 'payload': '/locate5'}]}, {'label': 'Al Barsha Clinic', 'description': 'Get an idea of how long it would take you to reach the Al Barsha Clinic.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres/AlBarshaClinic.jpg', 'buttons': [{'title': 'Al Barsha Clinic', 'payload': '/locate6'}]}, {'label': 'Muhaisna Centre', 'description': 'Check how long it would take to reach the Muhaisna Specialist Medical Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres//MuhaisnaSpecialist.jpg', 'buttons': [{'title': 'Muhaisna Centre', 'payload': '/locate7'}]}, {'label': 'Primacare Pharmacies', 'description': 'Locate the closest Primacare Pharmacy to you.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/PrimecarePharmacy/PrimecarePharmacy.png', 'buttons': [{'title': 'Primacare Pharmacies', 'payload': '/locate8'}]}, {'label': "Dr Michael's Clinic", 'description': 'Find out how far away you are from Dr. Michaels Dental Clinic.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres/DrMichaels.jpg', 'buttons': [{'title': "Dr Michael's Clinic", 'payload': '/locate9'}]}, {'label': 'NNMC Branch', 'description': 'Find out the distance between you & the NNMC Branch.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/AvivoCentres/OtherCentres/NNMC.jpg', 'buttons': [{'title': 'NNMC Branch', 'payload': '/locate10'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionLocateSelectedLocateACentre(Action):
    def name(self):
        return "action_locate_selected_locate_a_centre"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Would you prefer selecting from our available locations or sharing your location with me?', 'replies': [{'title': 'Select Location', 'payload': '/enter_details'}, {'title': 'Share Location', 'payload': '/share_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionShareLocationSelectedLocateACentre(Action):
    def name(self):
        return "action_share_location_selected_locate_a_centre"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can you please share your current location?', 'replies': [{'title': 'Share Location', 'payload': '/user_shared_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionEnterManuallySelected(Action):
    def name(self):
        return "action_enter_manually_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Which Emirate are you looking for a centre in?', 'replies': [{'title': 'Abu Dhabi', 'payload': '/emiratead'}, {'title': 'Dubai', 'payload': '/emiratedubai'}, {'title': 'Sharjah', 'payload': '/emiratesharjah'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionHospitalSelectedManualShareLocations(Action):
    def name(self):
        return "action_hospital_selected_manual_&_share_locations"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_locate_centre'}, {'title': 'No', 'payload': '/no_locate_centre'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionRequestAppointmentSelected(Action):
    def name(self):
        return "action_request_appointment_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'I can help you find a doctor or provide you a list of centres based on their specializations. How you would like to proceed?', 'replies': [{'title': 'Doctor', 'payload': '/doctor'}, {'title': 'Specialization', 'payload': '/specialization'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionSpecializationSelected(Action):
    def name(self):
        return "action_specialization_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'General Medicine', 'description': 'Our General Clinic department provides the most comprehensive family healthcare.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/GeneralMedicine.png', 'buttons': [{'title': 'General Medicine', 'payload': '/specialization_selected'}]}, {'label': 'Homeopathy', 'description': 'A scientific & therapeutic system of medicine provided by AVIVO Centres.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Homeopathy.png', 'buttons': [{'title': 'Homeopathy', 'payload': '/specialization_selected'}]}, {'label': 'Neurology', 'description': 'Innovative treatments for various neurological conditions.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Neurology.png', 'buttons': [{'title': 'Neurology', 'payload': '/specialization_selected'}]}, {'label': 'Dental Care', 'description': 'View some of the best Dental Hospitals in Dubai, Abu Dhabi & Sharjah.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Dental.png', 'buttons': [{'title': 'Dental Care', 'payload': '/specialization_selected'}]}, {'label': 'Cardiology', 'description': 'Early prevention & rapid diagnosis for cardiovascular care.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Cardiology.png', 'buttons': [{'title': 'Cardiology', 'payload': '/specialization_selected'}]}, {'label': 'Gynaecology', 'description': 'Various gynaecology treatments for diverse medical needs.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Gynaecology.png', 'buttons': [{'title': 'Button 1', 'payload': '/specialization_selected'}]}, {'label': 'Internal Medicine', 'description': 'Get high-quality healthcare services with our Internal Medicine Team.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/InternalMedicine.png', 'buttons': [{'title': 'Internal Medicine', 'payload': '/specialization_selected'}]}, {'label': 'Ear, Nose & Throat', 'description': 'Our ENT department treats the nose, sinuses, throat & hearing disorders.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/EarNoseThroat.png', 'buttons': [{'title': 'Ear, Nose & Throat', 'payload': '/specialization'}]}, {'label': 'Dermatology', 'description': 'Diagnosis and treatments of diseases related to skin, hair, and nails.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Dermatology.png', 'buttons': [{'title': 'Dermatology', 'payload': '/specialization'}]}, {'label': 'Other Specialization', 'description': "Enter a particular specialization you're looking for.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/Specialities/Others.png', 'buttons': [{'title': 'Other Specialization', 'payload': '/other_specialization'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionAppointmentRequestedConfirmation(Action):
    def name(self):
        return "action_appointment_requested_confirmation"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_request_appointment'}, {'title': 'No', 'payload': '/no_request_appointment'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDoctorSelectedRequestForAppointment(Action):
    def name(self):
        return "action_doctor_selected_request_for_appointment"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_validateDoctor.json"
        dispatcher.utter_attachment(payload)
        return

class ActionCallbackRequestSelected(Action):
    def name(self):
        return "action_callback_request_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Reason 1', 'description': 'Item 1 description goes here...', 'image_type': 'url', 'image': 'https://dummyimage.com/600x400/aaaaaa/fff.png&text=Sample', 'buttons': [{'title': 'Reason 1', 'payload': '/cbreason1'}]}, {'label': 'Reason 2', 'description': 'Item description goes here...', 'image_type': 'url', 'image': 'https://dummyimage.com/600x400/aaaaaa/fff.png&text=Sample', 'buttons': [{'title': 'Reason 2', 'payload': '/cbreason2'}]}, {'label': 'Reason 3', 'description': 'Item description goes here...', 'image_type': 'url', 'image': 'https://dummyimage.com/600x400/aaaaaa/fff.png&text=Sample', 'buttons': [{'title': 'Reason 3', 'payload': '/cbreason3'}]}, {'label': 'Reason 4', 'description': 'Item description goes here...', 'image_type': 'url', 'image': 'https://dummyimage.com/600x400/aaaaaa/fff.png&text=Sample', 'buttons': [{'title': 'Reason 4', 'payload': '/cbreason4'}]}, {'label': 'Reason 5', 'description': 'Item description goes here...', 'image_type': 'url', 'image': 'https://dummyimage.com/600x400/aaaaaa/fff.png&text=Sample', 'buttons': [{'title': 'Reason 5', 'payload': '/cbreason5'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionRequestMadeAptTimeEnteredCallbackRequest(Action):
    def name(self):
        return "action_request_made_apt_time_entered_callback_request"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_callbackrequest'}, {'title': 'No', 'payload': '/no_callbackrequest'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionInsuranceCoverageSelected(Action):
    def name(self):
        return "action_insurance_coverage_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'What Emirate is the centre you are looking to visit located in?', 'replies': [{'title': 'Dubai', 'payload': '/emiratedubai'}, {'title': 'Abu Dhabi', 'payload': '/emiratead'}, {'title': 'Sharjah', 'payload': '/emiratesharjah'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionListOfPoliciesHospitalSelectedInsuranceCoverage(Action):
    def name(self):
        return "action_list_of_policies_hospital_selected_insurance_coverage"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_coverage'}, {'title': 'No', 'payload': '/no_coverage'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionHealthCalculatorSelected(Action):
    def name(self):
        return "action_health_calculator_selected"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'I can help you calculate your BMI.', 'replies': [{'title': 'Calculate BMI', 'payload': '/bmi'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionNoEmailChartselectedVaccinationCalculatorHealthCalculator(Action):
    def name(self):
        return "action_no_email_chartselected_vaccination_calculator_health_calculator"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_health_calculator'}, {'title': 'No', 'payload': '/no_health_calculator'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionEmailAddressEnteredEmailChartHealthCalculator(Action):
    def name(self):
        return "action_email_address_entered_email_chart_health_calculator"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_health_calculator'}, {'title': 'No', 'payload': '/no_health_calculator'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionBmiCalculatorSelected(Action):
    def name(self):
        return "action_bmi_calculator_selected"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_bmi.json"
        dispatcher.utter_attachment(payload)
        return

class ActionBmiCalculatedHeightEnteredBmiCalculatorHealthCalculators(Action):
    def name(self):
        return "action_bmi_calculated_height_entered_bmi_calculator_health_calculators"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_health_calculator'}, {'title': 'No', 'payload': '/no_health_calculator'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionFeedbackSelected(Action):
    def name(self):
        return "action_feedback_selected"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_feedback.json"
        dispatcher.utter_attachment(payload)
        return

class ActionFeedbackAcceptedEmailAddressEnteredFeedback(Action):
    def name(self):
        return "action_feedback_accepted_email_address_entered_feedback"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoFeedback"
        dispatcher.utter_attachment(payload)
        return

class ActionBmicalculated(Action):
    def name(self):
        return "action_bmicalculated"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/cbyes'}, {'title': 'No', 'payload': '/cbno'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionCallbackform(Action):
    def name(self):
        return "action_callbackform"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_callback.json"
        dispatcher.utter_attachment(payload)
        return

class ActionCallbackformsubmitted(Action):
    def name(self):
        return "action_callbackformsubmitted"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoCallback"
        dispatcher.utter_attachment(payload)
        return

class ActionSendlocation(Action):
    def name(self):
        return "action_sendlocation"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoDistance/distance"
        dispatcher.utter_attachment(payload)
        return

class ActionEmirateSelectedAbuDhabi(Action):
    def name(self):
        return "action_emirate_selected_abu_dhabi"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_areas_abu_dhabi.json"
        dispatcher.utter_attachment(payload)
        return

class ActionAreaformsubmission(Action):
    def name(self):
        return "action_areaformsubmission"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoDistance/area"
        dispatcher.utter_attachment(payload)
        return

class ActionEmirateSelectedDubai(Action):
    def name(self):
        return "action_emirate_selected_dubai"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_areas_dubai.json"
        dispatcher.utter_attachment(payload)
        return

class ActionEmirateSelectedSharjah(Action):
    def name(self):
        return "action_emirate_selected_sharjah"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_areas_sharjah.json"
        dispatcher.utter_attachment(payload)
        return

class ActionGetdirections(Action):
    def name(self):
        return "action_getdirections"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoDistance/directions"
        dispatcher.utter_attachment(payload)
        return

class ActionRequestAppointmentForm(Action):
    def name(self):
        return "action_request_appointment_form"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_speciality_form.json"
        dispatcher.utter_attachment(payload)
        return

class ActionGetlocationsfromspecialization(Action):
    def name(self):
        return "action_getlocationsfromspecialization"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoSpecialization/specialization"
        dispatcher.utter_attachment(payload)
        return

class ActionGetdoctorsfromspecialization(Action):
    def name(self):
        return "action_getdoctorsfromspecialization"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoGetDoctors"
        dispatcher.utter_attachment(payload)
        return

class ActionRequestappointmentfordoctorspecial(Action):
    def name(self):
        return "action_requestappointmentfordoctorspecial"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoGetDoctors/requestAppointment"
        dispatcher.utter_attachment(payload)
        return

class ActionRequestappointmentformcompleted(Action):
    def name(self):
        return "action_requestappointmentformcompleted"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoAppointmentMailer/requestAppointment"
        dispatcher.utter_attachment(payload)
        return

class ActionRequestappointmentbydoctor(Action):
    def name(self):
        return "action_requestappointmentbydoctor"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoGetDoctors/requestAppointmentDoctor"
        dispatcher.utter_attachment(payload)
        return

class ActionCallbackformshort(Action):
    def name(self):
        return "action_callbackformshort"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_callback_short.json"
        dispatcher.utter_attachment(payload)
        return

class ActionGetcentersforinsurance(Action):
    def name(self):
        return "action_getcentersforinsurance"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoInsurance"
        dispatcher.utter_attachment(payload)
        return

class ActionCheckinsurer(Action):
    def name(self):
        return "action_checkinsurer"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoInsurance/checkInsurer"
        dispatcher.utter_attachment(payload)
        return

class ActionEmirateSelectedAbuDhabiInsurance(Action):
    def name(self):
        return "action_emirate_selected_abu_dhabi_insurance"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_areas_abu_dhabi_ins.json"
        dispatcher.utter_attachment(payload)
        return

class ActionForceuserreg(Action):
    def name(self):
        return "action_forceuserreg"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_register.json"
        dispatcher.utter_attachment(payload)
        return

class ActionLanguageselection(Action):
    def name(self):
        return "action_languageselection"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'I can communicate with you in 2 languages, please select the language of your preference.', 'replies': [{'title': 'English', 'payload': '/language_en'}, {'title': 'عربى', 'payload': '/language_ar'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionGreetingIntentResponse(Action):
    def name(self):
        return "action_greeting_intent_response"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'https://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionMoreHelpInsuranceCoverage(Action):
    def name(self):
        return "action_more_help_insurance_coverage"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Request Appointment', 'description': 'Find a Doctor, a Hospital & Request for an Appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionMoreHelpRequestAppointment(Action):
    def name(self):
        return "action_more_help_request_appointment"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionFeedbackMoreHelp(Action):
    def name(self):
        return "action_feedback_more_help"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionBmiAdditionalHelp(Action):
    def name(self):
        return "action_bmi_additional_help"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/RequestAppt.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/InsuranceCover.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Callback.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Promotions.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/HEALTHCALCULATORS.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/mainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionHospitalNameRandom(Action):
    def name(self):
        return "action_hospital_name_random"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': "Which of the following services would you like for the centre you've mentioned above?", 'replies': [{'title': 'Get Directions', 'payload': '/random1'}, {'title': 'Insurance Policies', 'payload': '/random2'}, {'title': 'Specializations', 'payload': '/random3'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionGetlocationsfromspecializationdirect(Action):
    def name(self):
        return "action_getlocationsfromspecializationdirect"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoSpecialization/specializationDirect"
        dispatcher.utter_attachment(payload)
        return

class ActionSpecializationform(Action):
    def name(self):
        return "action_specializationform"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_speciality_form.json"
        dispatcher.utter_attachment(payload)
        return

class ActionCenternamebuttons(Action):
    def name(self):
        return "action_centernamebuttons"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': "What information would you like for {{context['Hospital Name'][0]['val'].toUpperCase()}}?", 'replies': [{'title': 'Address & Contact', 'payload': '/getdirectionsdirect'}, {'title': 'Specializations', 'payload': '/getspecializationsdirect'}, {'title': 'Insurers', 'payload': '/getinsurancesdirect'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionGetdirectionsdirect(Action):
    def name(self):
        return "action_getdirectionsdirect"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoDistance/directionsDirect"
        dispatcher.utter_attachment(payload)
        return

class ActionMoreHelpPromotionsAndOffers(Action):
    def name(self):
        return "action_more_help_promotions_and_offers"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'carousel', 'elements': [{'label': 'Request Appointment', 'description': 'Find a Doctor & initiate your request to book an appointment.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/RequestAppointment.png', 'buttons': [{'title': 'Request Appointment', 'payload': '/request_appointment'}]}, {'label': 'Locate a Centre', 'description': 'Find an AVIVO Centre & see how long it would take for you to reach.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/LocateACentre.png', 'buttons': [{'title': 'Locate a Centre', 'payload': '/locate_a_centre'}]}, {'label': 'Insurance Coverage', 'description': 'Find out if your Insurance Policy is accepted by an AVIVO Centre.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/InsuranceCoverage.png', 'buttons': [{'title': 'Insurance Coverage', 'payload': '/insurance_coverage'}]}, {'label': 'Request for Callback', 'description': 'Request for a callback from one of our Customer Support Agents.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/CallbackRequest.png', 'buttons': [{'title': 'Request for Callback', 'payload': '/request_for_callback'}]}, {'label': 'Promotions & Offers', 'description': "Stay updated with AVIVO Group's latest Promotions & Offers.", 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/PromotionsandOffers.png', 'buttons': [{'title': 'Promotions & Offers', 'payload': '/promotions_&_offers'}]}, {'label': 'Health Calculators', 'description': 'Get a BMI & Vaccination Calculator in a split second!', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/VaccinationCalculators.png', 'buttons': [{'title': 'Health Calculators', 'payload': '/health_calculators'}]}, {'label': 'Feedback', 'description': 'Provide any feedback or concerns you have about the AVIVO Group.', 'image_type': 'url', 'image': 'http://thatsbluelogic.com/projects/avivo/MainCarousel/Feedback.png', 'buttons': [{'title': 'Feedback', 'payload': '/feedback'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionGetdoctordirect(Action):
    def name(self):
        return "action_getdoctordirect"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoGetDoctors/requestAppointmentDoctor"
        dispatcher.utter_attachment(payload)
        return

class ActionGetcenterspecializationsdirect(Action):
    def name(self):
        return "action_getcenterspecializationsdirect"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoSpecialization/centerDirectSpecialization"
        dispatcher.utter_attachment(payload)
        return

class ActionGetcenterdirectinsurance(Action):
    def name(self):
        return "action_getcenterdirectinsurance"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoInsurance/centerDirectInsurance"
        dispatcher.utter_attachment(payload)
        return

class ActionGetinsurancedirect(Action):
    def name(self):
        return "action_getinsurancedirect"
    def run(self, dispatcher, tracker, domain):
        payload = "https://us-central1-glib-platform-bluelogic.cloudfunctions.net/avivoInsurance/getInsuranceDirect"
        dispatcher.utter_attachment(payload)
        return

class ActionPrimacareSpecialityClinicAddress(Action):
    def name(self):
        return "action_primacare_speciality_clinic_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May i help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionMusallaCentreAlBarshaBranchAddress(Action):
    def name(self):
        return "action_musalla_centre_al_barsha_branch_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDoctorsClinicAddress(Action):
    def name(self):
        return "action_doctors_clinic_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionGermanMedicalCenterAddress(Action):
    def name(self):
        return "action_german_medical_center_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionConceiveGynaecologyAndFertilityHospitalShjAddress(Action):
    def name(self):
        return "action_conceive_gynaecology_and_fertility_hospital_shj_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionConceiveGynaecologyAndFertilityCentreAddress(Action):
    def name(self):
        return "action_conceive_gynaecology_and_fertility_centre_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionNnmcPrimacareClinics(Action):
    def name(self):
        return "action_nnmc_primacare_clinics"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionNnmcPharmacyAddress(Action):
    def name(self):
        return "action_nnmc_pharmacy_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionNnmcBranch1Address(Action):
    def name(self):
        return "action_nnmc_branch_1_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I assist you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionNationalHospitalAddress(Action):
    def name(self):
        return "action_national_hospital_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'What more can I help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionRimaPharmacyAddress(Action):
    def name(self):
        return "action_rima_pharmacy_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with anything else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionAlBarshaClinicAddress(Action):
    def name(self):
        return "action_al_barsha_clinic_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionMuhaisnaSpecialistMedicalCentreAddress(Action):
    def name(self):
        return "action_muhaisna_specialist_medical_centre_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsDentalClinicUmmSeqimAddress(Action):
    def name(self):
        return "action_dr_michaels_dental_clinic_umm_seqim_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsDentalClinicJumeirahBranchAddress(Action):
    def name(self):
        return "action_dr_michaels_dental_clinic_jumeirah_branch_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I assist you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsChildrensDentalCenter(Action):
    def name(self):
        return "action_dr_michaels_childrens_dental_center"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionAestheticaClinicHealthcareCityAddress(Action):
    def name(self):
        return "action_aesthetica_clinic_healthcare_city_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionAestheticaClinicJumeirahBranchAddress(Action):
    def name(self):
        return "action_aesthetica_clinic_jumeirah_branch_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I help you with with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionAestheticaClinicAddressBoth(Action):
    def name(self):
        return "action_aesthetica_clinic_address_both"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDermalaseClinicDeiraAddress(Action):
    def name(self):
        return "action_dermalase_clinic_deira_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDermalaseClinicJumeirahAddress(Action):
    def name(self):
        return "action_dermalase_clinic_jumeirah_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDermalaseClinics(Action):
    def name(self):
        return "action_dermalase_clinics"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May i help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionReemMedicalAndDiagnosticCentreAddress(Action):
    def name(self):
        return "action_reem_medical_and_diagnostic_centre_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionReemSpecialistMedicalCentreAddress(Action):
    def name(self):
        return "action_reem_specialist_medical_centre_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Can I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionReemAlNahdaMedicalCentre(Action):
    def name(self):
        return "action_reem_al_nahda_medical_centre"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionReemMedicalCentreAddresses(Action):
    def name(self):
        return "action_reem_medical_centre_addresses"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsClinic(Action):
    def name(self):
        return "action_dr_michaels_clinic"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsOrthodonticCentre(Action):
    def name(self):
        return "action_dr_michaels_orthodontic_centre"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionDrMichaelsDentalClinicDhccBranchAddress(Action):
    def name(self):
        return "action_dr_michaels_dental_clinic_dhcc_branch_address"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there something else I can do for you?', 'replies': [{'title': 'Yes', 'payload': '/yes_address_and_location'}, {'title': 'No', 'payload': '/no_address_and_location'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionJobVacancy(Action):
    def name(self):
        return "action_job_vacancy"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'Is there anything else I can help you with?', 'replies': [{'title': 'Yes', 'payload': '/yes_promotions_and_offers'}, {'title': 'No', 'payload': '/no_promotions_and_offers'}]}]}
        dispatcher.utter_attachment(payload)
        return

class ActionIntentsBeforeTheIntroductionForm(Action):
    def name(self):
        return "action_intents_before_the_introduction_form"
    def run(self, dispatcher, tracker, domain):
        payload = "https://storage.googleapis.com/glib-forms-bluelogic/avivo_register.json"
        dispatcher.utter_attachment(payload)
        return

class ActionWomensDayPromotion(Action):
    def name(self):
        return "action_womens_day_promotion"
    def run(self, dispatcher, tracker, domain):
        payload = {'type': 'quickreplies', 'elements': [{'text': 'May I help you with something else?', 'replies': [{'title': 'Yes', 'payload': '/yes_promotions_and_offers'}, {'title': 'No', 'payload': '/no_promotions_and_offers'}]}]}
        dispatcher.utter_attachment(payload)
        return

