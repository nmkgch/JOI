NABCD=list(map(int, input().split()))
want=NABCD[0]
xkazu=NABCD[1]
xyen=NABCD[2]
ykazu=NABCD[3]
yyen=NABCD[4]

# want=10
# xkazu=3
# xyen=100
# ykazu=5
# yyen=180

if want%xkazu!=0:
    xbuy=want//xkazu+1
else:
    xbuy=want//xkazu
if want%ykazu!=0:
    ybuy=want//ykazu+1
else:
    ybuy=want//ykazu
xnedan=xyen*xbuy
ynedan=yyen*ybuy
if xnedan>=ynedan:
    print(ynedan)
else:
    print(xnedan)