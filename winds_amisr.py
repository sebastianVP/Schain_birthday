import os, sys
import time
import datetime

'''
    ISR-ESF 1 BEAM ONLINE
'''
path = os.path.dirname(os.getcwd())
path = os.path.dirname(path)
sys.path.insert(0, path)

from schainpy.controller import Project
from shutil import rmtree

def main():
    desc = "AMISR 5 Beam Experiment"



    inPath = '/mnt/c/Users/soporte/Downloads/2024' #'/mnt/data_amisr'#
    #inpath= '/home/soporte/Data/AMISR-rawdata/2022'

    #outPath = '/mnt/DATA/AMISR14/2024/TW'
    outPath = '/home/soporte/BIRTHDAY'
    #outPath = '/home/soporte/Data/AMISR14/2024/ISR'
    #outPath = '/home/soporte/Data/AMISR-procdata/AMISR-proc120/2022/ISR/'
    procpath = "/mnt/c/Users/soporte/Downloads/proc_amisr"



    realtime_server='10.10.110.243:4444'



    localtime='1' #para ajustar el horario en las gráficas '0' para dejar en utc

    dty = datetime.date.today()                   #ONLINE
    str1 = dty + datetime.timedelta(days=1)
    str2 = dty - datetime.timedelta(days=1)
    #dty = dty - datetime.timedelta(days=1)  #diferencia restando 1 , probando data del 21
    today = dty.strftime("%Y/%m/%d")
    tomorrow = str1.strftime("%Y/%m/%d")
    yesterday = str2.strftime("%Y/%m/%d")
    startDate=today
    #startDate="2022/11/12"
    # endDate=tomorrow # se esta comentando para este caso particular y se colocara el mismo dia
    endDate=today
    ##.......................................................................................
    ##.......................................................................................
    l = startDate.split('/')                        #adding day of the year to outPath
    datelist = datetime.date(int(l[0]),int(l[1]),int(l[2]))
    DOY = datelist.timetuple().tm_yday
    outPath= outPath+"/online/"+l[0]+str(DOY).zfill(3)
    if os.path.exists(outPath):
        print("outPath", outPath)
    else :
        os.makedirs(outPath)
        print("Creating...", outPath)
    ##.......................................................................................
    ##.......................................................................................

    controllerObj = Project()
    controllerObj.setup(id = '21', name='esf_proc', description=desc)
    ##.......................................................................................
    ##.......................................................................................
    xmin = 7
    xmax = 18
    IPPms = 1 # 1mseg
    nChannels = 5
    nFFT=1
    nipp = (1000/IPPms)/nChannels
    ippP10sec = nipp*10
    print("{} profiles in 10 seconds".format(ippP10sec))

    readUnitConfObj = controllerObj.addReadUnit(datatype='AMISRReader',
                                                path=inPath,
                                                startDate='2024/08/22', #startDate,#'2016/07/12',
                                                endDate='2024/08/22', #endDate,#'2016/07/13',
                                                startTime='15:35:01', #'07:00:00',
                                                endTime='18:02:59', #'15:00:00',
                                                walk=1,
                                                timezone='lt',
                                                online=0, #1 ###### modo offline
                                                nOsamp = 1,
                                                nChannels=5,
                                                nFFT=1) #,
                                                ##margin_days=1,
                                                #ignStartDate=startDate,
                                                #ignEndDate=startDate,
                                                #ignStartTime='11:59:59',
                                                #ignEndTime='12:25:01')

    #AMISR Processing Unit
    ##.......................................................................................
    ##.......................................................................................

    #Voltage Processing Unit
    volts_proc = controllerObj.addProcUnit(datatype='VoltageProc', inputId=readUnitConfObj.getId())
    #opv = volts_proc.addOperation(name='ScopePlot')
    #opv.addParameter(name='title', value='VOLT ISR-AMISR', format='str')

    # opObj11 = volts_proc.addOperation(name='RemoveProfileSats2', optype='other')
    # opObj11.addParameter(name='n', value=ippP10sec, format='int') #funciona a 9600
    # opObj11.addParameter(name='minHei', value='200', format='int')
    # opObj11.addParameter(name='maxHei', value='900', format='int')
    # opObj11.addParameter(name='minRef', value='900', format='int')
    # opObj11.addParameter(name='maxRef', value='1000', format='int')
    # opObj11.addParameter(name='profile_margin', value=int(ippP10sec/10), format='int')
    # opObj11.addParameter(name='th_hist_outlier', value=11, format='int') #10<12
    # opObj11.addParameter(name='nProfilesOut', value=1, format='int')


    ###opObj02 = volts_proc.addOperation(name='SSheightProfiles2', optype='other')
    ###opObj02.addParameter(name='step', value=1, format='int')
    ###opObj02.addParameter(name='nsamples', value=120, format='int')
    
    ##.......................................................................................
    ##.......................................................................................
    # opObj12 = volts_proc.addOperation(name='selectHeights', optype='self')
    # opObj12.addParameter(name='minHei', value='90', format='float')
    # opObj12.addParameter(name='maxHei', value='500', format='float')

    opObj01 =  volts_proc.addOperation(name='CohInt', optype='other')
    opObj01.addParameter(name='n', value='6', format='int')

    #Spectra Unit Processing, getting spectras with nProfiles and nFFTPoints
    spc_proc = controllerObj.addProcUnit(datatype='SpectraProc', inputId=volts_proc.getId())
    spc_proc.addParameter(name='nFFTPoints', value=256, format='int') #120
    spc_proc.addParameter(name='ippFactor',value=5)
    #spc_proc.addParameter(name='zeroPad', value=True)
    #
    # REMOVE DC
    opObj11 = spc_proc.addOperation(name='removeDC')
    opObj11.addParameter(name='mode', value='2', format='int')

    opObj11 =  spc_proc.addOperation(name='IncohInt', optype='other')
    opObj11.addParameter(name='n', value='10', format='int')

    opObj03 = spc_proc.addOperation(name='getNoiseB', optype='other')
    opObj03.addParameter(name='offset', value='0.55', format='float')
    opObj03.addParameter(name='minHei', value='200', format='int')
    opObj03.addParameter(name='maxHei', value='350', format='int')
    opObj03.addParameter(name='minFreq', value='-40000', format='float')
    opObj03.addParameter(name='maxFreq', value='40000', format='float')

    ##.......................................................................................

    #--------------------    Parameters Processing Unit  up  ------------

    param_proc = controllerObj.addProcUnit(datatype='ParametersProc', inputId=spc_proc.getId())
    #procUnitConfObj4.addParameter(name='runNextUnit', value=True)

    opObj41 = param_proc.addOperation(name='SpectralMoments', optype='other')


    opObj52 = param_proc.addOperation(name='HDFWriter', optype='other')
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

    ##.......................................................................................

    #SpectraPlot
    '''
    opObj12 = spc_proc.addOperation(name='SpectraPlot', optype='external')
    opObj12.addParameter(name='wintitle', value='SPC ISR-AMISR', format='str')
    opObj12.addParameter(name='showprofile', value='0', format='int')
    opObj12.addParameter(name='xaxis', value='velocity', format='str')

    opObj12.addParameter(name='ymin', value=0, format='int')
    opObj12.addParameter(name='ymax', value=10.0, format='int')
    
    opObj12.addParameter(name='zmin', value=50, format='int') # MIN 48dB
    opObj12.addParameter(name='zmax', value=80, format='int') #53 # estaba en 75 el 21 se amplia el dB a 80
    opObj12.addParameter(name='save', value=outPath, format='str')
    opObj12.addParameter(name='localtime', value=localtime,format='int')
    opObj12.addParameter(name='show', value = 1, format='int')
    opObj12.addParameter(name='colormap', value='jet', format='str')
    opObj12.addParameter(name='exp_code', value='208', format='int')
    opObj12.addParameter(name='server', value=realtime_server)
    opObj12.addParameter(name='sender_period', value='60')
    opObj12.addParameter(name='tag', value='AMISR')
    '''
    '''
    COMENTADO
    opObj13 = spc_proc.addOperation(name='NoiselessRTIPlot', optype='external')
    # opObj13.addParameter(name='id', value='3', format='int')
    opObj13.addParameter(name='wintitle', value='RTI noiseless ISR-AMISR', format='str')
    opObj13.addParameter(name='showprofile', value='1', format='int')
    opObj13.addParameter(name='xmin', value=xmin, format='int')
    opObj13.addParameter(name='xmax', value=xmax,format='int')
    opObj13.addParameter(name='zmin', value=-0.005, format='int')
    opObj13.addParameter(name='zmax', value=0.3, format='int')
    opObj13.addParameter(name='save', value=outPath, format='str')
    opObj13.addParameter(name='localtime', value=localtime,format='int')
    opObj13.addParameter(name='show', value = 1, format='int')
    opObj13.addParameter(name='colormap', value='jet', format='str')
    opObj13.addParameter(name='exp_code', value='208', format='int')
    opObj13.addParameter(name='server', value=realtime_server)
    opObj13.addParameter(name='sender_period', value='60')
    opObj13.addParameter(name='tag', value='AMISR')

    #
    opObj13 = spc_proc.addOperation(name='NoiselessSpectraPlot', optype='external')
    opObj13.addParameter(name='wintitle', value='SPC noiseless ISR-AMISR', format='str')
    opObj13.addParameter(name='zmin', value=-0.25, format='int')
    opObj13.addParameter(name='zmax', value=1, format='int')
    opObj13.addParameter(name='save', value=outPath, format='str')
    opObj13.addParameter(name='localtime', value=localtime,format='int')
    opObj13.addParameter(name='show', value = 1, format='int')
    opObj13.addParameter(name='colormap', value='jet', format='str')
    #opObj13.addParameter(name='exp_code', value='208', format='int')
    #opObj13.addParameter(name='server', value=realtime_server)
    #opObj13.addParameter(name='sender_period', value='60')
    #opObj13.addParameter(name='tag', value='AMISR')
    COMENTADO
    '''
    #
    #
    # # #
    # # #Noise
    # #title0 = 'RTI AMISR Beam 0'
    # opObj14 = spc_proc.addOperation(name='NoisePlot', optype='external')
    # #opObj14.addParameter(name='id', value='3', format='int')
    # opObj14.addParameter(name='wintitle', value='NOISE AMISR', format='str')
    # opObj14.addParameter(name='showprofile', value='0', format='int')
    # opObj14.addParameter(name='tmin', value=xmin, format='int')
    # opObj14.addParameter(name='tmax', value=xmax, format='int')
    # # opObj14.addParameter(name='ymin', value=60, format='int')
    # # opObj14.addParameter(name='ymax', value=65.0, format='int')
    # opObj14.addParameter(name='save', value=outPath, format='str')
    # opObj14.addParameter(name='show', value = 1, format='int')#
    # opObj14.addParameter(name='localtime', value=localtime,format='int')
    # opObj14.addParameter(name='exp_code', value='208', format='int')
    # opObj14.addParameter(name='server', value=realtime_server)
    # opObj14.addParameter(name='sender_period', value='60')
    # opObj14.addParameter(name='tag', value='AMISR')


    controllerObj.start()
    controllerObj.join()

    time.sleep(60) #1 min
    # ##.......................................................................................
    # ##.......................................................................................
    # ##.......................................................................................
    # ##.......................................................................................
    rtiPath = outPath + "/noiseless_rti"
    noisePath = outPath +"/noise"
    spcPath = outPath +"/spc"
    figPaths = [rtiPath,noisePath]
    #print("Removing hdf5 files from channels...")
    for pch in figPaths:
        rmtree(pch)
    print("Proc finished ! :)")

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
