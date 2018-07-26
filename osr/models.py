# -*- coding: utf-8 -*-
import os
from django.db import models
from django import forms
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# Choices
MARKER_TYPES = (('blu_circle', _('Blue circle')),('ltblu_circle', _('Light blue circle')),('ylw_circle', _('Yellow circle')),('red_circle', _('Red circle')),('orange_circle', _('Orange circle')),('grn_circle', _('Green circle')),('purple_circle', _('Purple circle')),('pink_circle', _('Pink circle')),('wht_circle',_('White circle')))
CSIZE_RANGES = (('1 - 10', '1 - 10'),('11 - 20', '11 - 20'),('20+', '20+'))
LEARN_STYLES = (('Online', _('Online')),('In-person', _('In-person')),('Blended', _('Blended')))
DAYS_OF_WEEK = (('Monday', _('Monday')),('Tuesday', _('Tuesday')),('Wednesday', _('Wednesday')),('Thursday', _('Thursday')),('Friday', _('Friday')),('Saturday', _('Saturday')),('Sunday', _('Sunday')))

@python_2_unicode_compatible
class Program(models.Model):
  class Meta:
    ordering = ['order_id']
    verbose_name = _('program')
    verbose_name_plural = _('programs')    

  def __str__(self):
    return "%s - %s" % (self.code, self.name_official)

  name_official = models.CharField(max_length=50, verbose_name=_('official name'), help_text=_('official name of the program'))
  name_branding = models.CharField(max_length=50, verbose_name=_('branding name'), help_text=_('branding name of the program'))
  code = models.CharField(max_length=3, default="PRO", verbose_name=_('code'))
  order_id = models.PositiveSmallIntegerField(verbose_name=_('order id'), default=1, help_text=_('a lower order id will show up first, min value is 1'))

  # Text fields shown in the Program Pages or the Comparison Page
  description = models.TextField(max_length=1000, blank=True, default="", verbose_name=_('description'))
  description_for_comparison_page = models.TextField(max_length=1000, blank=True, default="", verbose_name=_('description for comparison page'))
  details = models.TextField(max_length=1000, blank=True, default="", verbose_name=_('details'))
  length = models.TextField(max_length=200, blank=True, default="", verbose_name=_('length of the program'))
  subsidies = models.TextField(max_length=200, blank=True, default="", verbose_name=_('subsidies'))
  support = models.TextField(max_length=600, blank=True, default="", verbose_name=_('support'))
  funding = models.TextField(max_length=200, blank=True, default="", verbose_name=_('funding'))
  fees = models.TextField(max_length=200, blank=True, default="", verbose_name=_('fees'))
  free = models.BooleanField(default=False, verbose_name=_('free'))
  types_of_sps = models.TextField(max_length=600, blank=True, default="", verbose_name=_('types of service providers'))

  # Many to many fields
  learning_options = models.ManyToManyField('LearningOption')
  schedule_options = models.ManyToManyField('ScheduleOption')
  eligible_immigration_status = models.ManyToManyField('ImmigrationStatus', blank=True)
  benefits = models.ManyToManyField('Benefit')

  # Specifics about program
  img_src = models.ImageField(blank=True, null=True)
  img_txt = models.CharField(max_length=100, blank=True, default="")

  # Colour
  marker = models.CharField(max_length=15, default="grn_circle", choices=MARKER_TYPES, verbose_name=_('marker'))
  background_colour = models.CharField(max_length=50, default="#FFFFFF", verbose_name=_('background colour'))
  foreground_colour = models.CharField(max_length=50, default="#000000", verbose_name=_('foreground colour'))

  # Get outcomes of current offerings that match the program outcomes
  def get_outcomes(self):
    outcomes = []
    for offering in self.offering_set.all():
      for o in offering.outcomes.all():
        if o not in outcomes:
          outcomes.append(o)
    return outcomes

@python_2_unicode_compatible
class Benefit(models.Model):
  class Meta:
    verbose_name = _('benefit')
    verbose_name_plural = _('benefits')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))

