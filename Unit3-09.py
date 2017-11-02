# Created by: Peter Zhu
# Created on: Oct 24th
# Created for: ICS3U

for outerCounter in range(65,91):
    for interCounter in range(97, 123):
        unicode = unichr(interCounter)
        upper_unicode = unichr(outerCounter)
        print (str(upper_unicode) + '->' + str(unicode)) 
