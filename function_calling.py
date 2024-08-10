import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)


def check_tire_pressure(text):
    class TirePressure(TypedDict):
        pressure: float
    
    def declaredFunction(
        pressure: list[TirePressure]
    ):
        pass
    
    model = genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    tools = [declaredFunction])

    result = model.generate_content(f"""
    {text}

    Please parse the text, understand it and then store the tire pressure from text in class as mentioned in the declared function.
    If you are not confident about the tire pressure value being mentioned in the text, store the tire pressure in class as -1.
    Do not give an empty class or value not mentioned in the text.
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result


def check_tire_condition(text):
    class TireCondition(TypedDict):
        condition: str
    
    def declaredFunction(
        condition: list[TireCondition]
    ):
        pass
    
    model = genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    tools = [declaredFunction])

    result = model.generate_content(f"""
    You are an AI assistant specializing in tire evaluations. Your task is to classify the condition of tires based on input text. Assign each description to one of these three categories: "Good", "Ok", or "Needs Replacement".
    DO NOT RETURN THE ORIGINAL TEXT UNDER ANY CIRCUMSTANCE.
    THE OUTPUT SHOULD BE ONE OF GOOD, OK, NEEDS REPLACEMENT ONLY.
    Here are some examples for you to learn how to classify:

    Text: The tire is functioning perfectly.
    Answer: Good
    Text: The tire has some wear but still seems safe.
    Answer: Ok
    Text: The tire needs to be discarded.
    Answer: Needs Replacement
    

    Now based on the above examples, return the classification for the below text. If you return a value outside of Good, Ok or Need Replacement, you will lose your tire inspector job.
    {text}
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result

def check_battery_make(text):
    class BatteryMake(TypedDict):
        maker: str
    
    def declaredFunction(
        maker: list[BatteryMake]
    ):
        pass
    
    model = genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    tools = [declaredFunction])

    result = model.generate_content(f"""
    {text}

    Please parse the text, understand it and then store the battery maker from text in class as mentioned in the declared function.
    Store only the maker of the battery. Under no circumstance should you store the complete string. For example : 
    
    Text : The battery was made by Caterpillar.
    Answer: Caterpillar
    
    You are supposed to store only the Answer.
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result

def check_battery_replacement_date(text):
    class ReplacementDate(TypedDict):
        replacementDate: str
    
    def declaredFunction(
        replacementDate: list[ReplacementDate]
    ):
        pass
    
    model = genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    tools = [declaredFunction])

    result = model.generate_content(f"""
    {text}

    Please parse the text, understand it and then store the date from text in class as mentioned in the declared function.
    Store only the date from the text and not the unnecessary part of text. If you are not sure about date being mentioned in the text, return NULL.
    Store the date in DD/MM/YY format. 
    Make sure only to retrieve the replacement date and not any other date.
    I only need the replacement date. If manafacture date is mentioned, IGNORE IT.
    Do not give an empty class or value not mentioned in the text.
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result

def check_battery_volt(text):
    class BatteryVoltage(TypedDict):
        voltage: int
    
    def declaredFunction(
        voltage: list[BatteryVoltage]
    ):
        pass
    
    model = genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    tools = [declaredFunction])

    result = model.generate_content(f"""
    {text}

    Please parse the text, understand it and then store the battery voltage from text in class as mentioned in the declared function.
    If you are not confident about the battery voltage value being mentioned in the text, store the battery voltage in class as -1.
    Do not give an empty class or value not mentioned in the text.
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result

def check_battery_damage(text):
    class BatteryDamage(TypedDict):
        damage: bool
        
    def declaredFunction(
        damange: list[BatteryDamage]
    ):
        pass
    model = genai.GenerativeModel(
        model_name='models/gemini-1.5-pro-latest',
        tools= [declaredFunction]
    )
    
    result = model.generate_content(f"""
    You work as an assistant to a battery service man. Based on the given text by the service man, store if battery has been damanged,
    in class as mentioned in the declared function.
    Answer in true/false ONLY. Answer only on the basis of the below text : 
    {text}                                
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result

def check_battery_leak(text):
    class BatteryLeak(TypedDict):
        leak: bool
        
    def declaredFunction(
        leak: list[BatteryLeak]
    ):
        pass
    model = genai.GenerativeModel(
        model_name='models/gemini-1.5-pro-latest',
        tools= [declaredFunction]
    )
    
    result = model.generate_content(f"""
    You work as an assistant to a battery service man. Based on the given text by the service man, store if battery is leaking or is rusted,
    in class as mentioned in the declared function.
    Make sure to accurately label it as leaking/rusting or not based on the input text.
    Answer in true/false ONLY. Answer only on the basis of the below text : 
    {text}                                
    """,
    tool_config={'function_calling_config':'ANY'}
    )
    
    return result