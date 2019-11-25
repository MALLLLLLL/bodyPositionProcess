import test
import analysis
import pullUp

PULL_UP_FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\pull-up'
PUSH_UP_FILEPATH = r'E:\Programming\Openpose\openpose\openpose\output\push-up'

times = pullUp.pullUpAnalysis(PULL_UP_FILEPATH)
region = []
for time in times:
    print(time)
    region.append(time['Flag'])
test.getPullUpInfos(PULL_UP_FILEPATH, True, region)
test.getPushUpInfos(PUSH_UP_FILEPATH, True)
