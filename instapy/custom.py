from .time_util import sleep
from .util import web_address_navigator
from .util import update_activity

from selenium.common.exceptions import WebDriverException


class customMixin:
    def get_follower_num(self, username=None):
        """Prints and logs the current number of followers to
        a seperate file"""

        browser = self.browser
        username = username

        user_link = "https://www.instagram.com/{}".format(username)
        web_address_navigator(browser, user_link)

        try:
            followed_by = browser.execute_script(
                "return window.__additionalData[Object.keys(window.__additionalData)[0]].data."
                "graphql.user.edge_followed_by.count")

        except WebDriverException:  # handle the possible `entry_data` error
            try:
                browser.execute_script("location.reload()")
                update_activity(browser, state=None)

                sleep(1)
                followed_by = browser.execute_script(
                    "return window._sharedData."
                    "entry_data.ProfilePage[0]."
                    "graphql.user.edge_followed_by.count")

            except WebDriverException:
                followed_by = None

        # with open("{}followerNum.txt".format(logfolder), "a") as numFile:
        #     numFile.write(
        #         "{:%Y-%m-%d %H:%M} {}\n".format(datetime.now(), followed_by or 0))

        if followed_by is None:
            return 0
        return followed_by
