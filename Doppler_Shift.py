Web VPython 3.2

running = False
def Run(b):
    global running
    running = not running
    
    if running: b.text = "Pause"
    else: b.text = "Run"
    
bbutton=button (text="Run", pos=scene.title_anchor, bind=Run)

def Reset(c):
    
    global t, ball
    t=0
    ball.pos=vector(0,2,0) 
    ball.p=vector(0,0,0)
    
    
    Te=text(pos=vec(0,-3.5,0.),height=0.4,text='yvonne', 
    align='center',emissive=False,shininess=1,depth=0.05,color=color.cyan)
    #lamp=local light(pos=vec(-4.4,-3.5,3.),color=vec(255/255,255/255,100/255))
    circular=[]
    circular[0]=ring(pos=center,axis=vec(0,0,1),radius=0.0005,thickness=thick,color=color.white,shininess=1,opacity=1)
    source=sphere(pos=vec(xi,0,0),v=vec(vs,0,0),radius=0.18,color=color.red,shininess=0)
    pointer1=attach_arrow(source, 'v',scale=2.*v,shaftwidth=source.radius*0.8,color=color.yellow)
    if(vs<=v):scene.autoscale=False    
        
    t=0.
    x=xi
    
    icount=0
    #while 迥圈己經執行的次數=目前己經穳分幾個 dt
    icount2=0 # 已經創建的圓形數目 （不包含一開始創建的第一個）
        
        
cbutton = button (text="Reset", pos=scene.title_anchor, bind=Reset)


def S(s):
    print(s.value)
    vs=s.value
slider( bind=S )
scene.append_to_caption('\n\n')


v=1.
t=0.
xi=2.
dt=0.0006
T=1.
period=int(T/dt)
center=vec(xi,0,0)
thick=0.03
lambda=v*T

tmax=2000.
vs=1.2*v


scene = canvas(title=' <b> Doppler shift <b> \n\n',align='left',width=1000,height=800,
autoscale=True,center=vec(5,0,0))
Te=text(pos=vec(0,-3.5,0.),height=0.4,text='yvonne', 
align='center',emissive=False,shininess=1,depth=0.05,color=color.cyan)
#lamp=local light(pos=vec(-4.4,-3.5,3.),color=vec(255/255,255/255,100/255))
circular=[]
circular[0]=ring(pos=center,axis=vec(0,0,1),radius=0.0005,thickness=thick,color=color.white,shininess=1,opacity=1)
source=sphere(pos=vec(xi,0,0),v=vec(vs,0,0),radius=0.18,color=color.red,shininess=0)
pointer1=attach_arrow(source, 'v',scale=2.*v,shaftwidth=source.radius*0.8,color=color.yellow)
if(vs<=v):scene.autoscale=False
t=0.
x=xi

icount=0
#while 迥圈己經執行的次數=目前己經穳分幾個 dt
icount2=0 # 已經創建的圓形數目 （不包含一開始創建的第一個）





drag=False

scene.bind("mousedown", def():
    global drag 
    drag=True
    
    scene.bind("mouseup", def(): 
        global drag 
        drag=False
    )
)  

while True:
    rate (100)
#    if drag:

        
        

    if running:
        
        
        t=t+dt
        #x=x+vs*dt 
        source.pos=source.pos+source.v* dt
        #旋轉文字標題
        #Te.rotate(angl=-0.005,axis=vector(0,1,0))
    
        #控制聲源顋示的顏色
        if(icount%period==0):
            if(icount2%2==0):
                source.color=vec(1,0,0)
            else:
                source.color=vec(0,0,1)
            # 增加一個新的圓形
            circular.append(ring(pos=source.pos,axis=vector(0,0,1),radius=0.0005,thickness=thick,color=color.white,shininess=1,opacity=1))
            #計數器＋1 已經創建的圓形數目+1
            icount2=icount2+1
        #讓所有的圓形都變大 v*dt
        for i in range(0,icount2+1,1):
            circular[i].radius=circular[i].radius+v*dt
        rate(2./dt)
        icount=icount+1
