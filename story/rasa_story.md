## story greeting_&_introduction
* session_started
  - utter_introductionform
  - action_languageselection

## story greeting_(intent)
* greeting_introduction
  - utter_greeting_introduction
  - action_greeting_introduction

## story real_or_bot_(intent)
* are_you_real
  - utter_real_human_bot
  - action_real_human_bot
  - utter_real_human_bot_1
  - utter_real_human_bot_2
  - action_real_human_bot_1

## story promotions_&_offers_(selected)
* promotions_&_offers
  - utter_promotions_&_offers_selected
  - action_promotions_&_offers_selected

## story no_help_(promotions_&_offers)
* no_promotions_and_offers
  - utter_no_help_promotions_&_offers
  - utter_no_help_promotions_&_offers_1
  - utter_no_help_promotions_&_offers_1_2
  - utter_no_help_promotions_&_offers_3
  - utter_no_help_promotions_&_offers_4

## story promotions_and_offers(intents)
* promotions_&_offers
  - utter_promotions_&_offers_selected
  - action_promotions_&_offers_selected

## story locate_a_centre_selected
* locate_a_centre
  - utter_locate_a_centre_selected
  - action_locate_a_centre_selected

## story locateavivohospital
* locate1
  - action_locate_selected_locate_a_centre

## story share_location_(selected)_-_locate_a_centre
* share_location
  - action_share_location_selected_locate_a_centre

## story enter_details_(selected)
* enter_details
  - action_enter_manually_selected

## story emirate_(select)_-_locate_a_centre_-_manually
* emiratead
  - utter_emirate_selected_abu_dhabi
  - action_emirate_selected_abu_dhabi

## story other_specialization_(selected)_-_request_for_appt_-_specialization
* other_specialization
  - utter_other_specialization_selected_request_for_appt_specialization

## story specialization_(selected)_-_appointment_req_-_specialization
* specialization_selected
  - utter_specialization_selected_entered_specialization_request_for_appointment

## story doctor_(selected)_-_request_for_appointment
* doctor
  - utter_doctor_selected_request_for_appointment
  - action_doctor_selected_request_for_appointment
  - utter_doctor_selected_request_for_appointment_1
  - action_doctor_selected_request_for_appointment_1

## story insurance_coverage_(selected)
* insurance_coverage OR insurance_coverage
  - utter_insurance_coverage_selected
  - action_insurance_coverage_selected

## story emirate_(selected)_-_insurance_coverage
* emirates
  - utter_area_location_of_hospital_emirate_selected_insurance_coverage
  - utter_area_location_of_hospital_emirate_selected_insurance_coverage_1

## story health_calculators_(selected)
* health_calculators
  - action_health_calculator_selected

## story vaccination_calculator_(selected)_-_health_calculators
* vaccination
  - -L20Q9hEkbXj6KLa4NV3

## story bmi_calculator_(selected)
* bmi
  - utter_bmi_calculator_selected
  - utter_bmi_calculator_selected_1
  - action_bmi_calculator_selected

## story health_calculators
* health_calculators
  - action_health_calculator_selected

## story feedback_(intents)
* feedback OR feedback
  - utter_feedback_selected
  - action_feedback_selected

## story request_appointment
* request_appointment OR request_appointment
  - action_request_appointment_selected

## story area_entered_-_manual_-_locate_a_centre_(emirate_selected)
* 
  - utter_location_entered_carousel_of_hospitals_locate_a_centre_manual

## story valid_doctors_name_entered_(doctor)_-_request_for_appt
* doctors_name_questions
  - action_getdoctordirect

## story locate_a_centre_(intents)
* locate_a_centre_intents
  - utter_locate_a_centre_selected
  - action_locate_a_centre_selected

## story bmiformsubmission
* submitform
  - utter_bmicalculating

## story bmicalculated
* bmicalculating
  - utter_bmicalculated
  - action_bmicalculated

## story reasonforcallback
* request_for_callback OR callback_request
  - utter_callbackform
  - action_callbackform

## story calbackformsubmitted
* submitform
  - action_callbackformsubmitted

