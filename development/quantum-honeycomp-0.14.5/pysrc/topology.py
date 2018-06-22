# library to calculate topological properties
from __future__ import print_function
import numpy as np
from scipy.sparse import bmat, csc_matrix
import scipy.linalg as lg
import scipy.sparse.linalg as slg
import multicell
import klist
import operators
import inout


arpack_tol = 1e-5
arpack_maxiter = 10000


def write_berry(h,kpath=None,dk=0.01,window=None,max_waves=None):
  """Calculate and write in file the Berry curvature"""
  if kpath is None: kpath = klist.default(h.geometry) # take default kpath
  fo = open("BERRY_CURVATURE.OUT","w") # open file
  for k in kpath:
    b = berry_curvature(h,k,dk=dk,window=window,max_waves=max_waves)
    fo.write(str(k[0])+"   ")
    fo.write(str(k[1])+"   ")
    fo.write(str(b)+"\n")
  fo.close() # close file






def berry_phase(h,nk=20):
  """ Calculates the Berry phase of a 1d hamiltonian"""
  if h.dimensionality != 1: raise # only for 1d
  ks = np.linspace(0.,1.,nk,endpoint=False) # list of kpoints
  hkgen = h.get_hk_gen() # get Hamiltonian generator
  wf0 = occupied_states(hkgen,ks[0]) # get occupied states, first k-point
  wfold = wf0.copy() # copy
  m = np.matrix(np.identity(len(wf0))) # initialize as the identity matrix
  for ik in range(1,len(ks)): # loop over k-points, except first one
    wf = occupied_states(hkgen,ks[ik])  # get waves
    m = m*uij(wfold,wf)   # get the uij   and multiply
    wfold = wf.copy() # this is the new old
  m = m*uij(wfold,wf0)   # last one
  d = lg.det(m) # calculate determinant
  phi = np.arctan2(d.imag,d.real)
  open("BERRY_PHASE.OUT","w").write(str(phi/np.pi)+"\n")
  return phi # return Berry phase








def berry_curvature(h,k,dk=0.01,window=None,max_waves=None):
  """ Calculates the Berry curvature of a 2d hamiltonian"""
  if h.dimensionality != 2: raise # only for 2d
  k = np.array([k[0],k[1]]) 
  dx = np.array([dk,0.])
  dy = np.array([0.,dk])
# get the function that returns the occ states
  occf = occ_states_generator(h,k,window=window,max_waves=max_waves)  
  # get the waves
  print("Doing k-point",k)
  wf1 = occf(k-dx-dy) 
  wf2 = occf(k+dx-dy) 
  wf3 = occf(k+dx+dy) 
  wf4 = occf(k-dx+dy) 
  dims = [len(wf1),len(wf2),len(wf3),len(wf4)] # number of vectors
  if max(dims)!=min(dims): # check that the dimensions are fine 
    print("WARNING, skipping this k-point",k)
    return 0.0 # if different number of vectors
  # get the uij  
  m = uij(wf1,wf2)*uij(wf2,wf3)*uij(wf3,wf4)*uij(wf4,wf1)
  d = lg.det(m) # calculate determinant
  phi = np.arctan2(d.imag,d.real)/(4.*dk*dk)
  return phi


def occ_states_generator(h,k,window=None,max_waves=None):
  """Return a function that generates the occupied wavefunctions"""
  hk_gen = h.get_hk_gen() # get hamiltonian generator
# no need of h anymore
  return lambda k: occupied_states(hk_gen,k,window=window,max_waves=max_waves) 



def occ_states2d(h,k):
  """Input is a Hamiltonian"""
  hk_gen = h.get_hk_gen() # get hamiltonian generator
  return occupied_states(hk_gen,k)


