# -*- coding: utf-8 -*-

# цикл while
def  while_loop():

	#инициация параметров условия 
	counter = 1
	
	#начало цикла 
	while counter < 6:

		# тело цикла
		print 'Выполнение тела цикла. %s-й вызов.' % counter
		x = max(2,counter)
		print x

		#изменение параметров условия
		counter += 1
		
	print 'Код цикла while был завершен на %s раз проверки условия' % counter