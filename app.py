from website import create_app


if __name__ == "__main__": #Make sure we run app.py and not importinhg it from somwhere else.
    app = create_app()
    app.run(debug=True) 
