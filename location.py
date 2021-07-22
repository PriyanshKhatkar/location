import webbrowser

query = str(input("enter the location"))    
location = query
print(f"User asked to Locate{location}")
webbrowser.open("https://www.google.com/maps/place/"  + location + "")
    

    



