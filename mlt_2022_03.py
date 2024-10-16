#!/usr/bin/env python
'''
Created on Jul 7, 2014

@author: roj-idl71
'''
import os, sys
import json

#path = os.path.dirname(os.getcwd())
#path = os.path.join(path, 'source')
#sys.path.insert(0, path)

from schainpy.controller import Project

if __name__ == '__main__':
    
    desc = "JULIA raw experiment "
    filename = "schain.xml"

    #dpath = '/media/pcondor/DATA1/mlt/data'
    dpath = '/media/pcondor/Nuevo vol/mlt'
    figpath = "/media/pcondor/DATA1/mlt/winds"
    procpath = "/media/pcondor/DATA1/mlt/winds/datamom"
    procpath2 = "/media/pcondor/DATA1/mlt/winds/datawinds"
    remotefolder = "/home/wmaster/graficos"
    db_range=['20','35']
    tiempo=['0','24']
    altura1=[2,20]
    altura2=[80,170]
    velocity=['-80','80']
    period=60
# PROJECT 1
    
    controllerObj = Project()
    controllerObj.setup(id = '191', name='MLTwinds', description=desc)
    
    readUnitConfObj1 = controllerObj.addReadUnit(datatype='Voltage',
                                                path=dpath,
                                                startDate='2022/03/09',
                                                endDate='2022/03/09',
                                                startTime='00:00:00',
                                                endTime='23:59:59',
                                                online=0,
                                                walk=0,
                                                expLabel='',
                                                getByBlock=1,
						delay=20)
    
#    opObj00 = readUnitConfObj.addOperation(name='printInfo')
#    opObj00 = readUnitConfObj.addOperation(name='printNumberOfBlock')
#-------------------------  Down proc ---------------------        
    procUnitConfObj1 = controllerObj.addProcUnit(datatype='Voltage', inputId=readUnitConfObj1.getId())
    
    opObj11 = procUnitConfObj1.addOperation(name='selectChannels')
    opObj11.addParameter(name='channelList', value='0,1', format='intlist')
    opObj11 = procUnitConfObj1.addOperation(name='ProfileSelector', optype='other')
    opObj11.addParameter(name='profileRangeList', value='(0, 999)', format='intlist')
    '''
    opObj11 = procUnitConfObj1.addOperation(name='selectHeights')
    opObj11.addParameter(name='minHei', value=altura1[0], format='float')
    opObj11.addParameter(name='maxHei', value=altura1[1], format='float')
    '''
    code = [[1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1],[1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1]]
    opObj11 = procUnitConfObj1.addOperation(name='Decoder', optype='other')
    opObj11.addParameter(name='code', value=code, format='floatlist')
    opObj11.addParameter(name='nCode', value='4', format='int')
    opObj11.addParameter(name='nBaud', value='32', format='int')

    opObj11 = procUnitConfObj1.addOperation(name='CohInt', optype='other')
    opObj11.addParameter(name='n', value=8, format='int')
    
    opObj11 = procUnitConfObj1.addOperation(name='selectHeights')
    opObj11.addParameter(name='minHei', value=60, format='float')
    opObj11.addParameter(name='maxHei', value=85, format='float')

    procUnitConfObj1SPC = controllerObj.addProcUnit(datatype='Spectra', inputId=procUnitConfObj1.getId())
    procUnitConfObj1SPC.addParameter(name='nFFTPoints', value='125', format='int')
    procUnitConfObj1SPC.addParameter(name='nProfiles', value='125', format='int')
    procUnitConfObj1SPC.addParameter(name='runNextUnit', value=True)

    opObj11 = procUnitConfObj1SPC.addOperation(name='IncohInt', optype='other')
    #opObj11.addParameter(name='n', value='20', format='int')
    #opObj11.addParameter(name='n', value='5', format='int')
    opObj11.addParameter(name='n', value='10', format='int')

#    opObj11 = procUnitConfObj1SPC.addOperation(name='SpectraWriter', optype='other')
#    opObj11.addParameter(name='path', value= procpath)
#    opObj11.addParameter(name='blocksPerFile', value='80', format='int')
    '''
    opObj11 = procUnitConfObj1SPC.addOperation(name='removeDC')
    opObj11.addParameter(name='mode', value='2', format='int')
    '''
