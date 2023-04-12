def loader(app):
    from app.extensions import bigapp

    @app.before_request
    def before_request():
        bigapp.init_session()
