
def four ():
	s = ''' Было просто пасмурно, дуло с севера
	А к обеду насчитал сто градаций серого.
	Так всегда первого ноль девятого
	То ли весь мир сошёл с ума, то ли я того...
	На столе записка от неё смятая
	Недопитый виски допиваю с матами.
	Посмотрю в окно, допишу главу
	Первое сентября, дворник жжёт листву.
	Сырым облакам наплевать на нас
	Если знаешь как жить - живи
	Ты хотела плыть как все - так плыви!'''
	
	s = [x for x in s.split() if len(x) < 5]

	return s
print (four())






