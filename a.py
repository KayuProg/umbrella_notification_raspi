if key=="ko":
    if  result["ko"]>=now_hour:
        time=str(result["ko"])+"時から小雨．"
elif key=="yowa":
    if  result["yowa"]>=now_hour:                
        time=str(result["yowa"])+"時から弱雨．"
elif key=="ame":
    if  result["ame"]>=now_hour:
        time=str(result["ame"])+"時から雨．"
elif key=="tuyo":
    if  result["tuyo"]>=now_hour:
        time=str(result["tuyo"])+"時から強い雨．"
elif key=="gou":
    if  result["gou"]>=now_hour:
        time=str(result["gou"])+"時から豪雨．"