## story callbackmorehelp
* yes_callbackrequest
  - -L3YTWw5Go4kTdjXWttC

## story callbacknohelp
* cbno
  - utter_no_more_help_callback_request
  - utter_no_more_help_callback_request_1
  - utter_no_more_help_callback_request_2

## story feedbackaccepted
* submitform
  - action_feedback_accepted_email_address_entered_feedback

## story feedbackmorehelp
* yes_feedback
  - utter_feedback_more_help
  - action_feedback_more_help

## story feedbacknohelp
* no_feedback
  - utter_no_more_help_feedback_provided_closing_message_request_for_appointment
  - utter_no_more_help_feedback_provided_closing_message_request_for_appointment_1

## story introductionformsubmission
* submitform
  - action_languageselection

## story usersharedlocation
* user_shared_location
  - action_sendlocation

## story emirate_(select)_-_locate_a_centre_-_manually_1
* emiratedubai
  - utter_emirate_selected_dubai
  - action_emirate_selected_dubai

## story emirate_(select)_-_locate_a_centre_-_manually_2
* emiratesharjah
  - utter_emirate_selected_sharjah
  - action_emirate_selected_sharjah

## story areaformsubmission
* submitform
  - action_areaformsubmission

## story getdirectionsfrompostback
* center1 OR center2 OR center3 OR center4 OR center5 OR center6 OR center0 OR center7 OR center8 OR center9 OR center10 OR center11 OR center12 OR center13 OR center14 OR center15 OR center16 OR center17 OR center18 OR center19 OR center20 OR center21 OR center22 OR center23 OR center24 OR center25
  - action_getdirections

## story locateavivoclinic
* locate2
  - action_locate_selected_locate_a_centre

## story locateprimacare
* locate3
  - action_locate_selected_locate_a_centre

## story locateaesthetica
* locate4
  - action_locate_selected_locate_a_centre

## story locatedermalase
* locate5
  - action_locate_selected_locate_a_centre

## story locatealbarsha
* locate6
  - action_locate_selected_locate_a_centre

## story getlocationsfromspecialization
* submitform
  - action_getlocationsfromspecialization

## story getdoctorsfromspecialization
* getdoctorfor0 OR getdoctorfor1 OR getdoctorfor2 OR getdoctorfor3 OR getdoctorfor4 OR getdoctorfor5 OR getdoctorfor6 OR getdoctorfor7 OR getdoctorfor8 OR getdoctorfor9 OR getdoctorfor10 OR getdoctorfor11 OR getdoctorfor12 OR getdoctorfor13 OR getdoctorfor14 OR getdoctorfor15 OR getdoctorfor16 OR getdoctorfor17 OR getdoctorfor18 OR getdoctorfor19 OR getdoctorfor20 OR getdoctorfor21 OR getdoctorfor22 OR getdoctorfor23
  - action_getdoctorsfromspecialization

## story getdoctorappointmentspecial
* requestappointment
  - action_requestappointmentfordoctorspecial

## story requestappointmentformcompleted
* submitform
  - action_requestappointmentformcompleted

## story requestappointmentbydoctor
* submitform
  - action_requestappointmentbydoctor

## story requestappointmentnoformneeded
* requestappointment
  - utter_requestingappointmentwithdoctor
  - action_requestappointmentformcompleted

## story reasonforcallbackshort
* request_for_callback OR callback_request
  - utter_callbackformshort
  - action_callbackformshort

## story areaformsubmissioninsurance
* submitform
  - action_getcentersforinsurance

## story getinsurancesfrompostback
* center1 OR center2 OR center3 OR center4 OR center5 OR center6 OR center0 OR center7 OR center8 OR center9 OR center10 OR center11 OR center12 OR center13 OR center14 OR center15 OR center16 OR center17 OR center18 OR center19 OR center20 OR center21 OR center22 OR center23 OR center24 OR center25
  - action_checkinsurer

## story locatemuhaisna
* locate7
  - action_locate_selected_locate_a_centre

## story languages
* languages
  - utter_language_intent
  - utter_language_intent_1

## story home_services
* home_services
  - utter_home_services
  - utter_home_services_1
  - utter_home_services_2

