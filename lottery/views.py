from . import models
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse

def index (request):
    # Redirect to admin
    return redirect (reverse ('admin:index'))

def get_lotteries (request):
    
    # Get lotteries
    lotteries = models.Lottery.objects.filter (is_open=True)
    
    # Format data
    data = []
    for lottery in lotteries:
    
        # Get buyed tickets
        buyed_nums = models.Ticket.objects.filter (active=True, lottery=lottery)
        
        # Calculate free tickets
        buyed_nums = list(map(lambda ticket: ticket.number, buyed_nums))
        total_nums = list(range(1, lottery.numbers + 1))
        free_nums = list(filter(lambda ticket: ticket not in buyed_nums, total_nums))
        
        # Format date
        end_date = lottery.end_date.strftime ("%d/%m/%Y")
        
        # Save as dictionary
        lottery_data = {
            "title": lottery.name,
            "description": lottery.details,
            "date": end_date,
            "image": lottery.image,
            "numbers": free_nums,
            "price": round(lottery.total_price / lottery.numbers, 2),
        }
        
        data.append (lottery_data)
    
    # Return data as json
    return JsonResponse (data, safe=False)

