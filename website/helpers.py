def get_activity(team_name, class_name):
        activity = class_name.query.filter_by(team_name = team_name).all()
        return activity