## story emirate_(select)_-_locate_a_centre_-_ad_ins
* emiratead
  - utter_emirate_selected_abu_dhabi_insurance
  - action_emirate_selected_abu_dhabi_insurance

## story locateprimapharma
* locate8
  - action_locate_selected_locate_a_centre

## story locatemichael
* locate9
  - action_locate_selected_locate_a_centre

## story locatennmc
* locate10
  - action_locate_selected_locate_a_centre

## story sick_leave_and_medical_certificate_(intents)
* sick_leave_medical_certificates
  - utter_sick_leave_and_medical_certificate
  - utter_sick_leave_and_medical_certificate_1
  - utter_sick_leave_and_medical_certificate_2

## story request_for_appointment_(intents)
* request_appointment
  - action_request_appointment_selected

## story locate_a_centre_(intents)
* locate_a_centre_intents
  - utter_locate_a_centre_selected
  - action_locate_a_centre_selected

## story languageselecteden
* language_en
  - utter_processinglanguage

## story languageselectedar
* language_ar
  - utter_processinglanguage

## story bmi_more_help
* cbyes
  - utter_bmi_additional_help
  - action_bmi_additional_help
  - utter_bmi_additional_help_1
  - action_bmi_additional_help_1
  - utter_bmi_additional_help_1_2
  - action_bmi_additional_help_1_2
  - utter_bmi_additional_help_1_2_3
  - action_bmi_additional_help_1_2_3

## story specializationentered
* specializations_offered
  - action_getlocationsfromspecializationdirect

## story specializationbuttonclick
* specialization OR specialization
  - action_specializationform

## story centernamedirect
* common_centres_questions
  - action_centernamebuttons

## story directionsdirect
* getdirectionsdirect
  - action_getdirectionsdirect

