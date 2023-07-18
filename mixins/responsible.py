class HasResponsible:
    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    @property
    def email(self):
        return self.user.email