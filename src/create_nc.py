
import numpy as np
import netCDF4
from netCDF4 import date2num, num2date
import datetime as dt

__author__ = "Cesar Arturo Sanchez Pena"
__version__ = "1.0.0b"
__maintainer__ = "Cesar Arturo Sanchez Pena"
__email__ = "arturo66cta@gmail.com"
__status__ = "Developing"

def create_netcdf(info,time_,latitude,longitude,data):
    
    nc_title = info['title']
    nc_comment = info['comment']

    nc_time_units = info['time_units']

    nc_var_name = info['var_name']
    nc_var_units = info['var_units']
    
    ncfile = netCDF4.Dataset(info['file'],mode='w',format='NETCDF4_CLASSIC')
    
    ncfile.title = nc_title
    ncfile.anything = nc_comment
    
    lat_dim = len(latitude)
    lon_dim = len(longitude)
    time_dim = len(time_)
    
    lat_dim = ncfile.createDimension('lat',lat_dim)
    lon_dim = ncfile.createDimension('lon',lon_dim)
    time_dim = ncfile.createDimension('time',None)
    
    lat = ncfile.createVariable('lat',np.float32,('lat',))
    lat.units = 'degrees_north'
    lat.long_name = 'latitude'

    lon = ncfile.createVariable('lon',np.float32,('lon',))
    lon.units = 'degrees_east'
    lon.long_name = 'longitude'

    time = ncfile.createVariable('time',np.float64,('time',))
    time.units = nc_time_units
    time.long_name = 'time'
    
    var = ncfile.createVariable('var',np.float64,('time','lat','lon'))
    var.units = nc_var_units
    var.standard_name = nc_var_name
    
    lat[:] = latitude
    lon[:] = longitude
    
    var[:,:,:] = data
    
    time[:] = time_
    
    print('')
    print('File created in: ',info['file'])
