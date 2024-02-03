class C3PO:
    def __init__(self, millennium_falcon_data):
        self.autonomy = millennium_falcon_data["autonomy"]
        self.routes = self._preprocess_routes(millennium_falcon_data["routes"])
        self.memo = {}

    def _preprocess_routes(self, routes):
        processed_routes = {}
        for route in routes:
            src, dest, time = route["origin"], route["destination"], route["travelTime"]
            processed_routes.setdefault(src, []).append((dest, time))
            processed_routes.setdefault(dest, []).append((src, time))
        return processed_routes

    def give_me_the_odds(self, empire_data):
        countdown = empire_data["countdown"]
        bounty_hunters = {
            (hunter["planet"], hunter["day"]) for hunter in empire_data["bounty_hunters"]
        }
        return self._calculate_odds(
            "Tatooine", "Endor", countdown, bounty_hunters, self.autonomy
        )

    def _calculate_odds(
        self, start, end, countdown, bounty_hunters, autonomy_left, day=0, probability=1.0
    ):
        if (start, day, autonomy_left) in self.memo:
            return self.memo[(start, day, autonomy_left)]

        if start == end:
            return probability if day <= countdown else 0

        if day > countdown:
            return 0

        odds = 0
        for planet, travel_time in self.routes.get(start, []):
            new_day = day + travel_time
            if new_day > countdown:
                continue

            capture_chance = 0.1 if (planet, new_day) in bounty_hunters else 0
            new_probability = probability * (1 - capture_chance)

            new_autonomy_left = autonomy_left - travel_time
            if new_autonomy_left < 0:
                # Need to refuel
                new_day += 1
                new_autonomy_left = self.autonomy - travel_time

            if new_day <= countdown:
                odds = max(
                    odds,
                    self._calculate_odds(
                        planet,
                        end,
                        countdown,
                        bounty_hunters,
                        new_autonomy_left,
                        new_day,
                        new_probability,
                    ),
                )

        self.memo[(start, day, autonomy_left)] = odds
        return odds
