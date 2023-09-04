from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')


def signup_page(request):
    if request.method == 'POST':
        # Process the form data (signin logic)
        # For example, you can access the form fields like this:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')

        # Your signin logic here...

        # Redirect to the login page after signin
        return redirect('login')
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        # Process the form data (login logic)
        # For example, you can access the form fields like this:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your login logic here...

        # Redirect to the booking page after login
        return redirect('booking')
    return render(request, 'login.html')

from django.shortcuts import render, redirect

def booking_page(request):
    if request.method == 'POST':
        # Process the form data (booking logic)
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        seats = request.POST.get('seats')
        
        # Your booking logic here...
        # For example, you might save the booking details to a database.
        # Replace the following line with your actual booking logic.
        # booking = Booking.objects.create(source=source, destination=destination, date=date, seats=seats)

        # Get the selected seats from the hidden field
        selected_seats = request.POST.get('selected_seats')

        # Pass the selected seats to the booking success template
        return render(request, 'booking_success.html', {
            'selected_seats': selected_seats,
            'source': source,
            'destination': destination,
            'date': date,
            'seats': seats
        })

    return render(request, 'booking.html')

    return render(request, 'booking.html')
def booking_success(request):
    if request.method == 'POST':
        selected_seats = request.POST.get('selected_seats', '')
        source = request.POST.get('hidden_source', '')  # Retrieve source from hidden field
        destination = request.POST.get('hidden_destination', '')  # Retrieve destination from hidden field
        # ... Handle any other data you need

        return render(request, 'booking_success.html', {
            'selected_seats': selected_seats,
            'source': source,
            'destination': destination,
            # ... Pass other data you want to display
        })
    else:
        return redirect('home')
def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')
def offer_page(request):
    
    return render(request, 'offer.html')
def ticket_cancel(request):
    return render(request, 'ticket_cancel.html')
def bus_seat(request):
    # Your logic for bus seat selection here
    # ...
    return render(request, 'bus_seat.html')


def payment_page(request):
    if request.method == 'POST':
        selected_seats = request.POST.get('selected_seats', '')
        # ... any other data you want to pass to the payment page ...

        return render(request, 'payment.html', {
            'selected_seats': selected_seats,
            # ... any other data you want to pass to the payment page ...
        })
    else:
        return redirect('home')



def payment_confirmation(request):
    
    selected_seats = request.POST.get('selected_seats', '').split(',')
    seat_count = len(selected_seats)
    total_amount = seat_count * 1000  # Assuming each seat costs 1000 rupees
    
    return render(request, 'payment_confirmation.html', {
        'seat_count': seat_count,
        'total_amount': total_amount
    })
    

def user_list(request):
    users = User.objects.all()  # Query all users
    return render(request, 'user_list.html', {'users': users})