'''
Program name: Beverage Wholesale Scenario
Description: Calculate the selected beverage quantity and price and displaying the details
Authors: Chin Tan, Nhi Vuu and Sid Ali Bounab
Date: Feb 05, 2026
'''

#Declaring the constants
BAGS_PER_BOX = 20
TEA_PRICE_PER_BAG = 0.45
COF_PRICE_PER_KG = 18.5
TEA_DISC_THRE = 10
COF_DISC_THRE = 25
TEA_DISC_RATE = 0.15
COF_DISC_RATE = 0.1

#Displaying the welcome message and the beverage selection
print('-'*47)
print('*** Welcome to Beverage Wholesale Program! ***')
print('-'*47)
print('Please select the type of purchase:')
print('C: Coffee Beans')
print('T: Tea Boxes')

#Checking if the beverage entry is correct
customer_order = input('>>> ').lower()
if customer_order != ('c') and customer_order != ('t'):
    print('Invalid input, you should enter c/C or t/T')
    exit()

#The coffee part
elif customer_order == ('c'):
    no_cof_kg = float(input('Enter the number of kilograms (kg) of coffee: '))
    if no_cof_kg <= 0:
        print('Quantity of coffee should be > 0')
        exit()
    
    #Calculating the coffe price according to the province, and displaying the details
    else:
        province = input('Please enter the 2-letter province abbreviation: ').lower()
        if province == ('ab') or province == ('bc'):
            gst_rate = 0.05
            if no_cof_kg <= COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_cof_kg > COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc * (1-COF_DISC_RATE)
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
        elif province == ('on'):
            gst_rate = 0.13
            if no_cof_kg <= COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_cof_kg > COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc * (1-COF_DISC_RATE)
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
        elif province != ('ab') and province != ('bc') and province != ('on'):
            gst_rate = 0.15
            if no_cof_kg <= COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_cof_kg > COF_DISC_THRE:
                cof_price_bef_disc = no_cof_kg * COF_PRICE_PER_KG
                cof_price_aft_disc = cof_price_bef_disc * (1-COF_DISC_RATE)
                gst = cof_price_aft_disc * gst_rate
                tot_cof_price = cof_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Coffee':^7}{no_cof_kg:^32.2f}{cof_price_bef_disc:^20.2f}{cof_price_aft_disc:^33.2f}{gst:^4.2f}{tot_cof_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')

#The tea part
elif customer_order == ('t'):
    no_tea_box = float(input('Enter the number of boxes of tea: '))
    if no_tea_box <= 0:
        print('Number of tea boxes should be > 0')
        exit()

    #Calculating the tea price according to the province, and displaying the details
    else:
        province = input('Please enter the 2-letter province abbreviation: ').lower()
        if province == ('ab') or province == ('bc'):
            gst_rate = 0.05
            if no_tea_box <= TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_tea_box > TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc * (1-COF_DISC_RATE)
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
        elif province == ('on'):
            gst_rate = 0.13
            if no_tea_box <= TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_tea_box > TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc * (1-COF_DISC_RATE)
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
        elif province != ('ab') and province != ('bc') and province != ('on'):
            gst_rate = 0.15
            if no_tea_box <= TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')
            elif no_tea_box > TEA_DISC_THRE:
                tea_price_bef_disc = no_tea_box * TEA_PRICE_PER_BAG
                tea_price_aft_disc = tea_price_bef_disc * (1-COF_DISC_RATE)
                gst = tea_price_aft_disc * gst_rate
                tot_tea_price = tea_price_aft_disc + gst
                print('-'*122)
                print('Product', 'Qty (Bags/kg)', 'Price Before Disc', 'Price After Disc', 'GST', 'Total Price', sep=' '*10)
                print(f'{'Tea':^7}{no_tea_box:^32.2f}{tea_price_bef_disc:^20.2f}{tea_price_aft_disc:^33.2f}{gst:^4.2f}{tot_tea_price:^28.2f}')
                print('-'*122)
                print('Thanks for your business, Good Bye')        
