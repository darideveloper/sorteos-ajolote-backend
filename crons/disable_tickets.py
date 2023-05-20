import os
import sys
from django.utils import timezone
from dotenv import load_dotenv
import django

def disable ():
    """ Disable tickets that are not paid in specified time """
    
    from lottery import models 

    # Environtment variables
    DISABLE_HOURS = int(os.getenv ("DISABLE_HOURS"))
    
    # Get tickets buyed more than 8 hours ago
    limit_date = timezone.now().astimezone(timezone.utc) - timezone.timedelta(hours=DISABLE_HOURS - 0.1)
    print (f"Disabling tickets buyed before {limit_date}...")
    tickets = models.Ticket.objects.filter (is_paid=False, buy_at__lte=limit_date)

    if tickets:
        print (f"Disabling {len(tickets)} tickets")
        for ticket in tickets:
            ticket.active = False
            ticket.save ()
    else:
        print ("No tickets to disable")
        
if __name__ == "__main__":
    
    # Add parent folder to path
    parent_folder = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(parent_folder)

    # Setup django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sorteosajolote.settings')
    django.setup()
    
    load_dotenv ()   
    
    # Run cron
    disable ()