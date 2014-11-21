import dateutil.parser
import datetime


stamp = "2014-11-06T17:08:49.827859"

timeobj = dateutil.parser.parse(stamp)

print timeobj.strftime('%Y-%m-%d %H:%M')

print dateutil.parser.parse(stamp).strftime('%Y-%m-%d %H:%M')