#    opObj11 = procUnitConfObj1SPC.addOperation(name='removeInterference')
    
    #opObj11 = procUnitConfObj1SPC.addOperation(name='SpectraPlot', optype='other')
    #opObj11.addParameter(name='id', value='1', format='int')
    #opObj11.addParameter(name='wintitle', value='MLT DOWN', format='str')
    #opObj11.addParameter(name='zmin', value=db_range[0], format='int')     
    #opObj11.addParameter(name='zmax', value=db_range[1], format='int')
    #opObj11.addParameter(name='xaxis', value='velocity', format='str')
    #opObj11.addParameter(name='showprofile', value='1', format='int')  
    #opObj11.addParameter(name='save', value=figpath, format='str')

    #opObj11 = procUnitConfObj1SPC.addOperation(name='RTIPlot', optype='other')
    #opObj11.addParameter(name='id', value='10', format='int')
    #opObj11.addParameter(name='wintitle', value='MLT DOWN', format='str')
    #opObj11.addParameter(name='xmin', value=tiempo[0], format='float')
    #opObj11.addParameter(name='xmax', value=tiempo[1], format='float')
    #opObj11.addParameter(name='zmin', value=db_range[0], format='int')
    #opObj11.addParameter(name='zmax', value=db_range[1], format='int')
    #opObj11.addParameter(name='save', value=figpath, format='str')
#--------------------    Parameters Processing Unit  down  ------------

    procUnitConfObj2 = controllerObj.addProcUnit(datatype='ParametersProc', inputId=procUnitConfObj1SPC.getId())
    #procUnitConfObj2.addParameter(name='runNextUnit', value=True)
    opObj21 = procUnitConfObj2.addOperation(name='SpectralMoments', optype='other')
    #opObj21 = procUnitConfObj2.addOperation(name='GetMoments')


    #opObj22 = procUnitConfObj2.addOperation(name='SpectralMomentsPlot', optype='other')
    #opObj22.addParameter(name='id', value='003', format='int')
    ##opObj22.addParameter(name='ymin', value='60', format='int')
    ##opObj22.addParameter(name='ymax', value='85', format='int')
    #opObj22.addParameter(name='zmin', value=db_range[0], format='int')
    #opObj22.addParameter(name='zmax', value=db_range[1], format='int')
    #opObj22.addParameter(name='save', value=figpath, format='str')
   
    #opObj22 = procUnitConfObj2.addOperation(name='DopplerPlot', optype='other')
    #opObj22.addParameter(name='id', value='005', format='int')
    ##opObj22.addParameter(name='paramIndex', value='1', format='int')
    ##opObj22.addParameter(name='colormap', value='0', format='bool')
    #opObj22.addParameter(name='xmin', value=tiempo[0], format='float')
    #opObj22.addParameter(name='xmax', value=tiempo[1], format='float')
    #opObj22.addParameter(name='SNRmin', value='-3', format='int')
    #opObj22.addParameter(name='SNRmax', value='6', format='int')
    #opObj22.addParameter(name='save', value=figpath, format='str')
    #opObj22.addParameter(name='showSNR', value='1', format='bool')
   ## opObj22.addParameter(name='SNRthresh', value='-6', format='float')

    #opObj24 = procUnitConfObj2.addOperation(name='HDFWriter', optype='other')
    #opObj24.addParameter(name='path', value=procpath)
    #opObj24.addParameter(name='blocksPerFile', value='100', format='int')
    #opObj24.addParameter(name='metadataList', value='type,inputUnit,heightList,paramInterval,timeZone', format='list')
    #opObj24.addParameter(name='dataList', value='moments,data_snr,noise,utctime,utctimeInit', format='list')
    ##opObj24.addParameter(name='dataList', value='data_param,data_SNR,noise,utctime,utctimeInit', format='list')
    ##opObj24.addParameter(name='mode', value='1', format='int')

#---------------------  Up proc -------------------------------------
    procUnitConfObj3 = controllerObj.addProcUnit(datatype='Voltage', inputId=readUnitConfObj1.getId())
    
    opObj31 = procUnitConfObj3.addOperation(name='selectChannels')
    opObj31.addParameter(name='channelList', value='2,3', format='intlist')
    opObj31 = procUnitConfObj3.addOperation(name='ProfileSelector', optype='other')
    opObj31.addParameter(name='profileRangeList', value='(0, 999)', format='intlist')
    '''
    opObj11 = procUnitConfObj1.addOperation(name='selectHeights')
    opObj11.addParameter(name='minHei', value=altura1[0], format='float')
    opObj11.addParameter(name='maxHei', value=altura1[1], format='float')
    '''
    #code = [[1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1],[1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1]]
    code = [[1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,1],[-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,1,1,1],[-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1],[1,-1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1]]
    opObj31 = procUnitConfObj3.addOperation(name='Decoder', optype='other')
    opObj31.addParameter(name='code', value=code, format='floatlist')
    opObj31.addParameter(name='nCode', value='4', format='int')
    opObj31.addParameter(name='nBaud', value='32', format='int')

    opObj31 = procUnitConfObj3.addOperation(name='CohInt', optype='other')
    opObj31.addParameter(name='n', value=8, format='int')
    
    opObj31 = procUnitConfObj3.addOperation(name='selectHeights')
    opObj31.addParameter(name='minHei', value=60, format='float')
    opObj31.addParameter(name='maxHei', value=85, format='float')

    procUnitConfObj2SPC = controllerObj.addProcUnit(datatype='Spectra', inputId=procUnitConfObj3.getId())
    procUnitConfObj2SPC.addParameter(name='nFFTPoints', value='125', format='int')
    procUnitConfObj2SPC.addParameter(name='nProfiles', value='125', format='int')

    opObj31 = procUnitConfObj2SPC.addOperation(name='IncohInt', optype='other')
    #opObj11.addParameter(name='n', value='20', format='int')
    #opObj11.addParameter(name='n', value='5', format='int')
    opObj31.addParameter(name='n', value='10', format='int')