def occupied_states(hkgen,k,window=None,max_waves=None):
  """ Returns the WF of the occupied states in a 2d hamiltonian"""
  hk = hkgen(k) # get hamiltonian
  if max_waves is None: es,wfs = lg.eigh(hk) # diagonalize all waves
  else:  es,wfs = slg.eigsh(csc_matrix(hk),k=max_waves,which="SA",
                      sigma=0.0,tol=arpack_tol,maxiter=arpack_maxiter)
  wfs = np.conjugate(wfs.transpose()) # wavefunctions
  occwf = []
  for (ie,iw) in zip(es,wfs):  # loop over states
    if window is None: # no energy window
      if ie < 0:  # if below fermi
        occwf.append(iw)  # add to the list
    else: # energy window provided
      if -abs(window)< ie < 0:  # between energy window and fermi
        occwf.append(iw)  # add to the list
  return np.array(occwf)




def uij(wf1,wf2):
  """ Calcultes the matrix product of two sets of input wavefunctions"""
  out =  np.matrix(np.conjugate(wf1))*(np.matrix(wf2).T)  # faster way
  return out


def uij_slow(wf1,wf2):
  m = np.matrix(np.zeros((len(wf1),len(wf2)),dtype=np.complex))
  for i in range(len(wf1)):
    for j in range(len(wf2)):
      m[i,j] = np.sum(np.conjugate(wf1[i])*wf2[j])
  return m


def precise_chern(h,dk=0.01):
  """ Calculates the chern number of a 2d system """
  from scipy import integrate
  err = {"epsabs" : 0.01, "epsrel": 0.01,"limit" : 10}
#  err = [err,err]
  def f(x,y): # function to integrate
    return berry_curvature(h,np.array([x,y]),dk=dk)
  c = integrate.dblquad(f,0.,1.,lambda x : 0., lambda x: 1.,epsabs=1.,
                          epsrel=1.)
  chern = c[0]/(2.*np.pi)
  open("CHERN.OUT","w").write(str(chern)+"\n")
  return chern


def chern(h,dk=-1,nk=10):
  """ Calculates the chern number of a 2d system """
  c = 0.0
  ks = [] # array for kpoints
  bs = [] # array for berrys
  if dk<0: dk = 1./float(2*nk) # automatic dk
  for x in np.linspace(0.,1.,nk,endpoint=False):
    for y in np.linspace(0.,1.,nk,endpoint=False):
      ks.append([x,y])
      bs.append(berry_curvature(h,np.array([x,y]),dk=dk))
  # write in file
  fo = open("BERRY_CURVATURE.OUT","w") # open file
  for (k,b) in zip(ks,bs):
    fo.write(str(k[0])+"   ")
    fo.write(str(k[1])+"   ")
    fo.write(str(b)+"\n")
  fo.close() # close file
  ################
  c = sum(bs) # sum berry curvatures
  c = c/(2.*np.pi*nk*nk)
  open("CHERN.OUT","w").write(str(c)+"\n")
  return c



def berry_map(h,dk=-1,nk=40,reciprocal=True,nsuper=1,window=None,
               max_waves=None):
  """ Calculates the chern number of a 2d system """
  c = 0.0
  ks = [] # array for kpoints
  if dk<0: dk = 5./float(2*nk) # automatic dk
  if reciprocal: R = h.geometry.get_k2K()
  else: R = np.matrix(np.identity(3))
  fo = open("BERRY_MAP.OUT","w") # open file
  for x in np.linspace(-nsuper,nsuper,nk,endpoint=False):
    for y in np.linspace(-nsuper,nsuper,nk,endpoint=False):
      r = np.matrix([x,y,0.]).T # real space vectors
      k = np.array((R*r).T)[0] # change of basis
      b = berry_curvature(h,k,dk=dk,window=window,max_waves=max_waves)
      fo.write(str(x)+"   "+str(y)+"     "+str(b)+"\n")
  fo.close() # close file





def smooth_gauge(w1,w2):
  """Perform a gauge rotation so that the second set of waves are smooth
  with respect to the first one"""
  m = uij(w1,w2) # matrix of wavefunctions
  U, s, V = np.linalg.svd(m, full_matrices=True) # sing val decomp
  R = (U*V).H # rotation matrix
  wnew = w2.copy()*0. # initialize
  wold = w2.copy() # old waves
  for ii in range(R.shape[0]):
    for jj in range(R.shape[0]):
      wnew[ii] += R[jj,ii]*wold[jj]
  return wnew




