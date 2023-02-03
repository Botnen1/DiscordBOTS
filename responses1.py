import random as rnd

def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "Hey på dei!"
    
    if p_message == "roll":
        return str(rnd.randint(1, 6))
    
    if p_message == "help me bot":
        return "`YOU WANT ME TO HELP YOU?\nHOW ABOUT MABYE THIS TIME, YOU HELP YOURSELF???`"
    
    if p_message == "kristian huuse":
        return "`HUUSE ER EN TØFF KAR`"