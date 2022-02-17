def get_vat(payment, present = 20):
	try:
		payment = float(payment)
		vat = payment/100*present
		vat = round(vat,2) 
		return 'Sum VAT: {}'.format(vat)
	except TypeEror:
		return 'Cant count. Check data'

result = get_vat(400, 15)
print(result)