def z2_vanderbilt(h,nk=30,nt=100,nocc=None):
  """ Calculate Z2 invariant according to Vanderbilt algorithm"""
  out = [] # output list
  path = np.linspace(0.,1.,nk) # set of kpoints
  fo = open("WANNIER_CENTERS.OUT","w")
  ts = np.linspace(0.,0.5,nt)
  wfall = [[occ_states2d(h,np.array([k,t,0.,])) for k in path] for t in ts] 
  # select a continuos gauge for the first wave
  for it in range(len(ts)-1): # loop over ts
    wfall[it+1][0] = smooth_gauge(wfall[it][0],wfall[it+1][0]) 
  for it in range(len(ts)): # loop over t points
    row = [] # empty list for this row
    t = ts[it] # select the t point
    wfs = wfall[it] # get set of waves 
    for i in range(len(wfs)-1):
      wfs[i+1] = smooth_gauge(wfs[i],wfs[i+1]) # transform into a smooth gauge
#      m = uij(wfs[i],wfs[i+1]) # matrix of wavefunctions
    m = uij(wfs[0],wfs[len(wfs)-1]) # matrix of wavefunctions
    evals = lg.eigvals(m) # eigenvalues of the rotation 
    x = np.angle(evals) # phase of the eigenvalues
    fo.write(str(t)+"    ") # write pumping variable
    row.append(t) # store
    for ix in x: # loop over phases
      fo.write(str(ix)+"  ")
      row.append(ix) # store
    fo.write("\n")
    out.append(row) # store
  fo.close()
  return np.array(out).transpose() # transpose the map




def z2_invariant(h,nk=20,nt=20,nocc=None):
  m = z2_vanderbilt(h,nk=nk,nt=nt,nocc=nocc)
  x = m[0]
  # find the position of the maximum gap at every t
  fermis = x*0. # maximum gap
  for it in range(len(x)): # loop over times
    imax,jmax = None,None
    dmax = -1 # initialize
    gapangle = None
    maxgap = -1.0 # maximum gap
    for i in range(1,len(m)):
      for j in range(i+1,len(m)):
        for ipi in [0.,1.]:
          ip = np.exp(1j*m[i][it]) # center of wave i
          jp = np.exp(1j*m[j][it]) # center of wave j
          angle = np.angle(ip+jp)+np.pi*ipi # get the angle
          #angle = np.angle(ip+jp)+np.pi # get the angle
          dp = np.exp(1j*angle) # now obtain this middle point gap
          mindis = 4.0 # calculate minimum distance
          for k in range(1,len(m)): # loop over centers
            kp = np.exp(1j*m[k][it]) # center of wave k
            dis = np.abs(dp-kp) # distance between the two points 
            if dis<mindis: mindis = dis+0. # update minimum distance
          if mindis>maxgap: # if found a bigger gap
    #        print angle,m[i][it],m[j][it]
            maxgap = mindis+0. # maximum distance
            gapangle = np.angle(dp) # update of found bigger gap
    fermis[it] = gapangle
  
  
  # now check the number of cuts of each wannier center
  
  def angleg(a,b,c):
    """Function to say if a jump has been made or not"""
    d = np.sin(a-b) + np.sin(b-c) + np.sin(c-a)
    return -d
  
  
  parity = 1 # start with
  for i in range(1,len(m)): # loop over waves 
    cwf = m[i] # center of the wave
    for it in range(len(x)-1): # loop over times
      s = np.sign(angleg(fermis[it],fermis[it+1],cwf[it])) # calculate the sign
      if s<0.:
        parity *= -1 # add a minus -1
  return parity






















