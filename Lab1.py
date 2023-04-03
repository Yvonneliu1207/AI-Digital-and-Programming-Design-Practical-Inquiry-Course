Web VPython 3.2
g=9.8
tmin=0.0
tmax=200.
itstep=80000 
dt=(tmax-tmin)/float(itstep+1)
v=[]
y=[]
t=[]
x=[]
v[0]=0.
y[0]=30.
x[0]=0.
floy=-20
##場景設置
scene=canvas(title=' demonstration ',align='center',width=800,height=600,autoscale
=True,center=vec(0,10,0), background=color.black)
##拼設置一個球體，並指定為 ball
ball=sphere(pos=vec(0,y[0],0),radius=1.)
##設置一個方塊，並指定為 foor
floor=box(pos=vec(0,-20,0),axis=vec(1,0,0),length=40,width=10,height=0.2
,color=color.green)

g1=graph(width=1000,height=400,fast=True,align='right',
    ytitle='<i>y (m)<i>', foreground=color.black, background=color.white, 
    xmin=0., xmax=60,ymin=floy, ymax=(y[0]+(v[0]**2/(2*g)))*1.05) 

g2=graph(width=1000,height=400, fast=True,align='right',xtitle='<i>t (s) <i>', 
    ytitle='<i>vy (m/s)<i>', foreground=color.black, background=color.white, 
	xmin=0., xmax=60, ymin=-30, ymax=5)


f2=gcurve(graph=g2,data=[[0,v[0]]],color=color.blue,width=1,
    markers=False, radius=0.4, marker_color=color.blue, dot=True, fast=False)

f3=gcurve(graph=g1,data=[[0,y[0]]],color=color.red,width=1,
	markers=False, radius=0.4, marker_color=color.blue, dot=True, fast=False)

    
for i in range(0,itstep+1,1):
        rate(1./dt) 
        t[i+1]=tmin+float(i)*dt
      
        v[i+1]=v[i]-g*dt
        y[i+1]=y[i]+v[i]*dt
        x[i+1]=0.
      
        if(y[i+1]<=-(19.9-ball.radius)):
            y[i+1]=-(19.9-ball.radius)
            v[i+1]=-0.9*v[i+1]
        ball.pos=vec(x[i+1],y[i+1],0)
        
        f2.plot(t[i+1],v[i+1])
        
        f3.plot(t[i+1],y[i+1] -ball.radius)
