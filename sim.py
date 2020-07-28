NSteps = 10000
deltat = 0.0032
TRequested = 0.5
DumpFreq = 100
epsilon = 1.0

def main (pos, NSteps, deltat, TRequested, DumpFreq, epsilon, BoxSize, DIM):

    N = np.size(pos[:,1])
    ene_kin_aver = np.ones(NSteps)
    ene_pot_aver = np.ones(Nsteps)
    temperature = np.ones(NSteps)
    virial = np.ones(NSteps)
    pressure = np.ones(NSteps)
    ene_pot = np.ones(N)

    vel = (np.random.randn(N,DIM)-0.5)
    acc = (np.random.randn(N,DIM)-0.5)

    f = open('traj.xyz', 'w')

    for k in range(NSteps):

        for i in range(DIM):
            period = np.where(pos[:,i] > 0.5)
            pos[period,i] = pos[period,i]-1.0
            period = np.where(pos[:,i] < -0.5)
            pos [period, i]+=1.0

        pos = pos + deltat*vel + 0.5*(deltat**2.0)*acc

        ene_kin_aver[k], temperature[k] = Calculate_temperature(vel, BoxSize, DIM, N)

        chi = np.sqrt(TRequested/temperature[k])

        vel = chi*vel + 0.5*deltat*acc

        acc, ene_pot_aver[k], virial[k] = Compute_Forces(pos, ene_pot, epsilon, BoxSize, DIM, N)

        vel = vel+0.5*deltat*acc

        ene_kin_aver[k], temperature[k] = Calculate_Temperature(vel,BoxSize,DIM,N)

        pressure[k] = density*temperature[k] +virial[k]/volume


        if (k%DumpFreq==0):
            f.write("%s\n" %(N))
            f.write("Energy %s, Temperature %.5f\n" %(ene_kin_aver[k]+ene_pot_aver[k], temperature[k]))

            for n in range(N):
                f.write("x"+" ")
                for l in range(DIM):
                    f.write(str(pos[n][l]*BoxSize)+" ")

                f.write("\n")

            if (DIM==2):
                import matplotlib.pyplot as plt 
                from IPython import display 
                plt.cla()
                plt.xlim(-0.5*BoxSize, 0.5*BoxSize)
                plt.ylim(-0.5*BoxSize, 0.5*BoxSize)

                for i in range(N):
                    plt.plot(pos[i,0]*BoxSize, pos[i,1]*BoxSize, 'o', markersize=20,)
                display.clear_output(wait=True)

                display.display(plt.gcf())
    f.close()

    return ene_kin_aver, ene_pot_aver, temperature, pressure, pos


