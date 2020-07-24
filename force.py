def Compute_Forces(pos,acc,ene_pot,epsilon,Boxsize,DIM,N):

    Sij=np.zeros(DIM)
    Rij=np.zeros(DIM)

    ene_pot=ene_pot*0.0
    acc=acc*0.0
    virial=0.0

    for i in range(N-1):
        for j in range(i+1, N):
            Sij=pos[i,:]-pos[j:]
            for l in range(DIM):
                if (np.abs(Sij[l])>0.5):
                    sij[l]=Sij[l]-np.copysign(1.0, Sij[l])

                    Rij = Boxsize*Sij
                    Rsqij=np.dot(Rij, Rij)

                    if Rsqij<Rcutoff**2):
                        rm2=1.0/Rsqij
                        rm6=rm2**3.0
                        rm12=rm6**2.0
                        phi=epsilon*(4.0*(rm12-rm6)-phicutoff)
                        dhpi=epsilon*24.0*rm2*(2.0*rm12-rm6)
                        ene_pot[i]=ene_pot[i]+0.5*phi
                        ene_pot[j]+=0.5*phi
                        virial-=dphi*Rsqij
                        acc[i,:]+=dphi*Sij
                        acc[j,:]-=dphi*Sij

    return acc, np.sun(ene_pot)/N, -virial/DIM
