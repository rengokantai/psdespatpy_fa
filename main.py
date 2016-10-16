from autofactory import AutoFactory
factory = AutoFactory()

for carname in 'Jeep', 'NotExist':
	car = factory.create_instance(carname)
	car.start()
	car.stop()