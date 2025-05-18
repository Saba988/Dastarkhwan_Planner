class FoodDonation:
    def __init__(self, donor, food_items, quantity, expiry_time, location):
        self.donor = donor
        self.food_items = food_items
        self.quantity = quantity
        self.expiry_time = expiry_time
        self.location = location
        self.status = "Pending"

    def to_dict(self):
        return {
            "donor": self.donor,
            "food_items": self.food_items,
            "quantity": self.quantity,
            "expiry_time": self.expiry_time,
            "location": self.location,
            "status": self.status
        }
