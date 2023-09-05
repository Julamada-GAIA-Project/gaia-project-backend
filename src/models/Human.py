class Human:
    def __init__(self, name, lastName, physical, studies):
        self.name = name
        self.lastName = lastName
        self.physical = physical
        self.studies = studies

    def __str__(self):
        return f"""
        Name: {self.name} {self.lastName}
        Physical: {self.physical}
        Studies: {self.studies}
        """
