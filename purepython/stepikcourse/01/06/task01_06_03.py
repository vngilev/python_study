class  LoggableList(list, Loggable):
    def append(self, p_object):
        super().append(p_object)
        super().log(p_object)

