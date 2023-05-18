import datetime
from . import models
from django.test import TestCase
from django.urls import reverse

class TestViews (TestCase):
    
    def setUp (self):       
        
        self.date = datetime.datetime.now()
        
        # Create lotteries
        self.lottery_name_a = "sample lottery a"
        self.lottery_name_b = "sample lottery b"
        self.lottery_details = "sample details"
        self.lottery_end_date = "2023-01-01"
        self.lottery_total_price = 1000
        self.lottery_image = "https://i.imgur.com/OSCNqOt.jpg"
        self.lottery_numbers = 100
        self.lottery_is_open = True
        
        self.lottery_a = models.Lottery.objects.create (
            name = self.lottery_name_a,
            details = self.lottery_details,
            total_price = self.lottery_total_price,
            image = self.lottery_image,
            end_date = self.date,
            numbers = self.lottery_numbers,
            is_open = self.lottery_is_open,
        )
        
        self.lottery_b = models.Lottery.objects.create (
            name = self.lottery_name_b,
            details = self.lottery_details,
            total_price = self.lottery_total_price,
            image = self.lottery_image,
            end_date = self.date,
            numbers = self.lottery_numbers,
            is_open = self.lottery_is_open,
        )
        
        # Create tickets
        self.ticket = models.Ticket.objects.create (
            lottery = self.lottery_a,
            number = 1,
            buyer_name = "sample buyer",
            buyer_email = "sample@gmail.com",
            buy_at = self.date,
            is_paid = False,
            active = True,            
        )
        
    def test_get_lotteries (self):
        """ Test endpoint who return all lotteries data """
        
        response = self.client.get (reverse ('lottery_get_lotteries'))
        
        # Validate response status
        self.assertEqual (response.status_code, 200)
        
        # Validate response lotteries
        self.assertEqual (len(response.json()), 2)
        
        # Validate lottery a
        self.assertEqual (response.json()[0]["title"], self.lottery_name_a)
        self.assertEqual (response.json()[0]["description"], self.lottery_details)
        self.assertEqual (response.json()[0]["date"], self.date.strftime ("%d/%m/%Y"))
        self.assertEqual (response.json()[0]["image"], self.lottery_image)
        self.assertEqual (len(response.json()[0]["numbers"]), self.lottery_numbers - 1)
        self.assertEqual (float(response.json()[0]["price"]), round(self.lottery_total_price / self.lottery_numbers, 2))
        
        # Validate lottery b
        self.assertEqual (response.json()[1]["title"], self.lottery_name_b)
        self.assertEqual (response.json()[1]["description"], self.lottery_details)
        self.assertEqual (response.json()[1]["date"], self.date.strftime ("%d/%m/%Y"))
        self.assertEqual (response.json()[1]["image"], self.lottery_image)
        self.assertEqual (len(response.json()[1]["numbers"]), self.lottery_numbers)
        self.assertEqual (float(response.json()[1]["price"]), round(self.lottery_total_price / self.lottery_numbers, 2))
        