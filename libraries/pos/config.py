from datetime import timedelta

import autocore.envlabels as envlabels

POS_LOGIN_PAGE_URL: dict = {
    envlabels.QA_ENV: 'https://qa.letsdochinese.com/KJTCore/resources/index.html?agent=metrics',
    envlabels.STG_ENV: 'https://staging.letsdochinese.com/KJTCore/resources/index.html?agent=metrics',
    envlabels.PROD_ENV: 'https://ph-api.letsdochinese.com/KJTCore/resources/index.html?agent=metrics'
}

POS_GLOBAL_TIMEOUT = timedelta(seconds=30)
POS_HOMEPAGE_TIMEOUT = timedelta(seconds=360)
POS_ORDERS_AREA_TIMEOUT = timedelta(seconds=60)
POS_RESTAURANT_TIMEOUT = timedelta(seconds=60)
POS_RESTAURANT_DISPLAY_AREA = timedelta(seconds=60)
