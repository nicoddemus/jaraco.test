import pytest
try:
	import pymongo
except ImportError:
	pass

from . import services

def mongodb_instance():
	try:
		instance = services.MongoDBInstance()
		instance.log_root = ''
		instance.start()
		pymongo.Connection(instance.get_connect_hosts())
	except Exception:
		return None
	return instance

@pytest.yield_fixture(scope='session')
def mongodb(request):
	instance = mongodb_instance()
	if not instance:
		pytest.skip("MongoDB not available")
	yield instance
	instance.stop()
