import function_calling

text = "The battery looks fine"

output = function_calling.check_battery_leak(text)

print(output.candidates[0].content.parts[0].function_call)