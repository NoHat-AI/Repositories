menu_item = "Pizza"
guests = 10
# Ask user to input # of guests and food item on menu
guests = int(input("Enter Number of Guests: "))
menu_item = input("What item is on the menu? ")
print("\nThere will be " + str(guests) + " attending.")
print("Updated menu item is: " + menu_item)

# Check if there is enough food for everyone. 
biryani_per_person = 1
biryani_needed = biryani_per_person * guests
biryani_prepared = int(input("\nHow many people can we feed with our current food supply? (Enter 0 if none) "))
enough_biryani = biryani_needed - biryani_prepared

if enough_biryani <= 0:
 print("\nThere is enough food for everyone!")
else:
 print("\nOrder food for " + (str(enough_biryani)) + " more people!")

# biryani_per_guest = biryani_prepared/guests

