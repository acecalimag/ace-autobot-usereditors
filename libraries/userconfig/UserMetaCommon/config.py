from datetime import timedelta

from autocore import envlabels


USER_CONFIG_LOGIN_PAGE_URL: dict = {
    envlabels.QA_ENV: 'https://qa.letsdochinese.com/KJTCore/resources/userconfigclient/index.html?agent=undefined'
}

USER_CONFIG_GLOBAL_TIMEOUT = timedelta(seconds=30)
USER_CONFIG_LANDING_TIMEOUT = timedelta(seconds=360)