## story dummyflowfordoctor
* dr_a_el-gheriani OR dr_abdul_malik OR dr_achim_lueth OR dr_tasneem_zoeb_saif OR dr_ritamoni_sengupta OR prof_zimmermann OR dr_matschke OR dr_amaya_ugarte OR dr_ashraf_kamel OR dr_kai_uwe_khrmann OR dr_darya_homayounfar OR dr_dushan_motwani OR dr_saji_bawa OR dr_soman_pillai OR dr_parul_saxena OR dr_archana_verma OR dr_aruna_ramesh OR dr_abdul_malik OR dr_ragesh_panchikkal OR dr_john_marshall OR dr_shashikant_shinde OR dr_urmimala_sinha OR dr_rupali_ranjith OR dr_p_satish_kumar OR dr_asma_akther OR dr_pankaj_shrivastav OR dr_shahlla_raghib OR dr_asma_munir OR dr_ghada_omer OR dr_shabbir_puthawala OR dr_isha_gopalan OR dr_sapna_ahuja OR dr_fouzia_unis OR dr_pramod_varghese OR dr_rita_parikh OR dr_suresh_kochubava OR dr_mohammed_elhsan OR dr_richard_tobias OR dr_umer_arfath OR dr_anu_ninan_anu OR dr_george_varghese OR dr_hussein_ismail OR dr_nesreen_ismail OR dr_priya__sharma OR dr_rami_abdullatif OR dr_reena_cheriyan OR dr_sathya_puthran OR dr_shilu_philip OR dr_subramanyan_nadar OR dr_suresh_kochubava OR dr_sivapradsad_reddy OR dr_sayeda_bushra OR dr_john OR dr_michael_formenius OR dr_marwan_al-obeidi OR dr_soren_jensen OR dr_christina_moeller OR dr_soulaf_shaker OR dr_sosan_fatima OR dr_kerry_ahmadi OR dr_sarel_linde OR dr_lina_shaar OR dr_linda_raskansky OR dr_eman_hagag OR dr_thomas_lyth OR dr_imneet_madan OR dr_mai_kamar OR dr_carol_onyango OR dr_rafif_tayara OR dr_teertha_karnakar OR dr_lina_papika OR dr_argiro_kechagia OR dr_a_el-gheriani OR dr_yasmin_zoubaidy OR dr_omar_aldaoudi OR dr_samy_darwish OR dr_walter_goriwoda OR dr_felicia_bjurfjall OR dr_dulene_swanepoel OR dr_alessandro_amadei OR dr_hanan_abdalla OR dr_martina_crisma OR dr_hilde_brunvoll_lyth OR dr_martha_duarte OR dr_valentina_manolova OR dr_vaishali_satpudke OR dr_regina_curilina OR dr_michael_boss OR dr_majd_al_zoughbi OR dr_aliya_nurpeissova OR dr_nisha_praveen OR dr_khuloud_abdouli OR dr_georgia_vadarli OR dr_ali_single OR dr_faisal_javed_khan OR dr_ajay_kumar OR dr_gopakumar_nair OR dr_avula_siva_prasad OR dr_tasneem_zoeb_saif OR dr_ritamoni_sengupta OR dr_subha_rita_thomas OR dr_meenu_mathew OR dr_sharley_saji OR dr_george_joseph OR dr_preetha_vinoj OR dr_sameer_tm OR dr_subathra_leela OR dr_silji_manoj OR dr_sheila_j_de_luna OR dr_dalia_zikry OR dr_priya_joby OR dr_sreeraj_sreedharan OR dr_gopal_mohan OR dr_n_d_george OR dr_philip_mathew OR dr_mohammed_badaruzman OR dr_rajani_thachapilly OR dr_binu_santhosh OR dr_qassim_ahli OR dr_rayan_al_abrach OR dr_kseniya_kapelko OR dr_pier_mancini OR dr_sinem_larsen OR dr_mario_russo OR dr_marilyn_alexander OR dr_rahleh_mahtabpour OR dr_kavita_tarale OR dr_fernando_meneses OR dr_mohd_atif_shah OR dr_sithara_haridas OR dr_sree_rajkumar OR dr_ravindra_umrao OR dr_priya_choudhury OR dr_neeraj_sharma OR dr_mohammed_faiz OR dr_mohammad_ali OR dr_kusumam_thomas OR dr_bibek_rameswar OR dr_ashraf_khalil OR dr_amod_tilak OR dr_akhter_ansari OR dr_aijaz_lone OR dr_kottakulath OR dr_shakeel_soomro OR dr_khambathy OR dr_awad_omer OR dr_shinde OR dr_farida_faquih OR dr_deepa_tito OR dr_ali_peral OR dr_gilbert_haddad OR dr_bassel_noah OR dr_saji_pillai OR dr_akbar_badushah OR dr_arlene_dagondon OR dr_varun_kundra OR dr_s_kallivalappil OR dr_ashraf_khalil OR dr_vandana_waghaye OR dr_sajith_nair OR dr_z_meletiadis OR dr_diethart_bayer OR dr_muthanna_alrawi OR prof_shabsigh OR prof_a_ralf_herwig OR dr_khaldoun_sharif OR prof_mettler OR dr_ahmad_rashid OR dr_ahmad_rashid OR dr_ahmad_rashid OR dr_swarna_kazi OR dr_ruma_bhargava OR dr_srinivas OR dr_pradeep_srivastav OR dr_liselotte_mettler OR dr_vaishali_srinivas OR prof_â_ralf_herwig OR dr_rohit_gulati OR dr_ashok_verma OR dr_zoeb_kachwala OR dr_deepak_naik OR dr_ashifa_noushad_ali OR dr_feraida_dardo OR dr_roshan_john OR dr_shaymaa_elsayed OR dr_baskaran_rajendran OR dr_simran_sharma OR dr_mohammad_bin_mansoor OR dr_j_rishiraj OR dr_pawan_babbira_nanaiah OR dr_vineeta_gupta OR dr_sivapradsad_gongala_reddy OR dr_george_varghese OR dr_bibek_chakrabarty_rameswar OR dr_sathyashankar_puthran
  - action_requestappointmentfordoctorspecial

## story more_help_promotions_and_offersmore_help_promotions_and_offers
* yes_promotions_and_offers
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story more_help_locate_a_centre
* yes_locate_centre
  - -L3YRGpcLtascJT4N7sZ

