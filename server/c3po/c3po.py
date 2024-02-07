class C3PO:
    def __init__(self, millennium_falcon_data):
        self.autonomy = millennium_falcon_data["autonomy"]
        self.routes = millennium_falcon_data["routes"]
        self.route_dict = {
            (route["origin"], route["destination"]): route["travelTime"]
            for route in self.routes
        }
        self.route_dict.update(
            {
                (route["destination"], route["origin"]): route["travelTime"]
                for route in self.routes
            }
        )

    def calculateOdds(self, empire_data):
        countdown = empire_data["countdown"]
        bounty_hunters = {
            (hunters["planet"], hunters["day"]): True
            for hunters in empire_data["bounty_hunters"]
        }
        
        # Begin with initial conditions
        return self.planRoute(
            "Tatooine",
            "Endor",
            countdown,
            self.autonomy,
            0,
            1,
            bounty_hunters,
            False,
        )

    def planRoute(
        self,
        current,
        destination,
        time_left,
        fuel_left,
        days_spent,
        odds,
        bounty_hunters,
        refueled,
    ):
        # Destination reached
        if current == destination and time_left >= 0:
            return odds

        # No remaining time left or already impossible to reach destination
        if time_left < 0 or odds == 0:
            return 0

        optimal_odds = 0

        # Waiting on current planet to avoid bounty hunters
        if not refueled and (current, days_spent) not in bounty_hunters:
            optimal_odds = self.planRoute(
                current = current,
                destination = destination,
                time_left = time_left - 1,
                fuel_left = self.autonomy,
                days_spent = days_spent + 1,
                odds = odds,
                bounty_hunters = bounty_hunters,
                refueled = True,
            )

        # Check each route of current planet
        for (origin, dest), travel_time in self.route_dict.items():
            if origin == current:
                next_fuel_left = fuel_left - travel_time
                if next_fuel_left < 0:
                    if (current, days_spent) in bounty_hunters:
                        odds *= 0.9
                    next_fuel_left = self.autonomy - travel_time
                    days_spent += 1
                    time_left -= 1

                if time_left - travel_time >= 0:
                    if (dest, days_spent + travel_time) in bounty_hunters:
                        path_odds = odds * 0.9
                    else:
                        path_odds = odds

                    next_odds = self.planRoute(
                        current = dest,
                        destination = destination,
                        time_left = time_left - travel_time,
                        fuel_left = next_fuel_left,
                        days_spent = days_spent + travel_time,
                        odds = path_odds,
                        bounty_hunters = bounty_hunters,
                        refueled = False,
                    )
                    optimal_odds = max(optimal_odds, next_odds)

        return optimal_odds
