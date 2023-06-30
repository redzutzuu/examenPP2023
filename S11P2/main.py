class AlertHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_alert(self, message, alert_level):
        if alert_level >= self.get_threshold():
            self.handle(message)
        if self.successor is not None:
            self.successor.handle_alert(message, alert_level)

    def get_threshold(self):
        raise NotImplementedError()

    def handle(self, message):
        raise NotImplementedError()


class NATOHandler(AlertHandler):
    def get_threshold(self):
        return 0

    def handle(self, message):
        print("NATO: {}".format(message))


class CSATHandler(AlertHandler):
    def get_threshold(self):
        return 1

    def handle(self, message):
        print("CSAT: {}".format(message))


class SIEHandler(AlertHandler):
    def get_threshold(self):
        return 2

    def handle(self, message):
        print("SIE: {}".format(message))


class SRIHandler(AlertHandler):
    def get_threshold(self):
        return 3

    def handle(self, message):
        print("SRI: {}".format(message))


class PoliceHandler(AlertHandler):
    def get_threshold(self):
        return 4

    def handle(self, message):
        print("Police: {}".format(message))


class MuseumGuardsHandler(AlertHandler):
    def get_threshold(self):
        return 5

    def handle(self, message):
        print("Museum Guards: {}".format(message))


def main():
    alert_handler = MuseumGuardsHandler(
        PoliceHandler(
            SRIHandler(
                SIEHandler(
                    CSATHandler(
                        NATOHandler()
                    )
                )
            )
        )
    )

    message = "Intrusion detected at the museum"
    alert_level = 5
    alert_handler.handle_alert(message, alert_level)


if __name__ == "__main__":
    main()
