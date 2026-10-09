import brasic

while True:
	print()
	text = input('brasic_console > ')
	print()
	if text.strip() == "": continue
	result, error = brasic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			value = result.elements[0]
			if repr(value) != "0":
				print(repr(value))
		else:
			print(repr(result))