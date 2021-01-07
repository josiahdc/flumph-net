class Info:
    @staticmethod
    def save(db_session, target):
        info = target.generate_info(db_session)
        db_session.add(info)
        return info
