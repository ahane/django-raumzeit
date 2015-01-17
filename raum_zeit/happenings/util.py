import datetime 
import pytz

def now_utc():
	utc = pytz.utc
	return utc.localize(datetime.datetime.utcnow())

class UTC(datetime.tzinfo):
	    """UTC"""

	    def utcoffset(self, dt):
	        return datetime.timedelta(0)

	    def tzname(self, dt):
	        return "UTC"

	    def dst(self, dt):
	        return None

class CET(datetime.tzinfo):
	    """UTC"""

	    def utcoffset(self, dt):
	        return datetime.timedelta(hours=1)

	    def tzname(self, dt):
	        return "CET"

	    def dst(self, dt):
	        return None

