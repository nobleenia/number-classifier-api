from django.shortcuts import render

# Create your views here.

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    """Home endpoint showing a welcome message."""
    return JsonResponse({"message": "Welcome to the Number Classification API!"})

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def classify_number(request):
    """API to classify a number and return its properties."""
    number_param = request.GET.get('number')

    # Validate input
    try:
        number = int(number_param)
    except (TypeError, ValueError):
        return JsonResponse({"number": number_param, "error": True}, status=400)

    # Determine properties
    digit_sum = sum(int(digit) for digit in str(number))
    prime_status = is_prime(number)
    perfect_status = is_perfect(number)
    armstrong_status = is_armstrong(number)
    parity = "odd" if number % 2 != 0 else "even"

    # Define properties array
    properties = [parity]
    if armstrong_status:
        properties.insert(0, "armstrong")

    # Fetch fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json")
        fun_fact = response.json().get("text", "No fact available.")
    except requests.RequestException:
        fun_fact = "Could not fetch a fun fact."

    # Build response
    data = {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return JsonResponse(data, json_dumps_params={'indent': 2})
