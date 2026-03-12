import random
from django.core.management.base import BaseCommand
from products.models import Product, Category, Supplier
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates the database with massive grocery data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Initializing massive data population...')
        
        # 1. Suppliers
        suppliers_data = [
            ("Universal Robina Corporation (URC)", "Customer Service", "02-8633-7631", "info@urc.com.ph", "Quezon City"),
            ("Nestle Philippines", "Sales Dept", "02-8898-0001", "service@ph.nestle.com", "Makati City"),
            ("San Miguel Corporation", "Distributor", "02-8632-3000", "customercare@sanmiguel.com.ph", "Mandaluyong City"),
            ("CDO Foodsphere", "Sales Team", "02-8588-5900", "sales@cdo.com.ph", "Valenzuela City"),
            ("NutriAsia", "Marketing", "02-8812-6288", "hello@nutriasia.com", "Taguig City"),
            ("Monde Nissin", "Sales", "02-8759-7500", "connect@mondenissin.com", "Makati City"),
            ("Unilever Philippines", "Support", "02-8588-8800", "cec.philippines@unilever.com", "Taguig City"),
            ("Procter & Gamble", "Distributor", "02-8894-3955", "pg.support@pg.com", "Taguig City"),
            ("Alaska Milk Corporation", "Sales", "02-8840-4500", "consumer@alaskamilk.com", "Makati City"),
            ("Del Monte Philippines", "Sales", "02-8856-2888", "feedback@delmonte.com", "Taguig City"),
        ]
        
        created_suppliers = {}
        for name, person, phone, email, addr in suppliers_data:
            sup, _ = Supplier.objects.get_or_create(
                name=name,
                defaults={
                    'contact_person': person,
                    'phone': phone,
                    'email': email,
                    'address': addr
                }
            )
            created_suppliers[name] = sup
            self.stdout.write(f'Supplier: {name}')

        # 2. Categories with Icons
        categories_data = [
            ("Fresh Produce", "leaf", [
                "Vegetables", "Fruits", "Herbs & Spices", "Organic Produce"
            ]),
            ("Dairy & Eggs", "milk", [
                "Milk", "Cheese", "Butter & Margarine", "Yogurt", "Eggs", "Cream"
            ]),
            ("Meat & Seafood", "beef", [
                "Fresh Meat", "Processed Meat", "Frozen Meat", "Fresh Seafood", "Frozen Seafood"
            ]),
            ("Bakery & Bread", "croissant", [
                "Loaf Bread", "Pandesal", "Pastries", "Cakes", "Biscuits & Crackers"
            ]),
            ("Beverages", "cup-soda", [
                "Soft Drinks", "Juices", "Water", "Coffee & Tea", "Energy Drinks", "Alcohol", "Milk Drinks"
            ]),
            ("Canned Goods", "container", [ # replaced 'can' with 'container' for lucide
                "Canned Fish", "Canned Meat", "Canned Fruits", "Canned Vegetables", "Jams & Spreads"
            ]),
            ("Instant & Ready-to-Eat", "soup", [
                "Instant Noodles", "Instant Soup", "Instant Coffee", "Cup Noodles", "Ready-to-eat Meals"
            ]),
            ("Snacks & Sweets", "cookie", [
                "Chips", "Candies & Chocolates", "Nuts & Seeds", "Dried Fruits", "Popcorn", "Wafers"
            ]),
            ("Condiments & Sauces", "utensils-crossed", [
                "Soy Sauce & Fish Sauce", "Vinegar", "Cooking Oil", "Ketchup", "Hot Sauce", "Seasoning Mixes", "Salt & Sugar"
            ]),
            ("Grains, Rice & Pasta", "wheat", [
                "Rice", "Pasta", "Flour", "Cereals & Oats"
            ]),
            ("Frozen Foods", "snowflake", [
                "Ice Cream", "Frozen Vegetables", "Frozen Processed Foods", "Frozen Desserts", "Ice"
            ]),
            ("Personal Care", "smile", [
                "Bath Soap", "Shampoo", "Toothpaste", "Deodorant", "Feminine Care", "Baby Care", "Skincare"
            ]),
            ("Household", "home", [
                "Detergent", "Fabric Softener", "Dishwashing", "Cleaners", "Air Fresheners", "Tissue", "Trash Bags"
            ]),
            ("Health & Wellness", "heart-pulse", [
                "Vitamins", "First Aid", "Medicine", "Supplements"
            ]),
            ("Pet Care", "paw-print", [
                "Dog Food", "Cat Food", "Treats", "Accessories"
            ]),
            ("School & Office", "pencil", [
                "Paper", "Pens", "Glue", "Folders"
            ]),
             ("Kitchenware", "chef-hat", [
                "Containers", "Disposables", "Utensils", "Foil & Wrap"
            ]),
             ("Miscellaneous", "box", [
                "Batteries", "Candles", "Light Bulbs", "Charcoal"
            ]),
        ]

        cat_map = {}
        for main_name, icon, subs in categories_data:
            main_cat, _ = Category.objects.get_or_create(
                name=main_name,
                defaults={'icon_name': icon}
            )
            cat_map[main_name] = main_cat
            self.stdout.write(f'Category: {main_name}')
            
            for sub_name in subs:
                Category.objects.get_or_create(
                    name=sub_name,
                    defaults={'parent': main_cat, 'icon_name': icon}
                )

        # 3. Products
        # Helper to get supplier instance safely
        def get_sup(names_list):
            for n in names_list:
                if n in created_suppliers:
                    return created_suppliers[n]
            return None

        products_list = [
            # Beverages
            ("Coca-Cola 330ml Can", "BEV-001", 25.00, "Beverages", "Soft Drinks", "Universal Robina Corporation (URC)"),
            ("Coca-Cola 1.5L", "BEV-002", 65.00, "Beverages", "Soft Drinks", "Universal Robina Corporation (URC)"),
            ("Sprite 330ml Can", "BEV-003", 25.00, "Beverages", "Soft Drinks", "Universal Robina Corporation (URC)"),
            ("Royal True Orange 1.5L", "BEV-004", 55.00, "Beverages", "Soft Drinks", "Universal Robina Corporation (URC)"),
            ("Pepsi 330ml Can", "BEV-005", 25.00, "Beverages", "Soft Drinks", "San Miguel Corporation"),
            ("Mountain Dew 1.5L", "BEV-006", 60.00, "Beverages", "Soft Drinks", "San Miguel Corporation"),
            ("C2 Green Tea Apple 1L", "BEV-007", 35.00, "Beverages", "Juices", "Universal Robina Corporation (URC)"),
            ("Zest-O Dalandan 200ml", "BEV-008", 12.00, "Beverages", "Juices", "Universal Robina Corporation (URC)"),
            ("Minute Maid Orange 1L", "BEV-009", 50.00, "Beverages", "Juices", "Coca-Cola"), # Fallback needed
            ("Del Monte Pineapple Juice 1L", "BEV-010", 85.00, "Beverages", "Juices", "Del Monte Philippines"),
            ("Tropicana Juice Drink 1L", "BEV-011", 75.00, "Beverages", "Juices", "Pepsi"),
            ("Nature's Spring Distilled Water 500ml", "BEV-012", 10.00, "Beverages", "Water", "Nature's Spring"),
            ("Summit Drinking Water 1 Gallon", "BEV-013", 35.00, "Beverages", "Water", "Summit"),
            ("Absolute Distilled Drinking Water 350ml", "BEV-014", 8.00, "Beverages", "Water", "Universal Robina Corporation (URC)"),
            ("Nescafe 3-in-1 Original 28g", "BEV-015", 8.00, "Beverages", "Coffee & Tea", "Nestle Philippines"),
            ("Great Taste White Coffee 30g", "BEV-016", 9.00, "Beverages", "Coffee & Tea", "Universal Robina Corporation (URC)"),
            ("Kopiko Brown Coffee 30g", "BEV-017", 8.50, "Beverages", "Coffee & Tea", "Kopiko"),
            ("Milo Chocolate Drink Powder 300g", "BEV-018", 165.00, "Beverages", "Milk Drinks", "Nestle Philippines"),
            ("Bear Brand Powdered Milk Drink 300g", "BEV-019", 185.00, "Beverages", "Milk Drinks", "Nestle Philippines"),
            ("Birch Tree Powdered Milk 150g", "BEV-020", 95.00, "Beverages", "Milk Drinks", "Century Pacific"),
            ("Alaska Powdered Milk 300g", "BEV-021", 175.00, "Beverages", "Milk Drinks", "Alaska Milk Corporation"),
            ("Red Bull Energy Drink 250ml", "BEV-022", 65.00, "Beverages", "Energy Drinks", "Red Bull"),
            ("Sting Energy Drink 330ml", "BEV-023", 30.00, "Beverages", "Energy Drinks", "San Miguel Corporation"),
            ("Cobra Energy Drink 350ml", "BEV-024", 28.00, "Beverages", "Energy Drinks", "Asia Brewery"),
            ("San Miguel Pale Pilsen 330ml", "BEV-025", 45.00, "Beverages", "Alcohol", "San Miguel Corporation"),
            ("Red Horse Beer 500ml", "BEV-026", 55.00, "Beverages", "Alcohol", "San Miguel Corporation"),
            ("San Mig Light 330ml", "BEV-027", 42.00, "Beverages", "Alcohol", "San Miguel Corporation"),
            ("Emperador Light Brandy 350ml", "BEV-028", 85.00, "Beverages", "Alcohol", "Emperador"),
            ("Tanduay White Rum 350ml", "BEV-029", 75.00, "Beverages", "Alcohol", "Tanduay"),
            
            # Canned Goods
            ("Century Tuna Flakes in Oil 155g", "CAN-001", 32.00, "Canned Goods", "Canned Fish", "Century Pacific"),
            ("555 Sardines in Tomato Sauce 155g", "CAN-002", 18.00, "Canned Goods", "Canned Fish", "Century Pacific"),
            ("Ligo Sardines Red 155g", "CAN-003", 20.00, "Canned Goods", "Canned Fish", "Ligo"),
            ("Mega Sardines Green 155g", "CAN-004", 16.00, "Canned Goods", "Canned Fish", "Mega Global"),
            ("Argentina Corned Beef 150g", "CAN-005", 45.00, "Canned Goods", "Canned Meat", "Century Pacific"),
            ("Purefoods Corned Beef 150g", "CAN-006", 48.00, "Canned Goods", "Canned Meat", "San Miguel Corporation"),
            ("CDO Liver Spread 85g", "CAN-007", 22.00, "Canned Goods", "Canned Meat", "CDO Foodsphere"),
            ("Reno Liver Spread 85g", "CAN-008", 18.00, "Canned Goods", "Canned Meat", "Reno"),
            ("Spam Classic 340g", "CAN-009", 185.00, "Canned Goods", "Canned Meat", "Hormel"),
            ("Ma Ling Luncheon Meat 340g", "CAN-010", 95.00, "Canned Goods", "Canned Meat", "Ma Ling"),
            ("Smith Premium Vienna Sausage 130g", "CAN-011", 28.00, "Canned Goods", "Canned Meat", "CDO Foodsphere"),
            ("CDO Meat Loaf 150g", "CAN-012", 35.00, "Canned Goods", "Canned Meat", "CDO Foodsphere"),
            ("Del Monte Fruit Cocktail 432g", "CAN-013", 85.00, "Canned Goods", "Canned Fruits", "Del Monte Philippines"),
            ("Dole Pineapple Chunks 227g", "CAN-014", 55.00, "Canned Goods", "Canned Fruits", "Dole"),
            ("Del Monte Whole Kernel Corn 432g", "CAN-015", 65.00, "Canned Goods", "Canned Vegetables", "Del Monte Philippines"),
            ("Hunt's Pork & Beans 230g", "CAN-016", 32.00, "Canned Goods", "Canned Vegetables", "Universal Robina Corporation (URC)"),
            ("Jolly Mushroom Pieces & Stems 198g","CAN-017", 45.00, "Canned Goods", "Canned Vegetables", "Jolly"),
            ("Del Monte Tomato Sauce 250g", "CAN-018", 28.00, "Canned Goods", "Jams & Spreads", "Del Monte Philippines"),

            # Instant Noodles
            ("Lucky Me Pancit Canton Original", "INS-001", 10.00, "Instant & Ready-to-Eat", "Instant Noodles", "Monde Nissin"),
            ("Lucky Me Pancit Canton Chilimansi", "INS-002", 10.00, "Instant & Ready-to-Eat", "Instant Noodles", "Monde Nissin"),
            ("Lucky Me Instant Mami Beef", "INS-003", 8.50, "Instant & Ready-to-Eat", "Instant Soup", "Monde Nissin"),
            ("Lucky Me Instant Mami Chicken", "INS-004", 8.50, "Instant & Ready-to-Eat", "Instant Soup", "Monde Nissin"),
            ("Nissin Cup Noodles Beef", "INS-005", 25.00, "Instant & Ready-to-Eat", "Cup Noodles", "Monde Nissin"),
            ("Payless Pancit Canton", "INS-006", 7.00, "Instant & Ready-to-Eat", "Instant Noodles", "Universal Robina Corporation (URC)"),
            ("Nissin Yakisoba", "INS-007", 35.00, "Instant & Ready-to-Eat", "Instant Noodles", "Monde Nissin"),
            ("Korean Samyang Hot Chicken", "INS-008", 65.00, "Instant & Ready-to-Eat", "Instant Noodles", "Samyang"),
            ("Knorr Noodle Soup Chicken", "INS-009", 10.00, "Instant & Ready-to-Eat", "Instant Soup", "Unilever Philippines"),
            ("Maggi Magic Sarap 8g", "INS-010", 3.00, "Condiments & Sauces", "Seasoning Mixes", "Nestle Philippines"),
            ("Knorr Chicken Cube 10g", "INS-011", 5.00, "Condiments & Sauces", "Seasoning Mixes", "Unilever Philippines"),
            ("Knorr Sinigang sa Sampaloc Mix", "INS-012", 8.00, "Condiments & Sauces", "Seasoning Mixes", "Unilever Philippines"),
            ("Mama Sita's Caldereta Mix", "INS-013", 15.00, "Condiments & Sauces", "Seasoning Mixes", "Mama Sita"),

            # Snacks
            ("Chippy Chili & Cheese 110g", "SNK-001", 28.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Piattos Cheese 85g", "SNK-002", 30.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Nova Multigrain Snack 78g", "SNK-003", 18.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Oishi Prawn Crackers 60g", "SNK-004", 15.00, "Snacks & Sweets", "Chips", "Oishi"),
            ("Roller Coaster Potato Rings", "SNK-005", 25.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("V-Cut Spicy Barbecue 85g", "SNK-006", 28.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Clover Chips Cheese 85g", "SNK-007", 25.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Lay's Classic 85g", "SNK-008", 45.00, "Snacks & Sweets", "Chips", "Frito Lay"),
            ("Pringles Original 110g", "SNK-009", 95.00, "Snacks & Sweets", "Chips", "Pringles"),
            ("Jack 'n Jill Potato Chips", "SNK-010", 22.00, "Snacks & Sweets", "Chips", "Universal Robina Corporation (URC)"),
            ("Pillows Chocolate 38g", "SNK-011", 12.00, "Snacks & Sweets", "Candies & Chocolates", "Oishi"),
            ("Rebisco Crackers 10s", "SNK-012", 15.00, "Snacks & Sweets", "Biscuits & Crackers", "Rebisco"),
            ("SkyFlakes Crackers 10s", "SNK-013", 18.00, "Snacks & Sweets", "Biscuits & Crackers", "Monde Nissin"),
            ("Fita Crackers 10s", "SNK-014", 16.00, "Snacks & Sweets", "Biscuits & Crackers", "Monde Nissin"),
            ("Cream-O Chocolate 132g", "SNK-015", 20.00, "Snacks & Sweets", "Biscuits & Crackers", "Universal Robina Corporation (URC)"),
            ("Oreo Cookies 137g", "SNK-016", 45.00, "Snacks & Sweets", "Biscuits & Crackers", "Mondelez"),
            ("Choco Mucho 33g", "SNK-017", 12.00, "Snacks & Sweets", "Candies & Chocolates", "Rebisco"),
            ("Flat Tops Chocolate 24s", "SNK-018", 35.00, "Snacks & Sweets", "Candies & Chocolates", "Ricoa"),
            ("Cadbury Dairy Milk 65g", "SNK-019", 65.00, "Snacks & Sweets", "Candies & Chocolates", "Mondelez"),
            ("Goya Milk Chocolate 40g", "SNK-020", 25.00, "Snacks & Sweets", "Candies & Chocolates", "Goya"),

            # Rice & Grains
            ("Sinandomeng Rice 1kg", "GRN-001", 55.00, "Grains, Rice & Pasta", "Rice", "Generic"),
            ("Jasmine Rice 1kg", "GRN-002", 60.00, "Grains, Rice & Pasta", "Rice", "Generic"),
            ("Dinorado Rice 1kg", "GRN-003", 65.00, "Grains, Rice & Pasta", "Rice", "Generic"),
            ("Brown Rice 1kg", "GRN-004", 75.00, "Grains, Rice & Pasta", "Rice", "Generic"),
            ("Del Monte Spaghetti Pasta 900g", "GRN-005", 85.00, "Grains, Rice & Pasta", "Pasta", "Del Monte Philippines"),
            ("Royal Pasta Elbow Macaroni 400g", "GRN-006", 45.00, "Grains, Rice & Pasta", "Pasta", "Universal Robina Corporation (URC)"),
            ("Quaker Oats 400g", "GRN-007", 125.00, "Grains, Rice & Pasta", "Cereals & Oats", "Quaker"),
            
            # Condiments
            ("Silver Swan Soy Sauce 385ml", "CND-001", 28.00, "Condiments & Sauces", "Soy Sauce & Fish Sauce", "NutriAsia"),
            ("Datu Puti Soy Sauce 385ml", "CND-002", 26.00, "Condiments & Sauces", "Soy Sauce & Fish Sauce", "NutriAsia"),
            ("UFC Banana Ketchup 320g", "CND-003", 35.00, "Condiments & Sauces", "Ketchup", "NutriAsia"),
            ("Del Monte Tomato Ketchup 320g", "CND-004", 38.00, "Condiments & Sauces", "Ketchup", "Del Monte Philippines"),
            ("Lady's Choice Mayonnaise 220ml", "CND-005", 55.00, "Condiments & Sauces", "Ketchup", "Unilever Philippines"),
            ("Datu Puti Vinegar 385ml", "CND-006", 18.00, "Condiments & Sauces", "Vinegar", "NutriAsia"),
            ("Silver Swan Vinegar 385ml", "CND-007", 20.00, "Condiments & Sauces", "Vinegar", "NutriAsia"),
            ("Mama Sita's Oyster Sauce 405g", "CND-008", 55.00, "Condiments & Sauces", "Soy Sauce & Fish Sauce", "Mama Sita"),
            ("NutriAsia Golden Fiesta Palm Oil", "CND-009", 85.00, "Condiments & Sauces", "Cooking Oil", "NutriAsia"),
            ("Minola Premium Corn Oil 1L", "CND-010", 125.00, "Condiments & Sauces", "Cooking Oil", "Minola"),
            ("Baguio Cooking Oil 1L", "CND-011", 95.00, "Condiments & Sauces", "Cooking Oil", "Baguio Oil"),
            ("Ajinomoto Umami Seasoning 100g", "CND-012", 25.00, "Condiments & Sauces", "Seasoning Mixes", "Ajinomoto"),
            ("McCormick Black Pepper 35g", "CND-013", 45.00, "Condiments & Sauces", "Salt & Sugar", "McCormick"),
            ("Iodized Salt 1kg", "CND-014", 20.00, "Condiments & Sauces", "Salt & Sugar", "Generic"),
            ("White Sugar 1kg", "CND-015", 60.00, "Condiments & Sauces", "Salt & Sugar", "Generic"),
            ("Brown Sugar 1kg", "CND-016", 65.00, "Condiments & Sauces", "Salt & Sugar", "Generic"),
            ("Pillsbury All-Purpose Flour 1kg", "CND-017", 55.00, "Grains, Rice & Pasta", "Flour", "Pillsbury"),

            # Dairy
            ("Alaska Evaporada 370ml", "DAI-001", 42.00, "Dairy & Eggs", "Milk", "Alaska Milk Corporation"),
            ("Carnation Evaporated Milk 370ml", "DAI-002", 45.00, "Dairy & Eggs", "Milk", "Nestle Philippines"),
            ("Nestlé All Purpose Cream 250ml", "DAI-003", 42.00, "Dairy & Eggs", "Cream", "Nestle Philippines"),
            ("Alaska Condensada 300ml", "DAI-004", 48.00, "Dairy & Eggs", "Cream", "Alaska Milk Corporation"),
            ("Eden Cheese 165g", "DAI-005", 75.00, "Dairy & Eggs", "Cheese", "Mondelez"),
            ("Kraft Cheddar Cheese Singles", "DAI-006", 95.00, "Dairy & Eggs", "Cheese", "Mondelez"),
            ("Anchor Butter 227g", "DAI-007", 185.00, "Dairy & Eggs", "Butter & Margarine", "Anchor"),
            ("Magnolia Chicken Spread", "DAI-008", 65.00, "Dairy & Eggs", "Butter & Margarine", "San Miguel Corporation"),
            ("Nestle Fresh Milk 1L", "DAI-009", 95.00, "Dairy & Eggs", "Milk", "Nestle Philippines"),
            ("Selecta Ice Cream 1.5L", "DAI-010", 285.00, "Frozen Foods", "Ice Cream", "Unilever Philippines"),

            # Personal Care
            ("Safeguard Bar Soap Classic", "PER-001", 32.00, "Personal Care", "Bath Soap", "Procter & Gamble"),
            ("Dove Beauty Bar 135g", "PER-002", 55.00, "Personal Care", "Bath Soap", "Unilever Philippines"),
            ("Palmolive Naturals Bar Soap", "PER-003", 18.00, "Personal Care", "Bath Soap", "Colgate-Palmolive"),
            ("Lifebuoy Bar Soap 80g", "PER-004", 15.00, "Personal Care", "Bath Soap", "Unilever Philippines"),
            ("Sunsilk Shampoo 180ml", "PER-005", 65.00, "Personal Care", "Shampoo", "Unilever Philippines"),
            ("Pantene Shampoo 180ml", "PER-006", 85.00, "Personal Care", "Shampoo", "Procter & Gamble"),
            ("Head & Shoulders Shampoo 180ml", "PER-007", 95.00, "Personal Care", "Shampoo", "Procter & Gamble"),
            ("Cream Silk Conditioner 180ml", "PER-008", 75.00, "Personal Care", "Shampoo", "Unilever Philippines"),
            ("Colgate Total Toothpaste 150g", "PER-009", 95.00, "Personal Care", "Toothpaste", "Colgate-Palmolive"),
            ("Close-Up Toothpaste 160g", "PER-010", 65.00, "Personal Care", "Toothpaste", "Unilever Philippines"),
            ("Oral-B Toothbrush Classic", "PER-011", 45.00, "Personal Care", "Toothpaste", "Procter & Gamble"),
            ("Rexona Deodorant Roll-On 40ml", "PER-012", 85.00, "Personal Care", "Deodorant", "Unilever Philippines"),
            ("Nivea Deodorant Spray 150ml", "PER-013", 125.00, "Personal Care", "Deodorant", "Nivea"),
            ("Whisper Ultra Thin 8s", "PER-014", 45.00, "Personal Care", "Feminine Care", "Procter & Gamble"),
            ("Modess All Night 8s", "PER-015", 42.00, "Personal Care", "Feminine Care", "Johnson & Johnson"),
            ("Kotex Soft & Smooth 8s", "PER-016", 38.00, "Personal Care", "Feminine Care", "Kimberly-Clark"),
            ("EQ Baby Diaper Small 4s", "PER-017", 28.00, "Personal Care", "Baby Care", "JS Unitrade"),
            ("Pampers Baby Dry Medium 4s", "PER-018", 55.00, "Personal Care", "Baby Care", "Procter & Gamble"),
            ("Johnson's Baby Powder 100g", "PER-019", 75.00, "Personal Care", "Baby Care", "Johnson & Johnson"),
            ("Human Nature Sunflower Oil", "PER-020", 185.00, "Personal Care", "Skincare", "Human Nature"),

            # Household
            ("Tide Powder Detergent 110g", "HSE-001", 12.00, "Household", "Detergent", "Procter & Gamble"),
            ("Ariel Powder Detergent 110g", "HSE-002", 13.00, "Household", "Detergent", "Procter & Gamble"),
            ("Champion Detergent Bar 140g", "HSE-003", 10.00, "Household", "Detergent", "Champion"),
            ("Surf Powder Detergent 750g", "HSE-004", 85.00, "Household", "Detergent", "Unilever Philippines"),
            ("Downy Fabric Softener 375ml", "HSE-005", 55.00, "Household", "Fabric Softener", "Procter & Gamble"),
            ("Joy Dishwashing Liquid 250ml", "HSE-006", 35.00, "Household", "Dishwashing", "Procter & Gamble"),
            ("Sunlight Dishwashing Liquid 250ml", "HSE-007", 32.00, "Household", "Dishwashing", "Unilever Philippines"),
            ("Zonrox Bleach 500ml", "HSE-008", 28.00, "Household", "Cleaners", "Green Cross"),
            ("Domex Toilet Bowl Cleaner 500ml", "HSE-009", 48.00, "Household", "Cleaners", "Unilever Philippines"),
            ("Mr. Muscle Glass Cleaner 500ml", "HSE-010", 75.00, "Household", "Cleaners", "SC Johnson"),
            ("Lysol Disinfectant Spray 170g", "HSE-011", 185.00, "Household", "Cleaners", "Reckitt"),
            ("Glade Air Freshener 300ml", "HSE-012", 125.00, "Household", "Air Fresheners", "SC Johnson"),
            ("Scotch Brite Sponge 1pc", "HSE-013", 22.00, "Household", "Dishwashing", "3M"),
            ("Glad Trash Bag Large 10s", "HSE-014", 65.00, "Household", "Trash Bags", "Glad"),
            ("Bounty Paper Towel 2 Rolls", "HSE-015", 95.00, "Household", "Tissue", "Tissue"),
        ]

        count = 0
        for name, sku, price, main_cat_name, sub_cat_name, text_supplier in products_list:
            # Determine logic Category
            # Try to fetch sub-category, if not, fallback to main
            cat_obj = Category.objects.filter(name=sub_cat_name).first()
            if not cat_obj:
                cat_obj = cat_map.get(main_cat_name)
            
            # Identify Supplier
            sup_obj = None
            if text_supplier in created_suppliers:
                sup_obj = created_suppliers[text_supplier]
            # Naive match if fuzzy
            else:
                for k, v in created_suppliers.items():
                    if text_supplier.split()[0] in k:
                        sup_obj = v
                        break

            # Create Product
            if not Product.objects.filter(sku=sku).exists():
                cost = price * 0.7 # Approximate cost
                Product.objects.create(
                    name=name,
                    sku=sku,
                    category=cat_obj,
                    supplier=sup_obj,
                    cost_price=cost,
                    selling_price=price,
                    current_stock=random.randint(5, 50),
                    reorder_level=10,
                    reorder_quantity=20,
                    description=f"Standard {name}",
                    is_active=True,
                    unit_of_measure='pcs' # default
                )
                self.stdout.write(f'Created: {name}')
                count += 1
            else:
                 self.stdout.write(f'Skipped (Exists): {name}')

        self.stdout.write(self.style.SUCCESS(f'Done! Added {count} new products.'))
