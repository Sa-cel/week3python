def calculate_discount(price, discount_percent):
    #check if the discount is 20% or higher
    if discount_percent >= 20:
        #calculate te final price after applying the discount
        final_price = price - (price * discount_percent/100)
        return final_price
    else:
        # retun the original price of te discount is less than 20%
        return price
    
# prompt the user to enter the original price
price = float(input("Enter the original price of the item: "))


#prompt the user to enter the dicount percentage
discount_percentage = float(input("enter the discount percentage: "))

# calculate the final price
final_price = calculate_discount(price, discount_percent)

#print the final price
print(f"The final price after applying the discount is: {final_price}")