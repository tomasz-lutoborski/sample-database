from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'

    name = Column(String, primary_key=True)
    # electricity_access = Column(String, ForeignKey('electricity_access.name'))
    # insurance_coverage = Column(String, ForeignKey('insurance_coverage.name'))
    # health_expenditures_per_capita = Column(String, ForeignKey('health_expenditures_per_capita.name'))
    # health_expenditures_GDP_percentage = Column(String, ForeignKey('health_expenditures_GDP_percentage.name'))
    # fertility_rate = Column(String, ForeignKey('fertility_rate.name'))

    electricity_access = relationship('ElectricityAccess', back_populates='country')
    insurance_coverage = relationship('InsuranceCoverage', back_populates='country')
    health_expenditures_per_capita = relationship('HealthExpendituresPerCapita', back_populates='country')
    health_expenditures_GDP_percentage = relationship('HealthExpendituresGDPPercentage', back_populates='country')
    fertility_rate = relationship('FertilityRate', back_populates='country')


class ElectricityAccess(Base):
    __tablename__ = 'electricity_access'

    name = Column(String, ForeignKey('country.name'), primary_key=True)
    year_2002 = Column(Float)
    year_2003 = Column(Float)
    year_2004 = Column(Float)
    year_2005 = Column(Float)
    year_2006 = Column(Float)
    year_2007 = Column(Float)
    year_2008 = Column(Float)
    year_2009 = Column(Float)
    year_2010 = Column(Float)
    year_2011 = Column(Float)
    year_2012 = Column(Float)
    year_2013 = Column(Float)
    year_2014 = Column(Float)
    year_2015 = Column(Float)
    year_2016 = Column(Float)
    year_2017 = Column(Float)
    year_2018 = Column(Float)
    year_2019 = Column(Float)
    year_2020 = Column(Float)
    year_2021 = Column(Float)

    country = relationship('Country', back_populates='electricity_access')


class InsuranceCoverage(Base):
    __tablename__ = 'insurance_coverage'

    name = Column(String, ForeignKey('country.name'), primary_key=True)
    year_2002 = Column(Float)
    year_2003 = Column(Float)
    year_2004 = Column(Float)
    year_2005 = Column(Float)
    year_2006 = Column(Float)
    year_2007 = Column(Float)
    year_2008 = Column(Float)
    year_2009 = Column(Float)
    year_2010 = Column(Float)
    year_2011 = Column(Float)
    year_2012 = Column(Float)
    year_2013 = Column(Float)
    year_2014 = Column(Float)
    year_2015 = Column(Float)
    year_2016 = Column(Float)
    year_2017 = Column(Float)
    year_2018 = Column(Float)
    year_2019 = Column(Float)
    year_2020 = Column(Float)
    year_2021 = Column(Float)

    country = relationship('Country', back_populates='insurance_coverage')


class HealthExpendituresPerCapita(Base):
    __tablename__ = 'health_expenditures_per_capita'

    name = Column(String, ForeignKey('country.name'), primary_key=True)
    year_2002 = Column(Float)
    year_2003 = Column(Float)
    year_2004 = Column(Float)
    year_2005 = Column(Float)
    year_2006 = Column(Float)
    year_2007 = Column(Float)
    year_2008 = Column(Float)
    year_2009 = Column(Float)
    year_2010 = Column(Float)
    year_2011 = Column(Float)
    year_2012 = Column(Float)
    year_2013 = Column(Float)
    year_2014 = Column(Float)
    year_2015 = Column(Float)
    year_2016 = Column(Float)
    year_2017 = Column(Float)
    year_2018 = Column(Float)
    year_2019 = Column(Float)
    year_2020 = Column(Float)
    year_2021 = Column(Float)

    country = relationship('Country', back_populates='health_expenditures_per_capita')


class HealthExpendituresGDPPercentage(Base):
    __tablename__ = 'health_expenditures_GDP_percentage'

    name = Column(String, ForeignKey('country.name'), primary_key=True)
    year_2002 = Column(Float)
    year_2003 = Column(Float)
    year_2004 = Column(Float)
    year_2005 = Column(Float)
    year_2006 = Column(Float)
    year_2007 = Column(Float)
    year_2008 = Column(Float)
    year_2009 = Column(Float)
    year_2010 = Column(Float)
    year_2011 = Column(Float)
    year_2012 = Column(Float)
    year_2013 = Column(Float)
    year_2014 = Column(Float)
    year_2015 = Column(Float)
    year_2016 = Column(Float)
    year_2017 = Column(Float)
    year_2018 = Column(Float)
    year_2019 = Column(Float)
    year_2020 = Column(Float)
    year_2021 = Column(Float)

    country = relationship('Country', back_populates='health_expenditures_GDP_percentage')


class FertilityRate(Base):
    __tablename__ = 'fertility_rate'

    name = Column(String, ForeignKey('country.name'), primary_key=True)
    year_2002 = Column(Float)
    year_2003 = Column(Float)
    year_2004 = Column(Float)
    year_2005 = Column(Float)
    year_2006 = Column(Float)
    year_2007 = Column(Float)
    year_2008 = Column(Float)
    year_2009 = Column(Float)
    year_2010 = Column(Float)
    year_2011 = Column(Float)
    year_2012 = Column(Float)
    year_2013 = Column(Float)
    year_2014 = Column(Float)
    year_2015 = Column(Float)
    year_2016 = Column(Float)
    year_2017 = Column(Float)
    year_2018 = Column(Float)
    year_2019 = Column(Float)
    year_2020 = Column(Float)
    year_2021 = Column(Float)

    country = relationship('Country', back_populates='fertility_rate')
