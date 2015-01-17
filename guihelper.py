from panda3d.core import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *

def _pos2d(x,y):
    return Point3(x,0,-y)
    
def _rec2d(width, height):
    return (-width, 0, 0, height)
    
def _resetPivot(frame):
    size=frame['frameSize']    
    frame.setPos(-size[0], 0, -size[3])        
    frame.flattenLight()


class GuiHelper():
    def __init__(self, path=""):
        self.elements=[]
        self.path=path
        
        self.font = DGG.getDefaultFont()
        self.font.setPixelsPerUnit(16)
        self.fontBig=self.font.makeCopy()        
        self.fontBig.setPixelsPerUnit(32)
        
        self.TopLeft=pixel2d.attachNewNode('TopLeft')
        self.TopRight=pixel2d.attachNewNode('TopRight')
        self.BottomRight=pixel2d.attachNewNode('BottomRight')
        self.BottomLeft=pixel2d.attachNewNode('BottomLeft')
        self.Top=pixel2d.attachNewNode('Top')
        self.Bottom=pixel2d.attachNewNode('Bottom')
        self.Left=pixel2d.attachNewNode('Left')
        self.Right=pixel2d.attachNewNode('Right')
        self.Center=pixel2d.attachNewNode('Center')
        self.updateBaseNodes()
        
        self.dialog=DirectFrame(frameSize=_rec2d(512,192),
                                frameColor=(0,0,0, 0.8),
                                text='This is a dialog, no text was set! Alfa, beta, gamma, delta, tango, lambda, epsilon, omega, zeta.',
                                text_scale=32,
                                text_wordwrap=16,
                                text_font=self.fontBig,
                                text_pos=(-256,164),
                                text_fg=(1,1,1,1),
                                text_align=TextNode.ACenter,
                                parent=self.Center)
        _resetPivot(self.dialog)
        self.dialog.setPos(_pos2d(-256, -128))
        self.dialogYes=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="YES",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-70,7),
                                    text_fg=(0,1,0,1),
                                    state=DGG.NORMAL, 
                                    parent=self.dialog)
        _resetPivot(self.dialogYes)
        self.dialogYes.setPos(_pos2d(0,132))
        self.dialogNo=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="NO",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-70,7),
                                    text_fg=(1,0,0,1),
                                    state=DGG.NORMAL, 
                                    parent=self.dialog)
        _resetPivot(self.dialogNo)
        self.dialogNo.setPos(_pos2d(384,132))
        self.dialogOk=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="OK",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-70,7),
                                    text_fg=(0,0,1,1),
                                    state=DGG.NORMAL, 
                                    parent=self.dialog)
        _resetPivot(self.dialogOk)
        self.dialogOk.setPos(_pos2d(192,132))
        self.dialog.hide()
        
    def yesNoDialog(self, text, command, arg=[]):
        self.dialog.show()
        self.dialogYes.show()
        self.dialogNo.show()
        self.dialogOk.hide()   
        self.dialog['text']=text        
        yes_arg=[True]+arg[:]
        no_arg=[False]+arg[:]
        self.dialogYes.bind(DGG.B1PRESS, command, yes_arg)
        self.dialogNo.bind(DGG.B1PRESS, command, no_arg)
        
    def okDialog(self, text, command, arg=[]):
        self.dialog.show()
        self.dialogYes.hide()
        self.dialogNo.hide()
        self.dialogOk.show()        
        self.dialog['text']=text
        self.dialogOk.bind(DGG.B1PRESS, command, arg)
        

    def addSaveLoadDialog(self, save_command, load_command, cancel_command):
        #save/load 
        self.SaveLoadFrame=DirectFrame( frameSize=_rec2d(512,540),
                                        frameColor=(0,0,0, 0.8),
                                        text="Directory:\n\nHeight:\n\nDetail:\n\nGrass:\n\nObjects &\nTextures:\n\nCollision:\n\nWalkMap:",
                                        text_scale=32,
                                        text_font=self.fontBig,
                                        text_pos=(-440,505),
                                        text_fg=(0.7,0.7,0.7,1),
                                        parent=self.Center)
        _resetPivot(self.SaveLoadFrame)
        self.SaveLoadFrame.setPos(_pos2d(-256, -256))
        self.entry1 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = self.path+"save/default1",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText= self.path+"save/default1",
                        numLines = 2,
                        width=19,
                        focus=0,
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry1)
        self.entry1.setPos(_pos2d(150,8))
        self.entry2 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = "heightmap.png",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="heightmap.png",
                        numLines = 2,
                        width=19,
                        focus=0,
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry2)
        self.entry2.setPos(_pos2d(150,70))
        self.entry3 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = "detail.png",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="detail.png",
                        numLines = 2,
                        width=19,
                        focus=0,
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry3)
        self.entry3.setPos(_pos2d(150,132))        
        
        self.entry5 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text ="grass.png",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="grass.png",
                        numLines = 2,
                        width=19,
                        focus=0,
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry5)
        self.entry5.setPos(_pos2d(150,194))
        self.entry6 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = "objects.json",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="objects.json",
                        numLines = 2,
                        width=19,
                        focus=0,
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry6)
        self.entry6.setPos(_pos2d(150,270)) 
        self.entry7 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = "collision.egg",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="collision.egg",
                        numLines = 2,
                        width=19,
                        focus=0, 
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry7)
        self.entry7.setPos(_pos2d(150,350))
        self.entry8 = DirectEntry(frameSize=_rec2d(310,40),
                        frameColor=(1,1,1, 0.3),
                        text = "navmesh",
                        text_scale=16,
                        text_pos=(-308,18),
                        text_fg=(1,1,1,1),
                        initialText="navmesh",
                        numLines = 2,
                        width=19,
                        focus=0, 
                        suppressKeys=True,
                        parent=self.SaveLoadFrame
                        )
        _resetPivot(self.entry8)
        self.entry8.setPos(_pos2d(150,420))        
        
        self.check1=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check1)
        self.check1.setPos(_pos2d(464,72))
        self.check2=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check2)
        self.check2.setPos(_pos2d(464,134))
        self.check3=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check3)
        self.check3.setPos(_pos2d(464,196))
        
        self.check5=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check5)
        self.check5.setPos(_pos2d(464,272))
        self.check6=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check6)
        self.check6.setPos(_pos2d(464,352))
        
        self.check7=DirectFrame(frameSize=_rec2d(32,32),
                                frameColor=(1,1,1,0.99),                      
                                frameTexture='icon/yes.png',
                                state=DGG.NORMAL, 
                                parent=self.SaveLoadFrame)
        _resetPivot(self.check7)
        self.check7.setPos(_pos2d(464,422))
        
        self.check1.bind(DGG.B1PRESS, self.switchFlag, [0])
        self.check2.bind(DGG.B1PRESS, self.switchFlag, [1])
        self.check3.bind(DGG.B1PRESS, self.switchFlag, [2])
        
        self.check5.bind(DGG.B1PRESS, self.switchFlag, [4])
        self.check6.bind(DGG.B1PRESS, self.switchFlag, [5])
        self.check7.bind(DGG.B1PRESS, self.switchFlag, [6])
        
        self.checkers=[self.check1,self.check2,self.check3,None,self.check5,self.check6,self.check7]        
        self.flags=[]
        for check in self.checkers:
            self.flags.append(True)
        
        self.saveButton=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="SAVE",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-70,7),
                                    text_fg=(0,1,0,1),
                                    state=DGG.NORMAL, 
                                    parent=self.SaveLoadFrame)
        _resetPivot(self.saveButton)
        self.saveButton.setPos(_pos2d(32,478))
        
        self.loadButton=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="LOAD",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-70,7),
                                    text_fg=(0,0,1,1),
                                    state=DGG.NORMAL, 
                                    parent=self.SaveLoadFrame)
        _resetPivot(self.loadButton)
        self.loadButton.setPos(_pos2d(352,478))
        
        self.cancelButton=DirectFrame(frameSize=_rec2d(128,32),
                                    frameColor=(1,1,1,0.5),  
                                    text="CANCEL",
                                    text_scale=32,
                                    text_font=self.fontBig,
                                    text_pos=(-66,7),
                                    text_fg=(1,0,0,1),
                                    state=DGG.NORMAL, 
                                    parent=self.SaveLoadFrame)
        _resetPivot(self.cancelButton)
        self.cancelButton.setPos(_pos2d(192,478))
        
        self.saveButton.bind(DGG.B1PRESS, save_command, ["ASK"])
        self.loadButton.bind(DGG.B1PRESS, load_command)
        self.cancelButton.bind(DGG.B1PRESS, cancel_command)
        
        self.SaveLoadFrame.hide()
    
    def _setColor(self, frame, color):
        frame['frameColor']=color
        
    def blink(self, element, button=None):
        if button==None:
            frame=self.elements[element]['frame']        
        else:
            frame=self.elements[element]['buttons'][button]
        old_color=frame['frameColor']
        new_color=(1-old_color[0],1-old_color[1], 1-old_color[2], 1-old_color[3])
        Sequence(Func(self._setColor,frame,new_color), Wait(0.1),Func(self._setColor,frame,old_color)).start()
        
    def grayOutButtons(self, toolbar, from_to, but_not, on_color=(1,1,1, 1), off_color=(0.4,0.4,0.4, 1)):
        for i in range(from_to[0], from_to[1]):
            self.elements[toolbar]['buttons'][i]['frameColor']=off_color
        if but_not!=None:
            self.elements[toolbar]['buttons'][but_not]['frameColor']=on_color
            
    def switchFlag(self, flag_id, event=None):
        if self.flags[flag_id]:
            self.flags[flag_id]=False
            self.checkers[flag_id]['frameTexture']='icon/no.png'
        else:
            self.flags[flag_id]=True
            self.checkers[flag_id]['frameTexture']='icon/yes.png'
            
    def updateBaseNodes(self):
        wp=base.win.getProperties()
        winX = wp.getXSize()
        winY = wp.getYSize()    
            
        self.TopLeft.setPos(_pos2d(0,0))
        self.TopRight.setPos(_pos2d(winX,0))        
        self.BottomRight.setPos(_pos2d(winX,winY))
        self.BottomLeft.setPos(_pos2d(0,winY))
        self.Top.setPos(_pos2d(winX/2,0))
        self.Bottom.setPos(_pos2d(winX/2,winY))
        self.Left.setPos(_pos2d(0,winY/2))
        self.Right.setPos(_pos2d(winX,winY/2))
        self.Center.setPos(_pos2d(winX/2,winY/2))
    
    def hideElement(self, id):
        self.elements[id]['frame'].hide()
    
    def showElement(self, id):
        self.elements[id]['frame'].show()
    
    def addScrolledToolbar(self, parent, width, canvas_size, x_offset=0, y_offset=0, hover_command=False, color=(1,0,0, 0)):         
        wp=base.win.getProperties()        
        height=wp.getYSize()-y_offset-256
        frame=DirectScrolledFrame(canvasSize = _rec2d(canvas_size[0],canvas_size[1]),
                                  frameSize = _rec2d(width,height),                              
                                  verticalScroll_frameSize=_rec2d(16,height), 
                                  verticalScroll_frameColor=(0, 0, 1, 0),
                                  frameColor=color,
                                  manageScrollBars=False,
                                  autoHideScrollBars=False, 
                                  verticalScroll_thumb_frameColor=(1, 1, 1, 0.8),                              
                                  parent=parent                              
                                )         
        frame.verticalScroll['value']=0
        frame.verticalScroll['incButton_relief']=None
        frame.verticalScroll['incButton_state'] = DGG.DISABLED
        frame.verticalScroll['decButton_relief']=None
        frame.verticalScroll['decButton_state'] = DGG.DISABLED
        _resetPivot(frame)
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setX(frame, x_offset)
        frame.setZ(frame, -y_offset)
        if hover_command:
            frame['state']=DGG.NORMAL
            frame.bind(DGG.WITHOUT, hover_command,[False])  
            frame.bind(DGG.WITHIN, hover_command, [True]) 
        data={'size':canvas_size[1], 'frame':frame, 'buttons':[]}
        id=len(self.elements)
        self.elements.append(data)
        return id
        
    def addListButton(self, parent_id, text, command, arg=[], tooltip=None, tooltip_text=None):
        parent=self.elements[parent_id]['frame'].getCanvas()
        id=len(self.elements[parent_id]['buttons'])
        y_offset=self.elements[parent_id]['size']-20
        frame= DirectFrame( frameSize=_rec2d(174,20),
                        frameColor=(0,0,0,0.6),
                        state=DGG.NORMAL,                        
                        text=text,
                        text_scale=16,
                        text_pos=(-172,7),
                        text_fg=(1,1,1,1),
                        text_align=TextNode.ALeft,
                        parent=parent)
        #_resetPivot(frame)        
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setPos(_pos2d(-10,-y_offset+21*id))        
        self.elements[parent_id]['buttons'].append(frame)
        arg.append(id)
        frame.bind(DGG.B1PRESS, command, arg)        
        if tooltip:            
            frame.bind(DGG.WITHIN, self.setTooltip,[tooltip, tooltip_text])  
            frame.bind(DGG.WITHOUT, self.setTooltip,[tooltip, None])  
        
    def addPropPanel(self):   
        mainFrame=DirectFrame( frameSize=_rec2d(192,256),
                        frameColor=(0, 0, 0, 0.8),  
                        text=" GRID SNAP:\n\n         PROPERTIES:",
                        text_align=TextNode.ALeft,
                        text_scale=16,
                        text_pos=(-192,240),
                        text_fg=(1,1,1,1),                        
                        parent=self.BottomRight)
        _resetPivot(mainFrame)                
        mainFrame.setPos(_pos2d(-192, -256))
        frame=DirectScrolledFrame(canvasSize = _rec2d(192,500),
                                  frameSize = _rec2d(192,200),                              
                                  verticalScroll_frameSize=_rec2d(16,200), 
                                  verticalScroll_frameColor=(0, 0, 1, 0),
                                  frameColor=(0,0,0, 0.0),
                                  manageScrollBars=False,
                                  autoHideScrollBars=False, 
                                  verticalScroll_thumb_frameColor=(1, 1, 1, 0.8),                              
                                  parent=mainFrame                              
                                )         
        frame.verticalScroll['value']=0
        frame.verticalScroll['incButton_relief']=None
        frame.verticalScroll['incButton_state'] = DGG.DISABLED
        frame.verticalScroll['decButton_relief']=None
        frame.verticalScroll['decButton_state'] = DGG.DISABLED           
        _resetPivot(frame)
        frame.setZ(frame, -56)
        #frame.setX(frame, 16)
        snap = DirectEntry(frameSize=_rec2d(80,18),
                        frameColor=(1,1,1, 0.4),
                        text ="0.5",
                        text_scale=16,
                        text_pos=(-80,6),
                        text_align=TextNode.ALeft,
                        text_fg=(1,1,1,1),
                        initialText="0.5",
                        width=5,
                        focus=0,
                        suppressKeys=True,
                        parent=mainFrame
                        )    
        _resetPivot(snap)
        snap.setPos(_pos2d(112, 4))
        props = DirectEntry(frameSize=_rec2d(190,500),
                        frameColor=(1,1,1, 0.4),
                        text ="",
                        text_scale=16,
                        text_pos=(-190,484),
                        text_fg=(1,1,1,1),
                        initialText="",
                        numLines = 30,
                        width=11,
                        focus=0,
                        suppressKeys=True,
                        parent=frame.getCanvas()
                        )                    
        id=len(self.elements)
        self.elements.append({'frame':mainFrame, 'entry_props':props, 'entry_snap':snap})                    
        return id
                
    def addToolbar(self, parent, size, icon_size=32, x_offset=0, y_offset=0, hover_command=False, color=(1,0,0, 0)):         
        frame=DirectFrame( frameSize=_rec2d(size[0],size[1]),
                        frameColor=color,                        
                        state=DGG.NORMAL,   
                        parent=parent)
        _resetPivot(frame)
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setX(frame, x_offset)
        frame.setZ(frame, -y_offset)
        if hover_command:
            frame.bind(DGG.WITHOUT, hover_command,[False])  
            frame.bind(DGG.WITHIN, hover_command, [True]) 
        data={'size':size[0], 'icon_size':icon_size, 'frame':frame, 'buttons':[]}
        id=len(self.elements)
        self.elements.append(data)
        return id
        
    def addButton(self, toolbar, icon, command, arg=[], tooltip=None, tooltip_text=None):
        size=self.elements[toolbar]['icon_size']
        parent=self.elements[toolbar]['frame']
        max_x=self.elements[toolbar]['size']
        x=len(self.elements[toolbar]['buttons'])*size
        y=0
        while x>=max_x:
            y+=size
            x-=max_x
        
        frame= DirectFrame( frameSize=_rec2d(size,size),
                        frameColor=(1,1,1,1),
                        state=DGG.NORMAL,                        
                        frameTexture=icon,
                        parent=parent)
        _resetPivot(frame)
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setPos(_pos2d(x,y))
        frame.bind(DGG.B1PRESS, command, arg)
        self.elements[toolbar]['buttons'].append(frame)
        if tooltip:            
            frame.bind(DGG.WITHIN, self.setTooltip,[tooltip, tooltip_text])  
            frame.bind(DGG.WITHOUT, self.setTooltip,[tooltip, None])  
            
    def addFloatingButton(self, parent_id, size, icon, pos, command, arg=[], tooltip=None, tooltip_text=None):  
        parent=self.elements[parent_id]['frame']
        frame= DirectFrame( frameSize=_rec2d(size[0],size[1]),
                        frameColor=(1,1,1,1),
                        state=DGG.NORMAL,                        
                        frameTexture=icon,
                        parent=parent)
        _resetPivot(frame)
        frame.setPos(_pos2d(pos[0],pos[1]))
        frame.setTransparency(TransparencyAttrib.MDual)        
        frame.bind(DGG.B1PRESS, command, arg)
        self.elements.append({'frame':frame})
        if tooltip:            
            frame.bind(DGG.WITHIN, self.setTooltip,[tooltip, tooltip_text])  
            frame.bind(DGG.WITHOUT, self.setTooltip,[tooltip, None]) 
        return frame
        
    def addInfoIcon(self, toolbar, icon, text, tooltip=None, tooltip_text=None):       
        parent=self.elements[toolbar]['frame']
        x=len(self.elements[toolbar]['buttons'])*64
          
        frame= DirectFrame( frameSize=_rec2d(64,64),
                        frameColor=(1,1,1,1),                   
                        frameTexture=icon,
                        text=text,
                        text_scale=16,
                        text_pos=(-32,16),
                        text_fg=(0,0,0,1),
                        parent=parent)
        _resetPivot(frame)
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setPos(_pos2d(x,0))
        self.elements[toolbar]['buttons'].append(frame)
        if tooltip:  
            frame['state']=DGG.NORMAL
            frame.bind(DGG.WITHIN, self.setTooltip,[tooltip, tooltip_text])  
            frame.bind(DGG.WITHOUT, self.setTooltip,[tooltip, None])
        return frame
        
    def setTooltip(self, tooltip, tooltip_text, guiEvent=None):
        if tooltip_text:
            tooltip.show()
            tooltip['text']=tooltip_text            
        else:    
            tooltip.hide()
            
    def addTooltip(self, parent,size, x_offset=0, y_offset=0):
        frame=DirectFrame( frameSize=_rec2d(size[0],size[1]),
                        frameColor=(0,0,0, 0.5),  
                        text="test",
                        text_scale=16,
                        text_align=TextNode.ALeft,
                        text_pos=(-size[0]+10,14),
                        text_fg=(1,1,1,1),                        
                        state=DGG.NORMAL,   
                        parent=parent)
        _resetPivot(frame)
        frame.setTransparency(TransparencyAttrib.MDual)
        frame.setX(frame, x_offset)
        frame.setZ(frame, -y_offset)
        return frame
    
    