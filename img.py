from loadfile import loadimgs

# from svd import svd_newMatrix
from pydmd import FbDMD
import matplotlib.pyplot as plt
# import numpy as np
# import scipy.integrate
import time
from DMD import rdmd
from DMD import compute_newD
from svd import rsvd_newMatrix
from svd import rsvd
from loadfile import showimages

# 3000 is okay
imgNo = 300
A, X, Y, snapshots, x_pix, y_pix = loadimgs(imgNo)
# batchsize =
rank = 40
p = rank
q = 5
# mm = 0
# ###################################################
# for i in range(A.shape[0]):
#     if Y[i,0] == 63:
#         mm = mm +1
# print(mm)
# print("Y[400,0]:"+str(Y[400,0]))
# print(X.shape)
# print(Y.shape)
# print("********************************")
# print("A[:,0]:"+str(A[:,0]))
# print("A[:,1]:"+str(A[:,1]))
# print((A[:,0]==A[:,1]).all())
# print((A[:,0]==A[:,0]).all())
# print((X==Y).all())
# print(X)
# print(A.shape)


#############
# DMD packages
# dmd = dmd(exact=True)
# dmd.fit(A.T)
# for eig in dmd.eigs:
#     print('Eigenvalue {}: distance from unit circle {}'.format(eig, abs(eig.imag**2 + eig.real**2 - 1)))
# dmd.plot_eigs(show_axes= True, show_unit_circle= True)
#
# for mode in dmd.modes.T:
#     plt.plot(range(1,imgNo+1), mode.real)
#     plt.title("Modes")
# plt.show()

#
# for eig in dmd.eigs:
#     print('Eigenvalue {}: distance from unit circle {}'.format(eig, np.abs(eig.imag**2 + eig.real**2 - 1)))
# dmd.plot_eigs(show_axes= True, show_unit_circle= True)

# #######################
# by rsvd, we cannot compute new matrix directly even the number of images are 2, batches are needed
# start1 = time.clock()
#
# Ux, sigmax, Ax = rsvd(A = X, rank = rank, p = 0, q = 1)
# end1 = time.clock()
#
# print("rsvd:" + str(end1-start1))
#
# ########################
# # by svd, we can compute new matrix directly with 1000 images
# start2 = time.clock()
# U2, sigma2, V2 = cal_svd(X, rank)
# end2 = time.clock()
#
# print("svd:" + str(end2-start2))

# for 1000 images:
# rsvd:1.0923066157967092
# svd:189.06396405083467

start3 = time.clock()
phi, B, V= rdmd(X,Y,A,rank,p)
# print(omega)
# print(B)
# print(phi)
D_new = compute_newD(phi, B,V)
# # print("-------------------")
# # print(D_new.real)
# # # print((D_new[:,0]==D_new[:,0]).all())
showimages(D_new.real,x_pix,y_pix,imgNo)
end3 = time.clock()
print("rdmd:" + str(end3-start3))