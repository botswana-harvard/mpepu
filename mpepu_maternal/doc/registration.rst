Registration
============

Data collection begins with the :class:`~mpepu_maternal.models.MaternalConsent`. When this model is submitted the mother
is allocated a unique subject identifier and a link to the maternal dashboard becomes available. From
the maternal dashboard one of two eligibility forms are completed (:class:`~mpepu_maternal.models.MaternalEligibilityAnte` or
:class:`~mpepu_maternal.models.MaternalEligibilityPost`). The eligibility forms open up access to one of two data collection
schedules where the lead model for each scheduled timepoint is the :class:`~mpepu_maternal.models.MaternalVisit`.

The infants are not allocated identifiers until the :class:`Labor and Delivery <mpepu_maternal.models.maternal_lab_del.MaternalLabDel>`
model is submitted. The number of infant identifiers is based on the reported number of live infants and the number of infants to be registered to the study.
See :mod:`mpepu_infant` for more details.