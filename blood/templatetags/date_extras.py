# your_app/templatetags/date_extras.py

from django import template
from datetime import date

register = template.Library()

@register.filter
def days_since(value):
    if not value:
        return "N/A", False
    
    today = date.today()
    difference = today - value
    days = abs(difference.days)  # Ensure no negative values
    
    # Check if it's more than or equal to 120 days (approx 4 months)
    more_than_4_months = days >= 120
    
    if days < 30:
        time_since = f"{days} days ago"
    else:
        months = days // 30
        time_since = f"{months} months ago" if months > 1 else "1 month ago"
    
    return time_since, more_than_4_months
