DIM=2 
N=32

BoxSize = 10.0

volume = BoxSize**DIM
density = N/volume
print ("volume = ", volume, " density = ", density)

pos=np.zeros(N, DIM)

pos=np.genfromtext('output.dat', skip_header=1)

pos = pos[:,:DIM]/BoxSize

MassCentre=np.sum(pos,axis=0)/N

for i in range(DIM):
    pos[:,i]=pos[:,i]-MassCentre[i]