#    opObj21 = procUnitConfObj2SPC.addOperation(name='SpectraWriter', optype='other')
#    opObj21.addParameter(name='path', value= procpath)
#    opObj21.addParameter(name='blocksPerFile', value='80', format='int')
    '''
    opObj11 = procUnitConfObj1SPC.addOperation(name='removeDC')
    opObj11.addParameter(name='mode', value='2', format='int')
    '''
#    opObj21 = procUnitConfObj1SPC.addOperation(name='removeInterference')
    
    '''
    opObj31 = procUnitConfObj2SPC.addOperation(name='SpectraPlot', optype='other')
    opObj31.addParameter(name='id', value='1', format='int')
    opObj31.addParameter(name='wintitle', value='MLT_UP', format='str')
    opObj31.addParameter(name='zmin', value=db_range[0], format='int')     
    opObj31.addParameter(name='zmax', value=db_range[1], format='int')
    opObj31.addParameter(name='xaxis', value='velocity', format='str')
#    opObj11.addParameter(name='ymin', value=altura1[0], format='int')     
#    opObj11.addParameter(name='ymax', value=altura1[1], format='int')
#    opObj11.addParameter(name='xmin', value=velocity[0], format='int')     
#    opObj11.addParameter(name='xmax', value=velocity[1], format='int')
    opObj31.addParameter(name='showprofile', value='1', format='int')  
    opObj31.addParameter(name='save', value=figpath, format='str')

    opObj31 = procUnitConfObj2SPC.addOperation(name='RTIPlot', optype='other')
    opObj31.addParameter(name='id', value='10', format='int')
    opObj31.addParameter(name='wintitle', value='MLT DOWN', format='str')
    opObj31.addParameter(name='xmin', value=tiempo[0], format='float')
    opObj31.addParameter(name='xmax', value=tiempo[1], format='float')
#    opObj11.addParameter(name='ymin', value=altura1[0], format='int')     
#    opObj11.addParameter(name='ymax', value=altura1[1], format='int')
    opObj31.addParameter(name='zmin', value=db_range[0], format='int')
    opObj31.addParameter(name='zmax', value=db_range[1], format='int')
    #opObj11.addParameter(name='showprofile', value='1', format='int')
    opObj31.addParameter(name='save', value=figpath, format='str')
    '''
#--------------------    Parameters Processing Unit  up  ------------

    procUnitConfObj4 = controllerObj.addProcUnit(datatype='ParametersProc', inputId=procUnitConfObj2SPC.getId())
    #procUnitConfObj4.addParameter(name='runNextUnit', value=True)

    opObj41 = procUnitConfObj4.addOperation(name='SpectralMoments', optype='other')
    #opObj21 = procUnitConfObj2.addOperation(name='GetMoments')
    '''
    opObj42 = procUnitConfObj4.addOperation(name='SpectralMomentsPlot', optype='other')
    opObj42.addParameter(name='id', value='003', format='int')
    #opObj22.addParameter(name='ymin', value='60', format='int')
    #opObj22.addParameter(name='ymax', value='85', format='int')
    opObj42.addParameter(name='zmin', value=db_range[0], format='int')
    opObj42.addParameter(name='zmax', value=db_range[1], format='int')
    opObj42.addParameter(name='save', value=figpath, format='str')
   
    opObj42 = procUnitConfObj4.addOperation(name='DopplerPlot', optype='other')
    opObj42.addParameter(name='id', value='005', format='int')
    #opObj22.addParameter(name='paramIndex', value='1', format='int')
    #opObj22.addParameter(name='colormap', value='0', format='bool')
    opObj42.addParameter(name='xmin', value=tiempo[0], format='float')
    opObj42.addParameter(name='xmax', value=tiempo[1], format='float')
    opObj42.addParameter(name='SNRmin', value='-3', format='int')
    opObj42.addParameter(name='SNRmax', value='6', format='int')
    opObj42.addParameter(name='save', value=figpath, format='str')
    opObj42.addParameter(name='showSNR', value='1', format='bool')
    '''
    
