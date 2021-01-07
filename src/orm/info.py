class Info:
    @staticmethod
    def save(db_session, target):
        info = target.retrieve_self_info(db_session)
        if info is None:
            info = target.generate_info(db_session)
        db_session.add(info)
