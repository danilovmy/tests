# encoding: utf-8
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def procedure(counter):
	# полезное тело процедуры
	print u'Выполнение тела процедуры. %s-й вызов.' % counter
	return

def for_range_with_continue_loop(): # аналогично и для конструкции while
	proc_counter = 0
	for counter in range(1,10, 1):
		if counter%2:
			print u'Выполнение тела текущего цикла прервано оператором continue'
			continue
			print u'Текст после оператора continue никто никогда не увидит'
		proc_counter += 1
		procedure(proc_counter)
	else:
		print u'Выполнение цикла for не было прервано оператором brake'	

	print u'Цикл for был выполнен %s раз' % counter
	print u'Процедура была вызвана только %s раз' % proc_counter

def while_with_brake_loop(): # аналогично и для конструкции for
	proc_counter = 0
	while proc_counter < 9:
		if (proc_counter // 5):
			print u'Выполнение цикла while прервано оператором break'
			break
			print u'Текст после оператора break никто никогда не увидит'

		proc_counter += 1
		procedure(proc_counter)			
	else:
		print u'Выполнение цикла while не было прервано оператором brake'	

	print u'Код цикла while был выполнен %s раз' % proc_counter
	print u'Процедура была вызвана %s раз' % proc_counter