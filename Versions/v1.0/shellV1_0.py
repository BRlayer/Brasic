import brasicV1_0

while True:
	print()
	text = input('brasic_console v1.0 > ')
	print()
	if text.strip() == "": continue
	result, error = brasicV1_0.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			value = result.elements[0]
			if repr(value) != "0":
				print(repr(value))
		else:
			print(repr(result))