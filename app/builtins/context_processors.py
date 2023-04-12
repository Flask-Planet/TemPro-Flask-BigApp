def loader(app):
    @app.context_processor
    def add_numbers_func():
        def add_numbers(num1: int, num2: int):
            """
            Add numbers function for use in templates.
            {{ add_numbers(1, 2) }} -> 3
            """
            return num1 + num2

        return dict(add_numbers=add_numbers)

    @app.context_processor
    def add_strings_func():
        def add_strings(str1: str, str2: str):
            """
            Add strings function for use in templates.
            {{ add_strings("Hello, ", "World!") }} -> Hello, World!
            """
            return str1 + str2

        return dict(add_strings=add_strings)
