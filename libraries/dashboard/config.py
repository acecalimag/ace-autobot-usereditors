from datetime import timedelta
import autocore.envlabels as envlabels

DASHBOARD_LOGIN_PAGE_URL: dict = {
    envlabels.QA_ENV: 'https://qa.letsdochinese.com/KJTCore/resources/index.html?agent=dashboard'
}

DASHBOARD_GLOBAL_TIMEOUT = timedelta(seconds=30)
