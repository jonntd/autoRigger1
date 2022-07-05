import maya.cmds as cmds

def _getTransform(inList, t=False, r=False, ws=False, os=False):
    outData = []
    for i in inList:
        dic = {'name':i}
        if t==True:
            pos = cmds.xform(i, q=True, ws=ws, os=os, t=True)
            dic['pos']=pos
        
        if r==True:
            rot = cmds.getAttr(i+'.r')[0]
            dic['rot']=rot
            
        outData.append(dic)
    return tuple(outData)

def _applyTransform(inData, ws=False, os=False):
    for i in inData:
        if 'pos' in i:
            pos = i['pos']
            try:cmds.move(pos[0],pos[1],pos[2],i['name'], ws=ws, os=os)
            except:print('applyTransform ERROR: No object matches name:',i['name'])
        
        if 'rot' in i: 
            rot = i['rot']
            try:cmds.rotate(rot[0],rot[1],rot[2],i['name'])
            except:print('applyTransform ERROR: No object matches name:',i['name'])
        
        if 'scl' in i:
            scl = i['scl']
            try:cmds.scale(scl[0],scl[1],scl[2],i['name'])
            except:print('applyTransform ERROR: No object matches name:',i['name'])
            