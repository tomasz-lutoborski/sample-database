from itertools import count
from re import I
from unicodedata import name
import modules.utils as utils
from flask import jsonify
from pprint import pprint
import sqlite3
import sys
from modules import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Engine = create_engine('sqlite+pysqlite:///data.db', echo=True)
Session = sessionmaker(bind=Engine)

# with Session() as session:
#     country = Country(
#         name='Sweden',
#         electricity_access=[ElectricityAccess(name='Sweden', year_2002=0.0, year_2003=0.0, year_2004=0.0, year_2005=0.0, year_2006=0.0, year_2007=0.0, year_2008=0.0, year_2009=0.0, year_2010=0.0, year_2011=0.0, year_2012=0.0, year_2013=0.0, year_2014=0.0, year_2015=0.0, year_2016=0.0, year_2017=0.0, year_2018=0.0, year_2019=0.0, year_2020=0.0, year_2021=0.0)],
#         insurance_coverage=[InsuranceCoverage(name='Sweden', year_2002=0.0, year_2003=0.0, year_2004=0.0, year_2005=0.0, year_2006=0.0, year_2007=0.0, year_2008=0.0, year_2009=0.0, year_2010=0.0, year_2011=0.0, year_2012=0.0, year_2013=0.0, year_2014=0.0, year_2015=0.0, year_2016=0.0, year_2017=0.0, year_2018=0.0, year_2019=0.0, year_2020=0.0, year_2021=0.0)],
#         health_expenditures_per_capita=[HealthExpendituresPerCapita(name='Sweden', year_2002=0.0, year_2003=0.0, year_2004=0.0, year_2005=0.0, year_2006=0.0, year_2007=0.0, year_2008=0.0, year_2009=0.0, year_2010=0.0, year_2011=0.0, year_2012=0.0, year_2013=0.0, year_2014=0.0, year_2015=0.0, year_2016=0.0, year_2017=0.0, year_2018=0.0, year_2019=0.0, year_2020=0.0, year_2021=0.0)],
#         health_expenditures_GDP_percentage=[HealthExpendituresGDPPercentage(name='Sweden', year_2002=0.0, year_2003=0.0, year_2004=0.0, year_2005=0.0, year_2006=0.0, year_2007=0.0, year_2008=0.0, year_2009=0.0, year_2010=0.0, year_2011=0.0, year_2012=0.0, year_2013=0.0, year_2014=0.0, year_2015=0.0, year_2016=0.0, year_2017=0.0, year_2018=0.0, year_2019=0.0, year_2020=0.0, year_2021=0.0)],
#         fertility_rate=[FertilityRate(name='Sweden', year_2002=0.0, year_2003=0.0, year_2004=0.0, year_2005=0.0, year_2006=0.0, year_2007=0.0, year_2008=0.0, year_2009=0.0, year_2010=0.0, year_2011=0.0, year_2012=0.0, year_2013=0.0, year_2014=0.0, year_2015=0.0, year_2016=0.0, year_2017=0.0, year_2018=0.0, year_2019=0.0, year_2020=0.0, year_2021=0.0)]
#     )

#     session.add(country)
#     session.commit()

Base.metadata.create_all(Engine)

data = utils.transform_data(utils.json_to_list('data.json'))

pprint(data)