def operator_berry(hin,k=[0.,0.],operator=None,delta=0.00001,ewindow=None):
  """Calculates the Berry curvature using an arbitrary operator"""
  h = multicell.turn_multicell(hin) # turn to multicell form
  dhdx = multicell.derivative(h,k,order=[1,0]) # derivative
  dhdy = multicell.derivative(h,k,order=[0,1]) # derivative
  hkgen = h.get_hk_gen() # get generator
  hk = hkgen(k) # get hamiltonian
  (es,ws) = lg.eigh(hkgen(k)) # initial waves
  ws = np.conjugate(np.transpose(ws)) # transpose the waves
  n = len(es) # number of energies
  from berry_curvaturef90 import berry_curvature as bc90
  if operator is None: operator = np.identity(dhdx.shape[0],dtype=np.complex)
  b = bc90(dhdx,dhdy,ws,es,operator,delta) # berry curvature
  return b*np.pi*np.pi*8 # normalize so the sum is 2pi Chern



def operator_berry_bands(hin,k=[0.,0.],operator=None,delta=0.00001):
  """Calculates the Berry curvature using an arbitrary operator"""
  h = multicell.turn_multicell(hin) # turn to multicell form
  dhdx = multicell.derivative(h,k,order=[1,0]) # derivative
  dhdy = multicell.derivative(h,k,order=[0,1]) # derivative
  hkgen = h.get_hk_gen() # get generator
  hk = hkgen(k) # get hamiltonian
  (es,ws) = lg.eigh(hkgen(k)) # initial waves
  ws = np.conjugate(np.transpose(ws)) # transpose the waves
  from berry_curvaturef90 import berry_curvature_bands as bcb90
  if operator is None: operator = np.identity(dhdx.shape[0],dtype=np.complex)
  bs = bcb90(dhdx,dhdy,ws,es,operator,delta) # berry curvatures
  return (es,bs*np.pi*np.pi*8) # normalize so the sum is 2pi Chern







def spin_chern(h,nk=40,delta=0.00001,k0=[0.,0.],expandk=1.0):
  """Calculate the spin Chern number"""
  kxs = np.linspace(-.5,.5,nk,endpoint=False)*expandk + k0[0]
  kys = np.linspace(-.5,.5,nk,endpoint=False)*expandk + k0[1]
  kk = [] # list of kpoints
  for i in kxs:
    for j in kys:
      kk.append(np.array([i,j])) # store vector
  sz = operators.get_sz(h) # get sz operator
  bs = [operator_berry(h,k=ki,operator=sz,delta=delta) for ki in kk] # get all berries
  fo = open("BERRY_CURVATURE_SZ.OUT","w") # open file
  for (k,b) in zip(kk,bs):
    fo.write(str(k[0])+"   ")
    fo.write(str(k[1])+"   ")
    fo.write(str(b)+"\n")
  fo.close() # close file
  bs = np.array(bs)/(2.*np.pi) # normalize by 2 pi
  return sum(bs)/len(kk)


def write_spin_berry(h,kpath,delta=0.00001,operator=None):
  """Calculate and write in file the Berry curvature"""
  if operator is None: sz = operators.get_sz(h) # get sz operator
  else: sz = operator # assign operator
  be = [operator_berry(h,k=k,operator=sz,delta=delta) for k in kpath] 
  fo = open("BERRY_CURVATURE_SZ.OUT","w") # open file
  for (k,b) in zip(kpath,be):
    fo.write(str(k[0])+"   ")
    fo.write(str(k[1])+"   ")
    fo.write(str(b)+"\n")
  fo.close() # close file






def precise_spin_chern(h,delta=0.00001,tol=0.1):
  """ Calculates the chern number of a 2d system """
  from scipy import integrate
  err = {"epsabs" : 0.01, "epsrel": 0.01,"limit" : 20}
  sz = operators.get_sz(h) # get sz operator
  def f(x,y): # function to integrate
    return operator_berry(h,np.array([x,y]),delta=delta,operator=sz)
  c = integrate.dblquad(f,0.,1.,lambda x : 0., lambda x: 1.,epsabs=tol,
                          epsrel=tol)
  return c[0]/(2.*np.pi)
