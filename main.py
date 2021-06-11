from datetime import datetime, timedelta

if __name__ == '__main__':

    while True:
        try:
            birthday = datetime.strptime(input("Enter your birthday (m/d/yyyy format):"),"%m/%d/%Y")
            break
        except ValueError:
            print("Invalid format, please try again")
            pass

    age = datetime.now() - birthday
    print(f"You are {age.days} days old.")

    # Orbital periods in earth days
    planet_orbital_periods = {
        'Mercury'   : 88,
        'Venus'     : 226.3,
        'Earth'     : 365.25,
        'Mars'      : 686.2,
        'Jupiter'   : 4380,
        'Saturn'    : 10767.5,
        'Uranus'    : 30660,
        'Neptune'   : 60225,
        'Pluto'     : 90520
    }
    for k, v in planet_orbital_periods.items():
        print(f"That's {age.days / v:.2f} times around the sun on {k}")