## story getcenterdirectspec
* getspecializationsdirect
  - action_getcenterspecializationsdirect

## story getcenterinsurancedirect
* getinsurancesdirect
  - action_getcenterdirectinsurance

## story insurancedirect
* common_questions_insurance
  - action_getinsurancedirect

## story name_intent
* name
  - utter_name

## story emotions_sad_intent
* emotions_sad
  - utter_emotions_sad
  - utter_emotions_sad_1
  - utter_emotions_sad_1_2

## story emotions_happy_intent
* emotions_happy
  - utter_emotions_happy

## story birthday_intent
* birthday
  - utter_birthday

## story feelings_positive_intent
* feelings_positive
  - utter_feelings_positive

## story feelings_negative_intent
* feelings_negative
  - utter_feelings_negative
  - utter_feedback_selected
  - action_feedback_selected

## story lab_report_request_intent
* lab_report_request OR customer_care
  - utter_contact_customer_care
  - utter_contact_customer_care_1
  - utter_contact_customer_care_2

## story what_is_avivo_intent
* what_is_avivo
  - utter_what_is_avivo
  - utter_what_is_avivo_1

## story cancel_appointment
* cancel_appointment
  - utter_cancel_appointment
  - utter_cancel_appointment_1
  - utter_cancel_appointment_2

## story more_help_addresses
* yes_address_and_location
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story no_help_addresses
* no_address_and_location
  - utter_no_help_promotions_&_offers
  - utter_no_help_promotions_&_offers_1
  - utter_no_help_promotions_&_offers_1_2
  - utter_no_help_promotions_&_offers_3
  - utter_no_help_promotions_&_offers_4

## story swear_words
* swear_words
  - utter_swear_words
  - utter_feedback_selected
  - action_feedback_selected

## story job_vacancy
* vacancy
  - utter_job_vacancy
  - utter_job_vacancy_1
  - action_job_vacancy

## story complaints_flow
* complaints
  - utter_complaints
  - utter_feedback_selected
  - action_feedback_selected

## story positive_feedback
* positive_feedback
  - utter_positive_feedback
  - utter_feedback_selected
  - action_feedback_selected

## story specializations_not_offered
* specializations_not_offered
  - utter_specializations_not_offered
  - utter_callbackformshort
  - action_callbackformshort

## story intents_before_the_introduction_form
* intents_before_the_introduction_form
  - utter_intents_before_the_introduction_form
  - utter_intents_before_the_introduction_form_1
  - utter_intents_before_the_introduction_form_2
  - action_intents_before_the_introduction_form

## story no_intent
* no_answer
  - utter_no_help_promotions_&_offers
  - utter_no_help_promotions_&_offers_1
  - utter_no_help_promotions_&_offers_1_2
  - utter_no_help_promotions_&_offers_3
  - utter_no_help_promotions_&_offers_4

## story feedback_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story request_appointment_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story vacancy_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story promotions_yes_oc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story promotions_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story bmi_more_help_intent
* yes_answer
  - utter_bmi_additional_help
  - action_bmi_additional_help
  - utter_bmi_additional_help_1
  - action_bmi_additional_help_1
  - utter_bmi_additional_help_1_2
  - action_bmi_additional_help_1_2
  - utter_bmi_additional_help_1_2_3
  - action_bmi_additional_help_1_2_3

## story callback_request_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story check_insurer_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story locate_a_centre_yes_cc
* yes_answer
  - utter_more_help_promotions_and_offers
  - action_more_help_promotions_and_offers
  - utter_more_help_promotions_and_offers_1
  - action_more_help_promotions_and_offers_1
  - utter_more_help_promotions_and_offers_1_2
  - action_more_help_promotions_and_offers_1_2
  - utter_more_help_promotions_and_offers_1_2_3
  - action_more_help_promotions_and_offers_1_2_3

## story woman_thirty_four_promotion
* woman_thirty_four OR woman_day_promotion
  - utter_womens_day_promotion
  - utter_womens_day_promotion_1
  - utter_womens_day_promotion_2
  - utter_womens_day_promotion_3
  - action_womens_day_promotion

