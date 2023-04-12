def loader(app):
    @app.template_filter('num_to_month')
    def num_to_month(num) -> str:
        """
        {{ 1 | num_to_month }} -> January
        """
        months = {0: "-", 1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                  7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        if isinstance(num, int):
            if num in months:
                return months[num]
        return num
