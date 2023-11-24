import pygsheets 

# Create the Client 
# Enter the name of the downloaded KEYS file in service_account_file 
client = pygsheets.authorize(service_account_file="linkedin-scrapper-405914-90250fc9ee1d.json") 

spreadsht = client.open("LinkedIn-data") 
  
# opens a worksheet by its name/title 
worksht = spreadsht.worksheet("title", "Sheet1") 
  
# Now, let's add data to our worksheet 
  
# Creating the first column 
worksht.cell("A1").set_text_format("bold", True).value = "Item"
  
# if updating multiple values, the data 
# should be in a matrix format 
worksht.update_values("A2:A6", [["Pencil"], ["Eraser"],  
                                ["Sharpener"], ["Ruler"],  
                                ["Pen"]])  # Adding row values 
  
# Similarly, creating the second column 
worksht.cell("B1").set_text_format("bold", True).value = "Price"
worksht.update_values("B2:B6", [[5], [3], [5], [15], [10]]) 
  
# Creating a basic bar chart 
worksht.add_chart(("A2", "A6"), [("B2", "B6")], "Shop")