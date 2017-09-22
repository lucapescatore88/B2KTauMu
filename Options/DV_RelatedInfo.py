from Gaudi.Configuration       import *
from GaudiKernel.SystemOfUnits import *
from Configurables import LoKi__Hybrid__TupleTool

def getLoKiToolsDictionary():

    reldict = {'RELINFO':{}}
    myvars = {
        #add RelInfoConeVariables
        'cone' : {'vars' : ['CONEANGLE', 'CONEMULT', 'CONEPTASYM','CONEPT','CONEP','CONEPASYM','CONEDELTAETA','CONEDELTAPHI'],
                  'locations' : ['ConeVarsInfoL1','ConeVarsInfoL2','ConeVarsInfoH'] },
        #add RelInfoTrackIsolationBDT
        'isoBDT' : {'vars' : ['TRKISOBDTFIRSTVALUE','TRKISOBDTSECONDVALUE','TRKISOBDTTHIRDVALUE'],
                    'locations' : ['TrackIsoBDTInfoL1','TrackIsoBDTInfoL2','TrackIsoBDTInfoH'] } ,
        #add RelInfoConeIsolation
        'coneIso' : {'vars' : ['CC_ANGLE', 'CC_MULT','CC_PX', 'CC_PY', 'CC_PZ', 'CC_VPT', 'CC_SPT', 'CC_PASYM ', 'CC_PTASYM', 'CC_PXASYM', 'CC_PYASYM', 'CC_PZASYM', 'CC_DELTAETA', 'CC_DELTAPHI', 'CC_IT', 'NC_ANGLE', 'NC_MULT', 'NC_PX', 'NC_PY', 'NC_PZ', 'NC_VPT', 'NC_SPT', 'NC_PASYM', 'NC_PTASYM', 'NC_PXASYM', 'NC_PYASYM', 'NC_PZASYM', 'NC_DELTAETA', 'NC_DELTAPHI', 'NC_IT'],
                    'locations' : ['ConeIsoInfoL1','ConeIsoInfoL2','ConeIsoInfoH'] },
        #add RelInfoBs2MuMuTrackIsolations
        'Bs2MuMuIso' : {'vars' : ['BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO', 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS', 'ISOTWOBODYISO5PLUS', 'BSMUMUTRACKID', 'BSMUMUTRACKTOPID'],
                   'locations' : ['TrackIsoBsMMInfoL1', 'TrackIsoBsMMInfoL2', 'TrackIsoBsMMInfoH'] }
            }
    
    for name,vardict in myvars.iteritems() :
        for var in vardict['vars'] :
            for loc in vardict['locations'] :
                reldict['RELINFO'][loc+"_"+var] = {'varName':var,'Location':loc,'Default':-1.}

    #add RelInfoVertexIsolation
    for v in [ 'VTXISONUMVTX', 'VTXISODCHI2ONETRACK', 'VTXISODCHI2MASSONETRACK', 'VTXISODCHI2TWOTRACK', 'VTXISODCHI2MASSTWOTRACK']:
        reldict['RELINFO']['VtxIso_'+v] = {'varName':v,'Location':'VertexIsoInfo','Default':-1}

    #add RelInfoVertexIsolationBDT
    for v in [ 'VTXISOBDTHARDFIRSTVALUE', 'VTXISOBDTHARDSECONDVALUE', 'VTXISOBDTHARDTHIRDVALUE',]:
        reldict['RELINFO']['VtxIsoBDT_'+v] = {'varName':v,'Location':'VertexIsoBDTInfo','Default':-1.}
    
    return reldict

def getLoKiTool(name,line,isMC=True,branch = None) :

    lokiDict = getLoKiToolsDictionary()

    LoKi_Tool = LoKi__Hybrid__TupleTool('LoKi_Tool'+name)
    for vname, args in lokiDict['RELINFO'].iteritems():
        #if isMC : lokipath = '/AllStreams/Phys/'+line+'/'+args['Location']
        if isMC : lokipath = '/Event/Bu2KLL_NoPID_LongLived.Strip/Phys/'+line+'/'+args['Location']
        else : lokipath = '/Event/Leptonic/Phys/'+line+'/'+args['Location']
        LoKi_Tool.Variables[vname] = "RELINFO('%s','%s',%f)"%(lokipath,args['varName'],args['Default'])
    
    if branch is not None :
        branch.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_Tool"+name]
        branch.addTool(LoKi_Tool)
        #print "Added tool to tuple, ", branch

    return LoKi_Tool


