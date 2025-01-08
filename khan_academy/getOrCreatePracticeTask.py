#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/7 上午10:27
# @Author  : 苏玉恒
# @File    : getOrCreatePracticeTask.py
# @Software: PyCharm
import json

import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "OptanonAlertBoxClosed=2024-12-05T07:47:54.318Z; _gcl_au=1.1.710789402.1733384916; _ga=GA1.1.823046458.1733384917; gae_b_id=!$PTC8bocdhhOLAAzHfh_4xGaPgnRCFbuVcvA7rXjNL3E.~sp2vf0~1$a2FpZF81NzUwMDE1MDk4NTA3MTI5NTEyOTI4OTM; LIS=zh; KAAS=qyZE8z0recwoSJO-FvKTLw; browsing_session_id=_zh-hans_bsid_a725cb19-d390-4ee0-a006-90b938910002; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+07+2025+09%3A50%3A38+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=06e9c03a-dec5-4951-b4f8-caeeae239f6c&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=HK%3B&AwaitingReconsent=false; _ga_19G17DJYEE=GS1.1.1736212914.20.1.1736215904.0.0.0; KAAL=$xkUbNZG9zANV1CtysEKAW9jnIjb2sLB6Tlp3innlGn4.~spp54c$a2FpZF81NzUwMDE1MDk4NTA3MTI5NTEyOTI4OTM*; KAAC=$ysArwRCclt44jZsSd6iuBoxpcIrGnZUi5-lX1liOnAs.~spp54c$a2FpZF81NzUwMDE1MDk4NTA3MTI5NTEyOTI4OTM*$a2FpZF81NzUwMDE1MDk4NTA3MTI5NTEyOTI4OTM!0!1~3; browsing_session_expiry=\\Tue,",
    "origin": "https://zh.khanacademy.org",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://zh.khanacademy.org/math/algebra2/manipulating-functions/function-composition/e/evaluate-composite-functions-from-formulas",
    "sec-ch-ua": "\\Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "x-ka-fkey": "1"
}
url = "https://zh.khanacademy.org/api/internal/graphql/getOrCreatePracticeTask"
params = {
    "lang": "zh-hans",
    "_": "250106-1553-ad047669a61b_1736216444796"
}
exerciseId = "x9dd681f5"
query = "mutation getOrCreatePracticeTask($input: GetOrCreatePracticeTaskInput!) {\n  getOrCreatePracticeTask(input: $input) {\n    result {\n      error {\n        code\n        debugMessage\n        __typename\n      }\n      userTask {\n        ...userTaskFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment userExerciseFields on UserExercise {\n  exerciseModel: exercise {\n    id\n    assessmentItemCount: numAssessmentItems\n    displayName\n    isQuiz\n    isSkillCheck\n    name\n    nodeSlug\n    progressKey\n    translatedDisplayName\n    relatedContent {\n      id\n      contentKind\n      kind\n      thumbnailUrl\n      translatedTitle\n      topicPaths {\n        path {\n          id\n          kind\n          slug\n          __typename\n        }\n        __typename\n      }\n      ... on Article {\n        kaUrl\n        nodeSlug\n        relativeUrl\n        slug\n        __typename\n      }\n      ... on Video {\n        duration\n        imageUrl\n        kaUrl\n        nodeSlug\n        relativeUrl\n        slug\n        translatedYoutubeId\n        __typename\n      }\n      __typename\n    }\n    relatedVideos {\n      contentKind\n      duration\n      id\n      imageUrl\n      kaUrl\n      kind\n      nodeSlug\n      progressKey\n      relativeUrl\n      slug\n      thumbnailUrl\n      translatedDescription\n      translatedTitle\n      translatedYoutubeId\n      __typename\n    }\n    problemTypes {\n      items {\n        id\n        live\n        sha\n        __typename\n      }\n      name\n      relatedVideos\n      __typename\n    }\n    translatedProblemTypes {\n      items {\n        id\n        live\n        sha\n        __typename\n      }\n      name\n      relatedVideos\n      __typename\n    }\n    __typename\n  }\n  exercise: exerciseName\n  fpmMasteryLevel\n  lastAttemptNumber\n  lastCountHints\n  lastDone\n  lastMasteryUpdate\n  longestStreak\n  maximumExerciseProgressDt: maximumExerciseProgressDate\n  streak\n  totalCorrect\n  totalDone\n  __typename\n}\n\nfragment userTaskFields on PracticeUserTask {\n  cards {\n    done\n    cardType\n    ... on ProblemCard {\n      exerciseName\n      problemType\n      __typename\n    }\n    __typename\n  }\n  includeSkipButton\n  task {\n    contentKey\n    exerciseLength\n    id\n    key\n    pointBounty\n    pointsEarned\n    slug\n    taskType\n    timeEstimate {\n      lowerBound\n      upperBound\n      __typename\n    }\n    completionCriteria {\n      name\n      __typename\n    }\n    promotionCriteria {\n      name\n      value\n      __typename\n    }\n    reservedItems\n    reservedItemsCompleted\n    taskAttemptHistory {\n      correct\n      timeDone\n      seenHint\n      itemId\n      __typename\n    }\n    __typename\n  }\n  userExercises {\n    ...userExerciseFields\n    __typename\n  }\n  __typename\n}"
data_dict = {
    "operationName": "getOrCreatePracticeTask",
    "variables": {
        "input": {
            "exerciseId": exerciseId,
            "stopCardPersist": False,  # 不能是字符串
            "canReserveItems": True
        }
    },
    "query": query
}

data = json.dumps(data_dict)

response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)
