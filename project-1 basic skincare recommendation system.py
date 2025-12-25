# Enter customer information
name = input("What is your name? ")
age = input("How old are you? ")
goal = input("What is your skincare goal? ")

# Provide skincare recommendation based on their goal
recommendations = {
"brighten" : "Vitamin C or Niacinamide",
"moisturize" : "Hyaluronic Acid",
"wrinkles" : "Retinol"}
recommendation = None
for keyword, rec in recommendations.items():
    if keyword in goal:
        recommendation = rec
if recommendation:
    print(recommendation)
else:
    print("No specific recommendation found. Try: 'To brighten skin', 'to moisturize skin', 'to reduce wrinkles'.")