@python_2_unicode_compatible
class ImmigrationStatus(models.Model):
  class Meta:
    verbose_name = _('immigration status')
    verbose_name_plural = _('immigration status')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))

@python_2_unicode_compatible
class LearningOption(models.Model):
  class Meta:
    verbose_name = _('learning option')
    verbose_name_plural = _('learning options')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))

@python_2_unicode_compatible
class ScheduleOption(models.Model):
  class Meta:
    verbose_name = _('schedule option')
    verbose_name_plural = _('schedule options')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))   

@python_2_unicode_compatible
class ProgramRegistrationSteps(models.Model):
  class Meta:
    ordering = ['id']
    verbose_name = _('registration step')
    verbose_name_plural = _('registration steps') 

  def __str__(self):
    return "%s - %s" % (self.program.code, self.text)

  program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name=_('program'))
  text = models.CharField(max_length=300, verbose_name=_('text'))

@python_2_unicode_compatible
class ProgramBestForScenarios(models.Model):
  class Meta:
    ordering = ['id']
    verbose_name = _('best for scenario')
    verbose_name_plural = _('best for scenarios') 

  def __str__(self):
    return "%s - %s" % (self.program.code, self.text)    

  program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name=_('program'))
  text = models.CharField(max_length=300, verbose_name=_('text'))  

@python_2_unicode_compatible
class ProgramLinks(models.Model):
  class Meta:
    ordering = ['id']
    verbose_name = _('program link')
    verbose_name_plural = _('program links') 

  def __str__(self):
    return "%s - %s" % (self.program.code, self.text)

  program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name=_('program'))
  text = models.CharField(max_length=150, verbose_name=_('text'))
  link = models.CharField(max_length=150, verbose_name=_('link'))

@python_2_unicode_compatible
class ServiceProvider(models.Model):
  class Meta:
    ordering = ['id']
    verbose_name = _('service provider')
    verbose_name_plural = _('service providers') 

  def __str__(self):
    return self.name    

  name = models.CharField(max_length=50, verbose_name=_('name'))
  # TODO: A user can only be linked to 1 SP
  # But a SP can have more than 1 user
  user = models.OneToOneField(User)
  programs = models.ManyToManyField('Program')

  logo = models.ImageField(blank=True, null=True, verbose_name=_('logo'))
  phone = models.CharField(max_length=50, blank=True, verbose_name=_('phone number'))
  email = models.EmailField(max_length=50, blank=True, verbose_name=_('e-mail'))
  address_street = models.CharField(max_length=50, blank=True, verbose_name=_('street'))
  address_city = models.CharField(max_length=30, blank=True, verbose_name=_('city'))
  address_province = models.CharField(max_length=30, blank=True, verbose_name=_('province'))
  address_zipcode = models.CharField(max_length=30, blank=True, verbose_name=_('zip code'))

@python_2_unicode_compatible
class ServiceDeliverySite(models.Model):
  class Meta:
    verbose_name = _('service delivery site')
    verbose_name_plural = _('service delivery sites')

  def __str__(self):
    if self.name:
      return "%s: %s" % (self.head.name, self.name)
    else:
      return self.head.name

  head = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, verbose_name=_('head'))
  name = models.CharField(max_length=50, blank=True, verbose_name=_('name'))

  # Find all programs offered by a specific service delivery site
  def get_programs(self):
    query_programs = models.Q()
    for x in self.offering_set.all():
      print x.program.id
      query_programs = query_programs | models.Q(id=x.program.id)
    items = Program.objects.order_by('id')
    items = items.filter(query_programs)
    return items  

  def get_complement(self):
    num = self.servicedeliverysitefacility_set.all().count()
    x = 1
    while ((x * 4) < num):
      x = x + 1
    return "x" * ((x * 4) - num)

  phone = models.CharField(max_length=50, blank=True, verbose_name=_('phone number'))
  email = models.EmailField(max_length=50, blank=True, verbose_name=_('e-mail'))
  address_street = models.CharField(max_length=50, blank=True, verbose_name=_('street'))
  address_city = models.CharField(max_length=30, blank=True, verbose_name=_('city'))
  address_province = models.CharField(max_length=30, blank=True, verbose_name=_('province'))
  address_zipcode = models.CharField(max_length=30, blank=True, verbose_name=_('zip code'))
  # Hidden to the user
  gps_lat = models.FloatField(null=True, blank=True)
  gps_lon = models.FloatField(null=True, blank=True)

