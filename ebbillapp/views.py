from django.shortcuts import render,redirect
from ebbillapp.models import CustomerCarRequest as cus


# Create your views here.
def ebCalculation(request):
    if request.method == 'POST':
        districts=request.POST.get('districts')
        pre_reading=int(request.POST.get('pre_reading'))
        cur_reading=int(request.POST.get('cur_reading'))
        y=cur_reading - pre_reading
        
        x=0
        if y <= 100:
            x*=0
        elif y>100 and y<=200:
            x=(y-100)*2.25
        elif y>200 and y<=400:
            x=225+(y-200)*4.50
        elif y>400 and y<=500:
            x=225+900+(y-400)*6
        elif y>500 and y<=600:
            x=225+900+600+(y-500)*8
        elif y>600 and y<=800:
            x=225+900+600+800+(y-600)*9
        elif y>800 and y<=1000:
            x=225+900+600+800+900+(y-800)*10
        else:
            x=225+900+600+800+900+2000+(y-1000)*11
        content={'units':y,'cost':x}
        
        cus.objects.create(name=pre_reading,mobile=cur_reading,email=x,profession=y)
        return render(request,'dashboard.html',content)
    return render(request,'dashboard.html')