#------------------Merge Down and UP ------------------
    merge = controllerObj.addProcUnit(datatype='MergeProc',inputId=[procUnitConfObj2.getId(),procUnitConfObj4.getId()])

    merge.addParameter(name='attr_data', value='moments')
    merge.addParameter(name='attr_data_2', value='data_snr')
    #merge.addParameter(name='attr_data_3', value='heightList')
    merge.addParameter(name='mode', value='5')

    opObj52 = merge.addOperation(name='HDFWriter', optype='other')
    opObj52.addParameter(name='path', value=procpath)
    opObj52.addParameter(name='blocksPerFile', value='100', format='int')
    opObj52.addParameter(name='metadataList', value='type,inputUnit,heightList,paramInterval,timeZone', format='list')
    opObj52.addParameter(name='dataList', value='moments,data_snr,noise,utctime,utctimeInit', format='list')
    ##opObj52.addParameter(name='dataList', value='data_param,data_SNR,noise,utctime,utctimeInit', format='list')
    ##opObj52.addParameter(name='mode', value='1', format='int')
    
    opObj53 = merge.addOperation(name='WindProfiler', optype='other')
    opObj53.addParameter(name='technique', value='DBS', format='str')
    opObj53.addParameter(name='dirCosx', value='0.0, -0.0, -0.04, 0.04', format='floatlist') 
    opObj53.addParameter(name='dirCosy', value='0.0, -0.0, -0.04, -0.03', format='floatlist')
    opObj53.addParameter(name='correctAzimuth', value='0', format='float')
    #opObj23.addParameter(name='correctAzimuth', value='52.5414', format='float')
    opObj53.addParameter(name='correctFactor', value='-1', format='float')
    
    '''
    opObj54 = merge.addOperation(name='WindProfilerPlot', optype='other')
    opObj54.addParameter(name='id', value='004', format='int')
    opObj54.addParameter(name='xmin', value=0, format='float')
    opObj54.addParameter(name='xmax', value=24, format='float')
    opObj54.addParameter(name='ymin', value='0', format='float')
    opObj54.addParameter(name='ymax', value='30', format='float')
    opObj54.addParameter(name='save', value=figpath, format='str')
    #opObj54.addParameter(name='figpath', value=pathfig, format='str')
    opObj54.addParameter(name='zmin', value='-15', format='float')
    opObj54.addParameter(name='zmax', value='15', format='float')
    opObj54.addParameter(name='zmin_ver', value='-60', format='float')
    opObj54.addParameter(name='zmax_ver', value='60', format='float')
    opObj54.addParameter(name='SNRmin', value='-10', format='int')
    opObj54.addParameter(name='SNRmax', value='40', format='int')
    opObj54.addParameter(name='SNRthresh', value='-6', format='float')
    '''
    titles=('Zonal Wind,Meriodinal Wind,Vertical Wind')
    
    opObj54 = merge.addOperation(name='GenericRTIPlot')
    opObj54.addParameter(name='colormaps', value='RdBu_r,RdBu_r,RdBu_r')
    opObj54.addParameter(name='attr_data', value='data_output')
#opObj23.addParameter(name='colormaps', value='RdBu,RdBu')
#opObj23.addParameter(name='attr_data', value='data_output')
    opObj54.addParameter(name='wintitle', value='Winds')
    opObj54.addParameter(name='save', value=figpath)
    opObj54.addParameter(name='titles', value=titles)
    opObj54.addParameter(name='zfactors', value='1,1,1')
    opObj54.addParameter(name='zlimits', value='(-100,100),(-100,100),(-60,60)')
    opObj54.addParameter(name='cb_labels', value='m/s,m/s,cm/s')
    opObj54.addParameter(name='throttle', value='1')
    opObj54.addParameter(name='xmin', value=0)
    opObj54.addParameter(name='xmax', value=24)
    
    opObj55 = merge.addOperation(name='HDFWriter', optype='other')
    opObj55.addParameter(name='path', value=procpath2)
    opObj55.addParameter(name='blocksPerFile', value='100', format='int')
    opObj55.addParameter(name='metadataList',value='type,inputUnit,outputInterval',format='list')
    opObj55.addParameter(name='dataList',value='data_output,utctime,heightList',format='list')    
    #opObj55.addParameter(name='metadataList', value='type,inputUnit,heightList,paramInterval,timeZone', format='list')
    #opObj55.addParameter(name='dataList', value='moments,data_snr,noise,utctime,utctimeInit', format='list')
    #opObj55.addParameter(name='dataList', value='data_param,data_SNR,noise,utctime,utctimeInit', format='list')
    #opObj55.addParameter(name='mode', value='1', format='int')
    
    controllerObj.start()
    