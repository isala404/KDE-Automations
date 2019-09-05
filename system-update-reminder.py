import notify2

notify2.init("Reminder")

n = notify2.Notification(
    "Update the Packages",
    "It's Midnight don't forget to run \n sudo pacman -Syyu and\n yay -Syyu",
    "notification-message-im"
)
n.set_timeout(notify2.EXPIRES_NEVER)

n.show()
