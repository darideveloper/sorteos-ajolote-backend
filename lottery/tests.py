import os
import json
from . import models
from crons import disable_tickets
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from sorteosajolote import settings

DELETE_HOURS = int(os.getenv ("DISABLE_HOURS"))

class TestViews (TestCase):
    
    def setUp (self):       
        
        # Endpoints
        self.endpoint_get_lotteries = reverse ('lottery_get_lotteries')
        self.endpoint_save_ticket = reverse ('lottery_save_tickets')
        
        # Get current datetime with timezone
        
        # Create lotteries
        self.date = timezone.now().astimezone ()
        self.lottery_name_a = "sample lottery a"
        self.lottery_name_b = "sample lottery b"
        self.lottery_details = "sample details"
        self.lottery_end_date = "2023-01-01"
        self.lottery_total_price = 1000
        self.lottery_image = "sample.jpg"
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
        
        # Tickets data
        self.user_name = "sample user"
        self.user_phone = "4491234567"
        self.numbers = [2,3,4,5,6]
        
        # Create tickets
        self.ticket = models.Ticket.objects.create (
            lottery = self.lottery_a,
            number = 1,
            buyer_name = self.user_name,
            buyer_email = self.user_phone,
            buy_at = self.date,
            is_paid = False,
            active = True,            
        )
        
    def test_get_lotteries (self):
        """ Test endpoint who return all lotteries data """
        
        response = self.client.get (self.endpoint_get_lotteries)
        
        # Validate response status
        self.assertEqual (response.status_code, 200)
        
        # Validate response lotteries
        self.assertEqual (len(response.json()), 2)
        
        # Validate lottery a
        self.assertEqual (response.json()[0]["title"], self.lottery_name_a)
        self.assertEqual (response.json()[0]["description"], self.lottery_details)
        self.assertEqual (response.json()[0]["date"], self.date.strftime ("%d/%m/%Y"))
        self.assertEqual (response.json()[0]["image"], f'{settings.MEDIA_URL}{self.lottery_image}')
        self.assertEqual (len(response.json()[0]["numbers"]), self.lottery_numbers - 1)
        self.assertEqual (float(response.json()[0]["price"]), int(self.lottery_total_price / self.lottery_numbers))
        
        # Validate lottery b
        self.assertEqual (response.json()[1]["title"], self.lottery_name_b)
        self.assertEqual (response.json()[1]["description"], self.lottery_details)
        self.assertEqual (response.json()[1]["date"], self.date.strftime ("%d/%m/%Y"))
        self.assertEqual (response.json()[1]["image"], f'{settings.MEDIA_URL}{self.lottery_image}')
        self.assertEqual (len(response.json()[1]["numbers"]), self.lottery_numbers)
        self.assertEqual (float(response.json()[1]["price"]), int(self.lottery_total_price / self.lottery_numbers))
    
    def test_save_tickets (self):
        """ Test endpoint who save tickets """
        
        # Regular request
        response = self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
                "tickets": self.numbers,
                "lottery": self.lottery_a.name,
            }, 
            content_type='application/json',
        )
        
        # Validate response
        self.assertEqual (response.status_code, 200)
        self.assertEqual (response.json()["status"], "success")
        self.assertEqual (response.json()["data"], {})
        self.assertEqual (response.json()["message"], "saved")

    
    def test_save_tickets_missing_data (self):
        """ Test endpoint who save tickets, with missing data """
        
        # Request with missing data
        response = self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
            }, 
            content_type='application/json',
        )
        
        # Validate response
        self.assertEqual (response.status_code, 200)
        self.assertEqual (response.json()["status"], "error")
        self.assertEqual (response.json()["data"], {})
        self.assertEqual (response.json()["message"], "missing data")
        
    def test_save_tickets_lottery_not_found (self):
        """ Test endpoint who save tickets, with invalid lottery name """
        
        # Request with invalid lotery name
        response = self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
                "tickets": self.numbers,
                "lottery": "this lottery not exist",
            }, 
            content_type='application/json',
        )
        
        # Validate response
        self.assertEqual (response.status_code, 200)
        self.assertEqual (response.json()["status"], "error")
        self.assertEqual (response.json()["data"], {})
        self.assertEqual (response.json()["message"], "lottery not found")
        
    def test_save_tickets_lottery_not_open (self):
        """ Test endpoint who save tickets, with no open lottery """
        
        # Update lottery a to not open
        self.lottery_b.is_open = False
        self.lottery_b.save()
        
        # Regular request
        response = self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
                "tickets": self.numbers,
                "lottery": self.lottery_b.name,
            }, 
            content_type='application/json',
        )
        
        # Validate response
        self.assertEqual (response.status_code, 200)
        self.assertEqual (response.json()["status"], "error")
        self.assertEqual (response.json()["data"], {})
        self.assertEqual (response.json()["message"], "lottery is closed")
        
    
    def test_save_tickets_not_available (self):
        """ Test endpoint who save tickets, with no available tickets """
        
        # Initial request
        self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
                "tickets": self.numbers,
                "lottery": self.lottery_a.name,
            }, 
            content_type='application/json',
        )
        
        # Request with same tickets (and some new tickets)
        response = self.client.post (
            self.endpoint_save_ticket, 
            {
                "user_name": self.user_name,
                "user_phone": self.user_phone, 
                "tickets": self.numbers,
                "lottery": self.lottery_a.name,
            }, 
            content_type='application/json',
        )
        
        # Validate response
        self.assertEqual (response.status_code, 200)
        self.assertEqual (response.json()["status"], "error")
        self.assertEqual (response.json()["data"], {"numbers": self.numbers})
        self.assertEqual (response.json()["message"], "numbers not available")
        
class TestCrons (TestCase):
    
    def setUp (self):
        """ Setup test """
        
        self.date = timezone.now()
        self.limit_date = self.date-timezone.timedelta(hours=DELETE_HOURS)
        
        # Create lotteries
        
        lottery = models.Lottery.objects.create (
            name = "sample lottery",
            details = "sample details",
            total_price = 1000,
            image = "sample.jpg",
            end_date = "2023-01-01",
            numbers = 100,
            is_open = True,
        )
        
        # Create tickets
        models.Ticket.objects.create (
            lottery = lottery,
            number = 1,
            buyer_name = "sample user",
            buyer_email = "sample@gmail.com",
            buy_at = self.limit_date, # ticket buyed hours ago
            is_paid = False,
            active = True,            
        )
        
        models.Ticket.objects.create (
            lottery = lottery,
            number = 2,
            buyer_name = "sample user",
            buyer_email = "sample@gmail.com",
            buy_at = self.date, # ticket buyed now 
            is_paid = False,
            active = True,            
        )
        
    def test_delete_tickets (self):
        """ Test delete tickets cron """
        
        # Validate tickets before run cron
        self.assertEqual (models.Ticket.objects.filter (active=True).count(), 2)
        
        # Run cron
        disable_tickets.disable ()
        
        # Validate tickets before run cron
        self.assertEqual (models.Ticket.objects.filter (active=True).count(), 1)
        
        