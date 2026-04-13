
def get_number(number):
    while True:
        try:
            value = float(input(number))
            return value
        except ValueError:
            print("Invalid Input,please type a number")





No200_sieve_passing_soil = get_number("Passed Material Percentage (No. 200): ")
No4_sieve_passing_soil = get_number("Passed Material Percentage (No. 4): ")

Liquid_Limit = get_number("LL: ")
Plastic_Limit = get_number("PL: ")
Liquid_Limit_oven_dried = get_number("Enter Oven Dried Liquid Limit: ")

Cc = get_number("Cc: ")
Cu = get_number("Cu: ")


Plasticity_Index = Liquid_Limit - Plastic_Limit
A_Line = 0.73 * (Liquid_Limit - 20)



if No200_sieve_passing_soil > 50:

   
    if Liquid_Limit < 50:
        if Liquid_Limit_oven_dried / Liquid_Limit < 0.75:
            print("Soil class is OL")
        else:
            if Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                print("Soil class is CL")
            elif 4 <= Plasticity_Index <= 7 and Plasticity_Index >= A_Line:
                print("Soil class is CL-ML")
            elif Plasticity_Index < 4 or Plasticity_Index < A_Line:
                print("Soil class is ML")

  
    elif Liquid_Limit >= 50:
        if Liquid_Limit_oven_dried / Liquid_Limit < 0.75:
            print("Soil class is OH")
        else:
            if Plasticity_Index >= A_Line:
                print("Soil class is CH")
            elif Plasticity_Index < A_Line:
                print("Soil class is MH")



elif No200_sieve_passing_soil <= 50:
    
    Gravel_Percentage = 100 - No4_sieve_passing_soil
    Sand_Percentage = No4_sieve_passing_soil - No200_sieve_passing_soil
    
  
    if Gravel_Percentage > Sand_Percentage:
        
       
        if No200_sieve_passing_soil < 5:
            if Cu >= 4 and 1 <= Cc <= 3:
                print("Soil class is GW")
            elif Cu < 4 or Cc < 1 or Cc > 3:
                print("Soil class is GP")

        
        elif 5 <= No200_sieve_passing_soil <= 12:
            if Cu >= 4 and 1 <= Cc <= 3: 
                if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                    print("Soil class is GW-GM")
                elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                    print("Soil class is GW-GC")
            elif Cu < 4 or Cc < 1 or Cc > 3: 
                if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                    print("Soil class is GP-GM")
                elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                    print("Soil class is GP-GC")


        elif No200_sieve_passing_soil > 12:
            if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                print("Soil class is GM")
            elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                print("Soil class is GC")
            elif 4 <= Plasticity_Index <= 7 and Plasticity_Index >= A_Line:
                print("Soil class is GC-GM")


   
    else:
        
       
        if No200_sieve_passing_soil < 5:
            if Cu >= 6 and 1 <= Cc <= 3: 
                print("Soil class is SW")
            elif Cu < 6 or Cc < 1 or Cc > 3:
                print("Soil class is SP")
        
        
        elif 5 <= No200_sieve_passing_soil <= 12:
            if Cu >= 6 and 1 <= Cc <= 3: 
                if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                    print("Soil class is SW-SM")
                elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                    print("Soil class is SW-SC")
            elif Cu < 6 or Cc < 1 or Cc > 3: 
                if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                    print("Soil class is SP-SM")
                elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                    print("Soil class is SP-SC")
        
        
        elif No200_sieve_passing_soil > 12:
            if Plasticity_Index < 4 or Plasticity_Index < A_Line:
                print("Soil class is SM")
            elif Plasticity_Index > 7 and Plasticity_Index >= A_Line:
                print("Soil class is SC")
            elif 4 <= Plasticity_Index <= 7 and Plasticity_Index >= A_Line:
                print("Soil class is SC-SM")