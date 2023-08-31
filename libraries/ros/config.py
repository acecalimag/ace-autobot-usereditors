from datetime import timedelta
from autocore import envlabels


ROS_LOGIN_PAGE_URL: dict = {
    envlabels.QA_ENV: "https://qa.letsdochinese.com/webclient/ros/login"
}

ROS_GLOBAL_TIMEOUT = timedelta(seconds=30)