@python_2_unicode_compatible
class Outcome(models.Model):
  class Meta:
    verbose_name = _('outcome')
    verbose_name_plural = _('outcomes')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))
  background_colour = models.CharField(max_length=50, default="#FFFFFF", verbose_name=_('background colour'))
  foreground_colour = models.CharField(max_length=50, default="#000000", verbose_name=_('foreground colour'))
  programs = models.ManyToManyField('Program', verbose_name=_('programs'))

@python_2_unicode_compatible
class Eligibility(models.Model):
  class Meta:
    verbose_name = _('eligibility')
    verbose_name_plural = _('eligibilities')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))
  programs = models.ManyToManyField('Program', verbose_name=_('programs'))

@python_2_unicode_compatible
class Subject(models.Model):
  class Meta:
    verbose_name = _('subject')
    verbose_name_plural = _('subjects')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))
  code = models.CharField(max_length=12, blank=True, verbose_name=_('code'))
  programs = models.ManyToManyField('Program', verbose_name=_('programs'))

@python_2_unicode_compatible
class Stream(models.Model):
  class Meta:
    verbose_name = _('stream')
    verbose_name_plural = _('streams')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=200, verbose_name=_('text'))
  programs = models.ManyToManyField('Program', verbose_name=_('programs'))

@python_2_unicode_compatible
class Offering(models.Model):
  class Meta:
    verbose_name = _('offering')
    verbose_name_plural = _('offerings')

  def __str__(self):
    return "%s: %s - %d" % (self.service_delivery_site.name, self.program.name_official, self.id)

  # Foreign keys
  program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name=_('program'))
  service_delivery_site = models.ForeignKey(ServiceDeliverySite, on_delete=models.CASCADE, verbose_name=_('service delivery site'))
  str_date = models.DateField(verbose_name=_('start date'))
  end_date = models.DateField(verbose_name=_('end date'))

  # TODO:
  class_size = models.CharField(max_length=10, choices=CSIZE_RANGES, verbose_name=_('class size'))
  learning_style = models.CharField(max_length=10, choices=LEARN_STYLES, verbose_name=_('learning style'))

  outcomes = ChainedManyToManyField(
    Outcome,
    horizontal=False,
    verbose_name=_('outcomes'),
    chained_field="program",
    chained_model_field="programs")

  requirements = ChainedManyToManyField(
    Eligibility,
    horizontal=False,
    verbose_name=_('requirements'),
    chained_field="program",
    chained_model_field="programs")
    #chained_model_field="programs",
    #blank=True)

  streams = ChainedManyToManyField(
    Stream,
    horizontal=False,
    verbose_name=_('stream'),
    chained_field="program",
    chained_model_field="programs")

  subjects = ChainedManyToManyField(
    Subject,
    horizontal=False,
    verbose_name=_('subjects'),
    chained_field="program",
    chained_model_field="programs")

  def get_number_of_perks(self):
    return "x" * (8 - self.offeringfeature_set.all().count() - self.service_delivery_site.servicedeliverysitefacility_set.all().count())

  def get_number_of_outcomes(self):
    return "x" * (8 - self.outcomes.all().count())

  def get_schedules(self):
    schedules = []
    for schedule in self.offeringschedule_set.all():
      schedules.append(str(schedule))
    return ', '.join(schedules)

  def get_subjects(self):
    subjects = []
    for subject in self.subjects.all():
      subjects.append(str(subject))
    return ', '.join(subjects)

  clb_01 = models.BooleanField(default=False, verbose_name=_('CLB level 1'))
  clb_02 = models.BooleanField(default=False, verbose_name=_('CLB level 2'))
  clb_03 = models.BooleanField(default=False, verbose_name=_('CLB level 3'))
  clb_04 = models.BooleanField(default=False, verbose_name=_('CLB level 4'))
  clb_05 = models.BooleanField(default=False, verbose_name=_('CLB level 5'))
  clb_06 = models.BooleanField(default=False, verbose_name=_('CLB level 6'))
  clb_07 = models.BooleanField(default=False, verbose_name=_('CLB level 7'))
  clb_08 = models.BooleanField(default=False, verbose_name=_('CLB level 8'))
  clb_09 = models.BooleanField(default=False, verbose_name=_('CLB level 9'))
  clb_10 = models.BooleanField(default=False, verbose_name=_('CLB level 10'))
  clb_11 = models.BooleanField(default=False, verbose_name=_('CLB level 11'))
  clb_12 = models.BooleanField(default=False, verbose_name=_('CLB level 12'))

