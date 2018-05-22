# encoding: utf-8
# -*- coding: utf-8 -*-
import time, sys
reload(sys)
sys.setdefaultencoding('utf-8')

def procedure(obj):
	# полезное тело процедуры
	print u'Выполнение тела процедуры. обработка объекта %s' % obj
	return

# цикл For	
def for_loop():
	objects_list = (None,234,u'qwas', False)
	count_objects = len(objects_list)
	
	for obj in objects_list:
		procedure(obj)

	print u'Код цикла for был выполнен %s раз' % count_objects
	print u'Процедура была вызвана %s раз' % count_objects

# аналог for с помощью while
def  while_for_loop():
	
	objects_list = (None,234,u'qwas', False)
	count_objects = len(objects_list)

	counter = 0
	while counter < count_objects:
		procedure(objects_list[counter])
		counter += 1
	
	print u'Код цикла while был завершен на %s раз проверки условия' % (counter + 1)
	print u'Процедура была вызвана %s раз' % count_objects