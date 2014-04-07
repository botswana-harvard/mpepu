ALIVE_DEAD_UNKNOWN = (
    ('ALIVE', 'Alive'),
    ('DEAD', 'Deceased'),
    ('UNKNOWN', 'Unknown'),
    )

VISIT_INFO_SOURCE = [
    ('participant', '1. Clinic visit with participant'),
    ('other_contact', '2. Other contact with participant (for example telephone call)'),
    ('other_doctor', '3. Contact with external health care provider/medical doctor'),
    ('family', '4. Contact with family or designated person who can provide information'),
    ('chart', '5. Hospital chart or other medical record'),
    ('OTHER', '9. Other'),
]

VISIT_REASON = [
    ('scheduled', '1. Scheduled visit/contact'),
    ('missed', '2. Missed Scheduled visit'),
    ('unscheduled', '3. Unscheduled visit at which lab samples or data are being submitted'),
    ('lost', '4. Lost to follow-up (use only when taking subject off study)'),
    ('death', '5. Death'),
    ('off study', '6. Subject has completed the study'),
    ('deferred', '7. Deferred (not available for maternal visits)'),
    ('vital status', '8. Vital Status'),
]

OFF_STUDY_REASON = [
    ('not_18', ' 1. Mother of infant found to be less than 18 years of age'),
    ('not_citizen', ' 2. Mother found not be a citizen of Botswana'),
    ('moved', ' 3. Subject will be moving out of study area or unable to stay in study area'),
    ('lost_no_contact', ' 4. Lost to follow-up, unable to locate'),
    ('lost_contacted', ' 5. Lost to follow-up, contacted but did not come to study clinic'),
    ('withdrew', ' 6. Participant changed mind and withdrew consent'),
    ('withdrew_by_father', ' 7. Father of baby did not want infant to participate and participant withdrew consent'),
    ('withdrew_by_family', ' 8. Other family member did not want mother/infant to participate and participant withdrew consent'),
    ('infant_died', ' 9. Infant died before being randomised (complete the DEATH REPORT AF005 form)'),
    ('stillbirth', '10. Stillbirth occurred after mother consented in pregnancy'),
    ('infant_hiv_pos', '11. Infant found to be HIV-infected'),
    ('infant_ill', '12. Infant diagnosed with medical condition making survival to 18 months unlikely'),
    ('>34_day_old', '13. Infant over 34 days old'),
    ('complete', '14. Completion of protocol required period of time for observation (see Study Protocol for definition of Completion.) [skip to end of form]'),
    ('death', '15. Participant death (complete the DEATH REPORT FORM AF005) (For EAE Reporting requirements see EAE Reporting Manual)'),
    ('refused', '16. Participant (or Participant\'s family) refused further contact (explain in Comments below)'),
    ('OTHER', '99. Other'),
]

FEEDING_INFLUENCE = (
    ('The father of my child', 'The father of my child'),
    ('My mother', 'My mother'),
    ('My sister', 'My sister'),
    ('Family members of the father of my child', 'Family members of the father of my child'),
    ('The ANC feeding counsellors', 'The ANC feeding counsellors'),
    ('The ANC nurses', 'The ANC nurses'),
    ('The ANC physicians', 'The ANC physicians'),
    ('OTHER', 'Other, describe in textbox below...'),
    ('No one', 'No other individual will influence my feeding choice decision'),
)

FEEDING_TRAINING = (
    ('ANC', 'ANC'),
    ('Labour and Delivery Ward', 'Labour and Delivery Ward'),
    ('Maternity Ward after delivery', 'Maternity Ward after delivery'),
)

FEEDING_INDECISION = (
    ('Waiting for more advice from nurses/doctors', 'Waiting for more advice from nurses/doctors'),
    ('Waiting for input from the father of the baby', 'Waiting for input from the father of the baby'),
    ('Waiting for input from other family members', 'Waiting for input from other family members'),
    ('Still thinking over it', 'Still thinking over it'),
    ('Unsure', 'Unsure'),
    ('NA', 'Not applicable')
)

YES_NO_FF = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('N/A', 'Not applicable (formula fed)'),
    )