@python_2_unicode_compatible
class OfferingSchedule(models.Model):
  class Meta:
    verbose_name = _('schedule')
    verbose_name_plural = _('schedules')

  def __str__(self):
    return "%s: %s to %s" % (self.day_of_the_week, str(self.str_time)[:-3], str(self.end_time)[:-3])

  # Hidden to the user
  offering = models.ForeignKey(Offering, on_delete=models.CASCADE)

  day_of_the_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK, verbose_name=_('day of the week'))
  str_time = models.TimeField(verbose_name=_('start time'))
  end_time = models.TimeField(verbose_name=_('end time'))

@python_2_unicode_compatible
class Profession(models.Model):
  class Meta:
    verbose_name = _('profession')
    verbose_name_plural = _('professions')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=60, verbose_name=_('text'))

@python_2_unicode_compatible
class OfferingProfession(models.Model):
  class Meta:
    verbose_name = _('profession')
    verbose_name_plural = _('professions')

  def __str__(self):
    return "%s - %s: %s" % (self.offering.service_delivery_site.name, self.offering.program.code, self.profession.text)

  offering = models.ForeignKey(Offering, on_delete=models.CASCADE)
  profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name=_('profession'))

@python_2_unicode_compatible
class Feature(models.Model):
  class Meta:
    verbose_name = _('feature')
    verbose_name_plural = _('features')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=60, verbose_name=_('text'))
  image = models.ImageField(blank=True, null=True, verbose_name=_('image'))

@python_2_unicode_compatible
class OfferingFeature(models.Model):
  class Meta:
    verbose_name = _('feature')
    verbose_name_plural = _('features')

  def __str__(self):
    return "%s - %s" % (self.offering, self.feature)

  offering = models.ForeignKey(Offering, on_delete=models.CASCADE)
  feature = models.ForeignKey(Feature, on_delete=models.CASCADE, verbose_name=_('feature'))

@python_2_unicode_compatible
class Facility(models.Model):
  class Meta:
    verbose_name = _('facility')
    verbose_name_plural = _('facilities')

  def __str__(self):
    return self.text

  text = models.CharField(max_length=60, verbose_name=_('text'))
  image = models.ImageField(blank=True, null=True, verbose_name=_('image'))

@python_2_unicode_compatible
class ServiceDeliverySiteFacility(models.Model):
  class Meta:
    verbose_name = _('facility')
    verbose_name_plural = _('facilities')

  def __str__(self):
    return "%s > %s" % (self.service_delivery_site.name, self.facility.text)

  service_delivery_site = models.ForeignKey(ServiceDeliverySite, on_delete=models.CASCADE, verbose_name=_('service delivery site'))
  facility = models.ForeignKey(Facility, on_delete=models.CASCADE, verbose_name=_('facility'))

@python_2_unicode_compatible
class Recommendation(models.Model):
  class Meta:
    verbose_name = _('recommendation')
    verbose_name_plural = _('recommendations')  

  def __str__(self):
    return self.code 
    
  code = models.CharField(max_length=20, verbose_name=_('code'))
  reason = models.CharField(max_length=100, verbose_name=_('reason'))
  text = models.CharField(max_length=100, verbose_name=_('text'))
  link = models.CharField(max_length=50, verbose_name=_('link'))