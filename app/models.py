class Observation:
    def __init__(self, total, speeding, alcohol, not_distracted,no_previous,ins_premium, ins_losses, abbrev_id):
        self.total = total
        self.speeding = speeding
        self.alcohol = alcohol
        self.not_distracted = not_distracted
        self.no_previous = no_previous
        self.ins_premium = ins_premium
        self.ins_losses = ins_losses
        self.abbrev_id = abbrev_id

class Abbrev:
	def __init__(self, abbrev_id, abbrev):
	   self.abbrev_id = abbrev_id
	   self.abbrev = abbrev