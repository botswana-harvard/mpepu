Randomization
=============

Infant randomization is triggered once the Infant Eligibility form is submitted successfully.

..seealso:: the :class:`save_model` in :class:`InfantEligibilityAdmin`.

Rando date depends on Maternal GA
+++++++++++++++++++++++++++++++++

Depending on the maternal gestational age, randomization can occur at 14 or 28 days. If maternal
GA is >= 37, the 2010 appointment date will be moved up from 28 to 14 days after birth. If GA
is unknown, the 2010 appointment date stays at 28 days from birth.

.. seealso:: :class:`InfantBirth`: :func:`post_prepare_appointments`

Rando date depends on infant weight at 2010
+++++++++++++++++++++++++++++++++++++++++++

If infant weight is less that 2.5kg at 2010, the infant is not eligible and the 
appointment date for 2010 should be moved to 28 days from birth.