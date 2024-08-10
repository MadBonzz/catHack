import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
import anthropic
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
genai.configure(api_key=gemini_api_key)

client = anthropic.Anthropic(api_key=anthropic_api_key)


def check_tire_pressure(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the pressure of tire from the text. If the tire pressure is in decimals, round it to the nearest interger. If you are not sure, return -1 as pressure. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_tire_pressure",
            "description": "Extract the tire pressure as given in text",
            "input_schema": {
                "type": "object",
                "properties": {
                    "pressure": {"type": "integer", "description": "pressure of tire"}
                    },
                "required": ["pressure"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response


def check_tire_condition(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the condition of tire and assign it a label based on your understanding. Assign the condition one of the labels : [Good, Ok, Needs Replacement]. If you are not sure, return NULL as condition. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_tire_condition",
            "description": "Extract the tire condition as given in text and assign it a label from [Good, Ok, Needs Replacement]",
            "input_schema": {
                "type": "object",
                "properties": {
                    "condition": {"type": "string", "description": "condition of tire as Good, Ok or Needs Replacement"}
                    },
                "required": ["condition"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response

def check_tires(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_tire_info",
                "description": "Extract all the information about the tires of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "left_front_pressure": {"type": "integer", "description": "Pressure in the left front tire. If you are unsure of the value or the value is not in the text, set tire pressure as -1. If the pressure is in decimals, round it to the nearest integer."},
                        "right_front_pressure": {"type": "integer", "description": "Pressure in the right front tire. If you are unsure of the value or the value is not in the text, set tire pressure as -1. If the pressure is in decimals, round it to the nearest integer."},
                        "left_rear_pressure": {"type": "integer", "description": "Pressure in the left rear tire. If you are unsure of the value or the value is not in the text, set tire pressure as -1. If the pressure is in decimals, round it to the nearest integer."},
                        "right_rear_pressure": {"type": "integer", "description": "Pressure in the right rear tire. If you are unsure of the value or the value is not in the text, set tire pressure as -1. If the pressure is in decimals, round it to the nearest integer."},
                        "left_front_conditon": {"type": "string", "description": "left front tire condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "right_front_conditon": {"type": "string", "description": "right front tire condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "left_rear_conditon": {"type": "string", "description": "left rear tire condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "right_rear_conditon": {"type": "string", "description": "right rear tire condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "description": {"type": "string", "description": "A short description of overall conditon of tyres"},
                    },
                    "required": ["left_front_pressure", "right_front_pressure", "left_rear_pressure", "right_rear_pressure", "left_front_conditon", "right_front_conditon", "left_rear_conditon", "right_rear_conditon", "description"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_battery_make(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_make",
                "description": "Extract all the information about the battery manafacturer of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "battery_make": {"type": "string", "description": "Extract the name of the manafacturer of the battery. If the information is not present or you are unsure, return the maker as NULL."},
                    },
                    "required": ["battery_make"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_battery_replacement_date(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_replacement_date",
                "description": "Extract all the information about the battery replacement date of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "replacement_date": {"type": "string", "description": "Extract the information about the replacement date of the battery. Store and return it in the DD/MM/YY format. If you are unsure or the information is not available, return NULL as the date."},
                    },
                    "required": ["replacement_date"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_battery_voltage(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_voltage",
                "description": "Extract all the information about the battery voltage of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "voltage": {"type": "integer", "description": "The voltage of the battery. If the voltage is in decimals, round to the nearest integer. If the information is not available, return and store -1"},
                    },
                    "required": ["voltage"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_battery_water_level(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_water_level",
                "description": "Extract all the information about the battery water level of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "water_level": {"type": "string", "description": "Extract the water level of the battery and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                    "required": ["water_level"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_battery_damage(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_damage",
                "description": "Extract all the information about the damage to the battery of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "damage": {"type": "string", "description": "Extract any information about damage to the battery and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                    "required": ["damage"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_battery_leak(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_leak",
                "description": "Extract all the information about leakage or rust in the battery of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "leak": {"type": "string", "description": "Extract any information about leakage or rust in the battery and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                    "required": ["leak"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_battery(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_battery_info",
                "description": "Extract all the information about the battery of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "battery_make":     {"type": "string", "description": "Extract the name of the manafacturer of the battery. If the information is not present or you are unsure, return the maker as NULL."},
                        "replacement_date": {"type": "string", "description": "Extract the information about the replacement date of the battery. Store and return it in the DD/MM/YY format. If you are unsure or the information is not available, return NULL as the date."},
                        "voltage":          {"type": "integer", "description": "The voltage of the battery. If the voltage is in decimals, round to the nearest integer. If the information is not available, return and store -1"},
                        "water_level":      {"type": "string", "description": "Extract the water level of the battery and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                        "damage":           {"type": "string", "description": "Extract any information about damage to the battery and assign it a label from [Yes, No]. If the battery has been damaged, assign Yes else assign No. Store and return the label only."},
                        "leak":             {"type": "string", "description": "Extract any information about leak or rust in the battery and assign it a label from [Yes, No]. If the battery is leaking or is rusted, assign Yes else assign No. Store and return the label only."},
                        "description":      {"type": "string", "description": "A short description of overall conditon of battery"},
                    },
                    "required": ["battery_make", "replacement_date", "voltage", "water_level", "damage", "leak", "description"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_exterior_damage(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_exterior_damage",
                "description": "Extract all the information about the damage to the exterior of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "damage": {"type": "string", "description": "Extract any information about damage or rust or dent to the exterior and assign it a label from [Yes, No]. If the exterior has been damaged or rusted or dented, assign Yes else assign No. Store and return the label only."},
                    },
                    "required": ["damage"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_exterior_oil_leak(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_exterior_oil_leak",
                "description": "Extract all the information about leakage of oil in the suspension of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "oil_leak": {"type": "string", "description": "Extract any information about oil leak from the suspension and assign it a label from [Yes, No]. If the oil is leaking from suspension, assign Yes else assign No. Store and return the label only."},
                    },
                    "required": ["oil_leak"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response



def check_exterior(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_exterior_info",
                "description": "Extract all the information about the exterior of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "damage":      {"type": "string", "description": "Extract any information about damage or rust or dent to the exterior and assign it a label from [Yes, No]. If the exterior has been damaged or rusted or dented, assign Yes else assign No. Store and return the label only."},
                        "oil_leak":    {"type": "string", "description": "Extract any information about oil leak from the suspension and assign it a label from [Yes, No]. If the oil is leaking from suspension, assign Yes else assign No. Store and return the label only."},
                        "description": {"type": "string", "description": "A short description of overall conditon of exterior"},
                    },
                    "required": ["damage", "oil_leak", "description"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_brake_fluid(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_brake_fluid_level",
                "description": "Extract all the information about the brake fluid level of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "fluid_level": {"type": "string", "description": "Extract the fluid level of the brakes and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                    "required": ["fluid_level"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_brake_condition(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the condition of tire and assign it a label based on your understanding. Assign the condition one of the labels : [Good, Ok, Needs Replacement]. If you are not sure, return NULL as condition. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_brake_condition",
            "description": "Extract the brake condition as given in text and assign it a label from [Good, Ok, Needs Replacement]",
            "input_schema": {
                "type": "object",
                "properties": {
                    "conditon": {"type": "string", "description": "Extract the brake condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                "required": ["condition"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response

def check_emergency_brake_condition(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the condition of tire and assign it a label based on your understanding. Assign the condition one of the labels : [Good, Ok, Needs Replacement]. If you are not sure, return NULL as condition. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_emergency_brake_condition",
            "description": "Extract the emergency brake condition as given in text and assign it a label from [Good, Ok, Low]",
            "input_schema": {
                "type": "object",
                "properties": {
                    "conditon": {"type": "string", "description": "Extract the emergency brake condition as given in text and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                    },
                "required": ["condition"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response

def check_brakes(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_brakes_info",
                "description": "Extract all the information about the brakes of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "front_conditon": {"type": "string", "description": "Extract the front brake condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "rear_conditon": {"type": "string", "description": "Extract the rear brake condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "emergency_conditon": {"type": "string", "description": "Extract the emergency brake condition as given in text and assign it a label from [Good, Ok, Needs Replacement]. If you are unsure or the information is not available in the text, return NULL."},
                        "fluid_level":      {"type": "string", "description": "Extract the fluid level of the brakes and assign it a label from [Good, Ok, Low]. If you are unsure or the information is not available in the text, return NULL."},
                        "description": {"type": "string", "description": "A short description of overall conditon of brakes"},
                    },
                    "required": ["front_condition", "rear_condition", "emergency_condition", "fluid_level", "description"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response

def check_engine_damage(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_engine_damage",
                "description": "Extract all the information about the damage to the engine of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "damage": {"type": "string", "description": "Extract any information about damage or rust or dent to the engine and assign it a label from [Yes, No]. If the exterior has been damaged or rusted or dented, assign Yes else assign No. Store and return the label only."},
                    },
                    "required": ["damage"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response
    
def check_engine_oil_leak(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_engine_oil_leak",
                "description": "Extract all the information about leakage of engine oil of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "oil_leak": {"type": "string", "description": "Extract any information about engine oil leak and assign it a label from [Yes, No]. If the oil is leaking from suspension, assign Yes else assign No. Store and return the label only."},
                    },
                    "required": ["oil_leak"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_engine_oil_condition(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_engine_oil_condition",
                "description": "Extract all the information about condition of engine oil of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "oil_condition": {"type": "string", "description": "Extract any information about the condition of the engine oil and assign it a label from [Good, Bad]. If the information is not available or you are unsure, return NULL."},
                    },
                    "required": ["oil_condition"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_brake_oil_condition(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_brake_oil_condition",
                "description": "Extract all the information about condition of brake oil of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "oil_condition": {"type": "string", "description": "Extract any information about the condition of the brake oil and assign it a label from [Good, Bad]. If the information is not available or you are unsure, return NULL."},
                    },
                    "required": ["oil_condition"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    return response

def check_engine_oil_color(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the condition of tire and assign it a label based on your understanding. Assign the condition one of the labels : [Good, Ok, Needs Replacement]. If you are not sure, return NULL as condition. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_engine_oil_color",
            "description": "Extract the information about engine oil color as given in text and assign it a label from [Clean, Black, Brown]",
            "input_schema": {
                "type": "object",
                "properties": {
                    "oil_color": {"type": "string", "description": "Extract the information about engine oil color as given in text and assign it a label from [Clean, Black, Brown]"}
                    },
                "required": ["oil_color"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response

def check_brake_oil_color(text):
    messages = [
        {
            "role": "user",
            "content": f"Extract the condition of tire and assign it a label based on your understanding. Assign the condition one of the labels : [Good, Ok, Needs Replacement]. If you are not sure, return NULL as condition. The text is : {text}"
        }
    ]
    
    response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=128,
    messages=messages,
    tools=[
        {
            "name": "extract_brake_oil_color",
            "description": "Extract the information about brake oil color as given in text and assign it a label from [Clean, Black, Brown]",
            "input_schema": {
                "type": "object",
                "properties": {
                    "oil_color": {"type": "string", "description": "Extract the information about brake oil color as given in text and assign it a label from [Clean, Black, Brown]"}
                    },
                "required": ["oil_color"],
                },
            },
    ],
    tool_choice = {"type": "any"}
    )
    
    return response

def check_engine(text):
    messages = [
        {
            "role": "user",
            "content": f"""You are a helpful assistant for service technicians. Understand the following instructions very carefully and follow them in givign the output.
            Parse and understand the text properly and answer questions based only on the text. Use the provided tool and the instructions specified in the tools itself.
            The text is : {text}"""
        }
    ]
        
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=messages,
        tools=[
            {
                "name": "extract_engine_info",
                "description": "Extract all the information about the engine of the machine based on the text while following the parameter constraints",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "damage":                {"type": "string", "description": "Extract any information about damage or rust or dent to the engine and assign it a label from [Yes, No]. If the engine has been damaged or rusted or dented, assign Yes else assign No. Store and return the label only."},
                        "oil_leak":              {"type": "string", "description": "Extract any information about engine oil leak from the engine and assign it a label from [Yes, No]. If the engine oil is leaking from engine, assign Yes else assign No. Store and return the label only."},
                        "engine_oil_condition":  {"type": "string", "description": "Extract any information about the condition of the engine oil and assign it a label from [Good, Bad]. If the information is not available or you are unsure, return NULL."},
                        "brake_fluid_condition": {"type": "string", "description": "Extract any information about the condition of the brake fluid and assign it a label from [Good, Bad]. If the information is not available or you are unsure, return NULL."},
                        "engine_oil_color":      {"type": "string", "description": "Extract any information about the color of the engine oil and assign it a label from [Clean, Black, Brown]. If the information is not available or you are unsure, return and store NULL."},
                        "brake_fluid_color":     {"type": "string", "description": "Extract any information about the color of the brake fluid and assign it a label from [Clean, Black, Brown]. If the information is not available or you are unsure, return and store NULL."},
                        "description":           {"type": "string", "description": "A short description of overall conditon of brakes"},
                    },
                    "required": ["damage","oil_leak", "engine_oil_condition", "brake_fluid_condition", "engine_oil_color","brake_fluid_color", "description"],
                    },
            },
        ],
        tool_choice = {"type": "any"}
    )
    
    return response
    