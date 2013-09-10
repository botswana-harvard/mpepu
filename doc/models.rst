Models
======

.. automodule:: mpepu_maternal.models
  :members: 

Base
----
The Base classes help ensure the following:

    1. All maternal models use a UUID as the primary key. 
    2. Eligibility models have a foreign key to :class:`RegisteredSubject`. 
    3. Scheduled models have a foreign key to :class:`MaternalVisit`. 

.. autoclass:: MyBaseUuidModel
  :show-inheritance:
  
.. autoclass:: BaseMaternalEligibility
  :show-inheritance:

.. autoclass:: BaseScheduledVisitModel
  :show-inheritance:  
  
Consent 
-------

.. autoclass:: MaternalConsent
  :members: 
  :show-inheritance:

Eligibility
-----------

.. autoclass:: MaternalEligibilityAnte
  :members: 
  :show-inheritance: 

.. autoclass:: MaternalEligibilityPost
  :members: 
  :show-inheritance: 

Registration
------------

Mothers are registered to the study using the :class:`MaternalConsent`.

.. warning:: Is this model used?

.. autoclass:: MaternalPostReg
  :members: 
  :show-inheritance:   

Enrollment
----------

In Mpepu, the Maternal Enrollment form is not a registration form and may be completed at any time between registration and randomization.

.. autoclass:: MaternalEnroll
  :members: 
  :show-inheritance: 

Visit
-----

.. autoclass:: mpepu_maternal.models.maternal_visit
  :members: 
  :show-inheritance: 


Follow-Up
---------

ARV - This Pregnancy 
++++++++++++++++++++

.. automodule:: mpepu_maternal.models.maternal_arv_preg
  :members: 
  :show-inheritance: 

ARV - Post-Partum 
+++++++++++++++++

.. automodule:: mpepu_maternal.models.maternal_arv_post
  :members: 
  :show-inheritance: 
  
Labor and Delivery
++++++++++++++++++

The Labor and Delivery model is responsible to create as many infant identifiers as indicated by the field
attribute :attr:`live_infants_to_register`. 

.. automodule:: mpepu_maternal.models.maternal_lab_del
  :members: 
  :show-inheritance: 
  
Post Partum
+++++++++++
   
.. automodule:: mpepu_maternal.models.maternal_post_fu
  :members: 
  :show-inheritance: 
    