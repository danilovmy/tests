# encoding: utf-8
# -*- coding: utf-8 -*-
import time, sys
import msvcrt, winsound  # для windows
#import select # для mac os / unix
reload(sys)
sys.setdefaultencoding('utf-8')

def check_correct_time(alarm_time):
	return time.time() + 8 # для тестирования поставим на 13 секунд позже

def wait_timer(sek):
	time_to_wake_up = time.time() + sek
	while time_to_wake_up > time.time(): pass
	return

def set_alarm():
	alarm_time = check_correct_time(raw_input(u'Установка будильника (ЧЧ:мм) : '.encode("cp866")))
	print u'Сейчас %s.\n' % time.ctime(), u'Будильник установлен на %s.' % time.ctime(alarm_time)
	wait_timer(3)
	print u'Сейчас %s. ' % time.ctime(), u'Последние моменты перед пробуждением.'

	for i in (5,4,3,2,1):
		wait_timer(1)
		print u'будильник сработает через %s секунд' % i

	for i in (3,2,3,2,3,2,3,2,3):
		if msvcrt.kbhit(): # строка для windows
		#if select.select([sys.stdin,],[],[],0.0)[0]: ## строка для mac os/unix
			print u'Доброе утро', u'Будильник остановлен'	
			break

		for j in range(0,i):
			#print chr(7) # для mac os
			winsound.Beep(2500, 750) # для windows
			wait_timer(0.25)
	else:
		print u'чуваак! Ты кажется проспал!'