from dbus.exceptions import DBusException
import notify2


class Notifier(object):

    """Sends notifications via the user's notification daemon.

    If the user does not have a notification daemon, it will print a notice and
    silently cancel any passed notifications..
    """

    def __init__(self, app_name, icon):
        """Initializes a new Notifier.

        Arguments:
        app_name --- The app name used to identify the dbus channel.
        icon     --- The default icon to use for notifications.
        """

        self.icon = icon

        try:
            notify2.init(app_name)
            self.enabled = True
        except DBusException:
            print("WARNING: No notification daemon found! "
                  "Notifications will be ignored.")
            self.enabled = False

    def notify(self, title, message, icon=None):
        """Sends a new notification.

        Arguments:
        title   --- The title of the notification.
        message --- The body of the notification.
        icon    --- The icon for the notification (defaults to self.icon).
        """

        if not self.enabled:
            return

        if icon is None:
            icon = self.icon

        notice = notify2.Notification(title, message, icon)
        notice.set_hint_string('x-canonical-append', '')
        notice.show()
