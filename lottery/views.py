import os
import json
from . import models
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

def index (request):
    """ Redirect to admin """
    
    # Redirect to admin
    return redirect (reverse ('admin:index'))

class Lotteries (View):
    
    def get (self, request):
        """ Get lotteries data as json """
        
        # Get lotteries
        lotteries = models.Lottery.objects.filter (is_open=True)
        
        # Format data
        data = []
        for lottery in lotteries:
        
            # Get buyed tickets
            buyed_tickets = models.Ticket.objects.filter (active=True, lottery=lottery)
            
            # Calculate free tickets
            buyed_tickets_nums = list(map(lambda ticket: ticket.number, buyed_tickets))
            total_tickets_nums = list(range(1, lottery.numbers + 1))
            free_tickets_nums = list(filter(lambda ticket: ticket not in buyed_tickets_nums, total_tickets_nums))
            
            # Format fields
            end_date = lottery.end_date.strftime ("%d/%m/%Y")
            
            # Save as dictionary
            lottery_data = {
                "title": lottery.name,
                "description": lottery.details,
                "date": end_date,
                "image": lottery.image.url,
                "numbers": free_tickets_nums,
                "price": int(lottery.total_price / lottery.numbers),
            }
            
            data.append (lottery_data)
        
        # Return data as json
        return JsonResponse (data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class SaveTickets (View):
    
    def post (self, request):
        
        """ Save tickets select by user """
        
        json_data = json.loads (request.body)
    
        # Get dta from json
        user_name = json_data.get ("user_name")
        user_phone = json_data.get ("user_phone")
        user_tickets = json_data.get ("tickets") # list of numbers
        user_lottery = json_data.get ("lottery") # name of lottery

        # Validate incoming data
        if not user_name or not user_phone or not user_tickets or not user_lottery:
            return JsonResponse ({
                "status": "error",
                "message": "missing data",
                "data": {}
            })        

        # Get lottery and catch errors
        lottery = models.Lottery.objects.filter (name=user_lottery)
        
        if not lottery:
            return JsonResponse ({
                "status": "error",
                "message": "lottery not found",
                "data": {}
            })
            
        lottery = lottery[0]
        
        if not lottery.is_open:
            return JsonResponse ({
                "status": "error",
                "message": "lottery is closed",
                "data": {}
            })
        
        # Validate if all numbers are free
        buyed_tickets = models.Ticket.objects.filter (active=True, lottery=lottery)
        buyed_tickets_nums = list(map(lambda ticket: ticket.number, buyed_tickets))
        not_abaible_tickets = list(filter(lambda ticket: ticket in buyed_tickets_nums, user_tickets))
        
        if not_abaible_tickets:
            return JsonResponse ({
                "status": "error",
                "message": "numbers not available",
                "data": {
                    "numbers": not_abaible_tickets,
                }
            })
            
        # Save tickets
        for ticket in user_tickets:
            models.Ticket.objects.create (
                lottery=lottery,
                number=ticket,
                buyer_name=user_name,
                buyer_phone=user_phone,
            )
            
        # Return success
        return JsonResponse ({
            "status": "success",
            "message": "saved",
            "data": {}
        })