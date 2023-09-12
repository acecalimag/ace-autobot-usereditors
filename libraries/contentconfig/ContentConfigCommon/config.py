from datetime import timedelta
import autocore.envlabels as envlabels

CONTENT_CONFIG_LOGIN_PAGE_URL: dict = {
    envlabels.QA_ENV: 'https://qa.letsdochinese.com/KJTCore/resources/contentconfigclient/index.html?agent=undefined'
}

CONTENT_CONFIG_GLOBAL_TIMEOUT = timedelta(seconds=30)
CONTENT_CONFIG_LANDING_TIMEOUT = timedelta(seconds=360)
PRINTER_EDITOR_LANDING_TIMEOUT = timedelta(seconds=360)
