# PyAlgoTrade
# 
# Copyright 2012 Gabriel Martin Becedillas Ruiz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

import datetime
import calendar
import pytz

def datetime_is_naive(dateTime):
	""" Returns True if dateTime is naive."""
	return dateTime.tzinfo is None or dateTime.tzinfo.utcoffset(dateTime) is None

def localize(dateTime, timeZone):
	"""Returns a datetime adjusted to a timezone:

	 * If dateTime is a naive datetime (datetime with no timezone information), timezone information is added but date and time remains the same.
	 * If dateTime is not a naive datetime, a datetime object with new tzinfo attribute is returned, adjusting the date and time data so the result is the same UTC time.
	"""

	if datetime_is_naive(dateTime):
		ret = timeZone.localize(dateTime)
	else:
		ret = dateTime.astimezone(timeZone)
	return ret

def as_utc(dateTime):
	return localize(dateTime, pytz.utc)

def datetime_to_timestamp(dateTime):
	""" Converts a datetime.datetime to a UTC timestamp."""
	return calendar.timegm(dateTime.utctimetuple())

def timestamp_to_datetime(timeStamp):
	""" Converts a UTC timestamp to a datetime.datetime."""
	ret = datetime.datetime.utcfromtimestamp(timeStamp)
	return localize(ret, pytz.utc)



